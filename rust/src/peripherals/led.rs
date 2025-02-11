// region:    --- Modules

use super::consts::{LED_R, LED_G, LED_B};

use crate::Result;

use rppal::gpio::{Gpio, OutputPin};

// endregion: --- Modules

const FREQUENCY: f64 = 1000.0;

pub struct Color {
    pub r: f64,
    pub g: f64,
    pub b: f64,
}

impl Color {
    pub fn from_srgb(r: f64, g: f64, b: f64) -> Self {
        Self { r, g, b }
    }

    pub const WHITE: Color = Color { r: 1.0, g: 1.0, b: 1.0 };
    pub const OFF: Color = Color { r: 0.0, g: 0.0, b: 0.0 };

    // Primary Colors
    pub const RED: Color = Color { r: 1.0, g: 0.0, b: 0.0 };
    pub const GREEN: Color = Color { r: 0.0, g: 1.0, b: 0.0 };
    pub const BLUE: Color = Color { r: 0.0, g: 0.0, b: 1.0 };

    // Secondary Colors
    pub const YELLOW: Color = Color { r: 1.0, g: 1.0, b: 0.0 };
    pub const CYAN: Color = Color { r: 0.0, g: 1.0, b: 1.0 };
    pub const MAGENTA: Color = Color { r: 1.0, g: 0.0, b: 1.0 };

    // Tertiary Colors
    pub const ORANGE: Color = Color { r: 1.0, g: 0.5, b: 0.0 };
    pub const SPRING_GREEN: Color = Color { r: 0.0, g: 1.0, b: 0.5 };
    pub const SKY_BLUE: Color = Color { r: 0.0, g: 0.5, b: 1.0 };
    pub const VIOLET: Color = Color { r: 0.5, g: 0.0, b: 1.0 };
    pub const ROSE: Color = Color { r: 1.0, g: 0.0, b: 0.5 };
    pub const CHARTREUSE: Color = Color { r: 0.5, g: 1.0, b: 0.0 };
}

pub struct LED {
    led_r: OutputPin,
    led_g: OutputPin,
    led_b: OutputPin,

    color: Color,
    brightness: f64,
}

impl LED {
    pub fn new(gpio: &Gpio) -> Result<Self> {
        Ok(Self {
            led_r: gpio.get(LED_R)?.into_output(),
            led_g: gpio.get(LED_G)?.into_output(),
            led_b: gpio.get(LED_B)?.into_output(),
            color: Color::WHITE,
            brightness: 1.0,
        })
    }

    pub fn set_color(&mut self, color: Color, brightness: Option<f64>) -> Result<()> {
        self.color = color;
        if let Some(brightness) = brightness { self.brightness = brightness };
        self.led_r.set_pwm_frequency(FREQUENCY, self.brightness * self.color.r)?;
        self.led_g.set_pwm_frequency(FREQUENCY, self.brightness * self.color.g)?;
        self.led_b.set_pwm_frequency(FREQUENCY, self.brightness * self.color.b)?;
        Ok(())
    }
}