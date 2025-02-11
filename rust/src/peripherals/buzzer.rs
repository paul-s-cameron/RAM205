// region:    --- Modules

use super::consts::BUZZER;

use crate::{Result, utils};

use rppal::gpio::{Gpio, OutputPin};

// endregion: --- Modules

pub struct Buzzer {
    pub pin: OutputPin,
    pub frequency: f64,
    pub duty_cycle: f64,
    pub polarity: utils::Polarity,
}

impl Buzzer {
    pub fn new(gpio: &Gpio, frequency: f64, duty_cycle: f64) -> Result<Self> {
        Ok(Self {
            pin: gpio.get(BUZZER)?.into_output_high(),
            frequency,
            duty_cycle,
            polarity: utils::Polarity::DefaultHigh,
        })
    }

    pub fn beep(&mut self) -> Result<()> {
        self.pin.set_low();
        sleep!(100);
        self.pin.set_high();
        Ok(())
    }

    pub fn start(&mut self) -> Result<()> {
        self.pin.set_pwm_frequency(self.frequency, self.duty_cycle)?;
        Ok(())
    }

    pub fn stop(&mut self) -> Result<()> {
        self.pin.clear_pwm()?;
        match self.polarity {
            utils::Polarity::DefaultHigh => {
                self.pin.set_high();
            }
            utils::Polarity::DefaultLow => {
                self.pin.set_low();
            }
        }
        Ok(())
    }

    pub fn set_frequency(&mut self, frequency: f64) {
        self.frequency = frequency;
    }

    pub fn set_duty_cycle(&mut self, duty_cycle: f64) {
        self.duty_cycle = duty_cycle;
    }
}