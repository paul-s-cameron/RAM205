// region:    --- Modules

use super::consts::{ECHO, TRIG};

use crate::Result;

use rppal::gpio::{Event, Gpio, InputPin, OutputPin, Trigger};
use std::{thread, time::{Duration, Instant}};

// endregion: --- Modules

pub enum Unit {
    Millimeters,
    Centimeters,
    Decimeters,
    Meters,
}

pub struct Ultrasonic {
    echo: InputPin,
    trig: OutputPin,
    sound_speed: f32,
    timeout: Duration,
}

impl Ultrasonic {
    fn calibration_calc(temp: f32) -> (f32, Duration) {
        /// Speed of sound at 0C in m/s.
        const SOUND_SPEED_0C: f32 = 331.3;
        /// Increase speed of sound over temperature factor m/[sC].
        const SOUND_SPEED_INC_OVER_TEMP: f32 = 0.606;
        /// Maximum measuring range for HC-SR04 sensor in m.
        const MAX_RANGE: f32 = 4.0;

        // Speed of sound, depending on ambient temperature (if `temp` is `None`, default to 20C).
        let sound_speed = SOUND_SPEED_0C + (SOUND_SPEED_INC_OVER_TEMP * temp);

        let timeout = Duration::from_secs_f32(MAX_RANGE / sound_speed * 2.);

        (sound_speed, timeout)
    }

    pub fn new(gpio: &Gpio, temp: Option<f32>) -> Result<Self> {
        let mut echo = gpio.get(ECHO)?.into_input_pulldown();
        echo.set_interrupt(Trigger::Both, None)?;

        let (sound_speed, timeout) = Self::calibration_calc(temp.unwrap_or(20.));

        Ok(Self {
            trig: gpio.get(TRIG)?.into_output_low(),
            echo,
            sound_speed,
            timeout,
        })
    }

    /// Calibrate the sensor with the given **ambient temperature** (`temp`) expressed as *Celsius
    /// degrees*.
    pub fn calibrate(&mut self, temp: f32) {
        (self.sound_speed, self.timeout) = Self::calibration_calc(temp);
    }

    /// Perform **distance measurement**.
    ///
    /// Returns `Ok` variant if measurement succedes. Inner `Option` value is `None` if no object
    /// is present within maximum measuring range (*4m*); otherwhise, on `Some` variant instead,
    /// contained value represents distance expressed as the specified `unit`
    /// (**unit of measure**).
    pub fn measure_distance(&mut self, unit: Unit) -> Result<Option<f32>> {
        self.trig.set_high();
        thread::sleep(Duration::from_micros(10));
        self.trig.set_low();

        'rising: loop {
            match self.echo.poll_interrupt(false, Some(self.timeout))? {
                Some(Event { trigger: Trigger::RisingEdge, .. }) => {
                    break 'rising
                }
                _ => {
                    return Ok(None);
                }
            }
        }
        let instant = Instant::now();

        'falling: loop {
            match self.echo.poll_interrupt(false, Some(self.timeout))? {
                Some(Event { trigger: Trigger::FallingEdge, .. }) => {
                    break 'falling
                }
                _ => {
                    return Ok(None);
                }
            }
        }

        // Distance in m.
        let distance = (self.sound_speed * instant.elapsed().as_secs_f32()) / 2.;

        Ok(Some(match unit {
            Unit::Millimeters => distance * 1000.,
            Unit::Centimeters => distance * 100.,
            Unit::Decimeters => distance * 10.,
            Unit::Meters => distance,
        }))
    }
}