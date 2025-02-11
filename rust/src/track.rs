#![allow(dead_code)]

// region:    --- Modules

use crate::Result;

use std::time::Duration;
use rppal::gpio;

// endregion: --- Modules

const PWM_A_PIN: u8 = 16;
const PWM_B_PIN: u8 = 13;
const AIN_1_PIN: u8 = 21;
const AIN_2_PIN: u8 = 20;
const BIN_1_PIN: u8 = 26;
const BIN_2_PIN: u8 = 19;

const PWM_FREQUENCY: f64 = 2000.0;

pub struct LeftMotor {
    /// Left motor speed
    pub pwm: gpio::OutputPin,
    /// Left motor backward
    pub in_1: gpio::OutputPin,
    /// Left motor forward
    pub in_2: gpio::OutputPin,

    speed: f64,
}

impl LeftMotor {
    pub fn forward(&mut self, speed: Option<f64>) -> Result<()> {
        if let Some(speed) = speed { self.set_speed(speed)? };
        self.in_1.set_low();
        self.in_2.set_high();
        Ok(())
    }

    pub fn backward(&mut self, speed: Option<f64>) -> Result<()> {
        if let Some(speed) = speed { self.set_speed(speed)? };
        self.in_2.set_low();
        self.in_1.set_high();
        Ok(())
    }

    pub fn speed(&self) -> f64 {
        self.speed
    }

    pub fn set_speed(&mut self, speed: f64) -> Result<()> {
        self.speed = speed;
        self.pwm.set_pwm_frequency(PWM_FREQUENCY, self.speed)?;
        Ok(())
    }
}

pub struct RightMotor {
    /// Right motor speed
    pub pwm: gpio::OutputPin,
    /// Right motor backward
    pub in_1: gpio::OutputPin,
    /// Right motor forward
    pub in_2: gpio::OutputPin,

    speed: f64,
}

impl RightMotor {
    pub fn forward(&mut self, speed: Option<f64>) -> Result<()> {
        if let Some(speed) = speed { self.set_speed(speed)? };
        self.in_1.set_low();
        self.in_2.set_high();
        Ok(())
    }

    pub fn backward(&mut self, speed: Option<f64>) -> Result<()> {
        if let Some(speed) = speed { self.set_speed(speed)? };
        self.in_2.set_low();
        self.in_1.set_high();
        Ok(())
    }

    pub fn speed(&self) -> f64 {
        self.speed
    }

    pub fn set_speed(&mut self, speed: f64) -> Result<()> {
        self.speed = speed;
        self.pwm.set_pwm_frequency(PWM_FREQUENCY, self.speed)?;
        Ok(())
    }
}

pub struct Track {
    pub left: LeftMotor,
    pub right: RightMotor,
}

impl Track {
    pub fn new(gpio: &gpio::Gpio) -> gpio::Result<Self> {
        let a_in_1 = gpio.get(AIN_1_PIN)?.into_output_low();
        let a_in_2 = gpio.get(AIN_2_PIN)?.into_output_low();
        let mut pwm_a = gpio.get(PWM_A_PIN)?.into_output_low();
        let b_in_1 = gpio.get(BIN_1_PIN)?.into_output_low();
        let b_in_2 = gpio.get(BIN_2_PIN)?.into_output_low();
        let mut pwm_b = gpio.get(PWM_B_PIN)?.into_output_low();

        pwm_a.set_pwm_frequency(2000.0, 0.0)?;
        pwm_b.set_pwm_frequency(2000.0, 0.0)?;

        Ok(Self {
            left: LeftMotor {
                pwm: pwm_a,
                in_1: a_in_1,
                in_2: a_in_2,
                speed: 0.0,
            },
            right: RightMotor {
                pwm: pwm_b,
                in_1: b_in_1,
                in_2: b_in_2,
                speed: 0.0,
            }
        })
    }

    pub fn forward(&mut self, speed: Option<f64>) -> Result<()> {
        self.left.forward(speed)?;
        self.right.forward(speed)?;
        Ok(())
    }

    pub fn backward(&mut self, speed: Option<f64>) -> Result<()> {
        self.left.backward(speed)?;
        self.right.backward(speed)?;
        Ok(())
    }

    pub fn speed(&mut self, speed: f64) -> Result<()> {
        self.left.set_speed(speed)?;
        self.right.set_speed(speed)?;
        Ok(())
    }

    pub fn lerp_speed(&mut self, from: Option<f64>, to: f64, duration: Duration) -> Result<()> {
        let l_from: f64 = from.unwrap_or(self.left.speed());
        let r_from: f64 = from.unwrap_or(self.right.speed());

        let duration_millis = duration.as_millis();
        let resolution: u128 = 100;
        let steps: u128 = duration_millis / resolution;

        if steps == 0 {
            self.left.set_speed(to)?;
            self.right.set_speed(to)?;
            return Ok(());
        }

        let l_step = (to - l_from) / steps as f64;
        let r_step = (to - r_from) / steps as f64;
        
        for step in 0..steps  {
            let l_speed = l_from + l_step * step as f64;
            let r_speed = r_from + r_step * step as f64;

            self.left.set_speed(l_speed)?;
            self.right.set_speed(r_speed)?;

            sleep!(resolution as u64);
        }

        self.left.set_speed(to)?;
        self.right.set_speed(to)?;

        Ok(())
    }
}