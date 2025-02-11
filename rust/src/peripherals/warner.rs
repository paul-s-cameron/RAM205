// region:    --- Modules

use super::consts::WARNER;

use crate::Result;

use rppal::gpio::{Gpio, OutputPin};

// endregion: --- Modules

pub struct Warner {
    pub pin: OutputPin,
    pub frequency: f64,
    pub duty_cycle: f64,
}

impl Warner {
    pub fn new(gpio: &Gpio, frequency: f64, duty_cycle: f64) -> Result<Self> {
        Ok(Self {
            pin: gpio.get(WARNER)?.into_output_high(),
            frequency,
            duty_cycle,
        })
    }

    pub fn start(&mut self) -> Result<()> {
        self.pin.set_pwm_frequency(self.frequency, self.duty_cycle)?;
        Ok(())
    }

    pub fn stop(&mut self) -> Result<()> {
        self.pin.clear_pwm()?;
        Ok(())
    }

    pub fn set_frequency(&mut self, frequency: f64) {
        self.frequency = frequency;
    }

    pub fn set_duty_cycle(&mut self, duty_cycle: f64) {
        self.duty_cycle = duty_cycle;
    }
}