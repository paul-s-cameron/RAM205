#![allow(dead_code)]

mod buzzer;
mod ultrasonic;
mod led;
mod warner;

#[allow(unused_imports)]
pub mod prelude {
    pub use super::{
        buzzer::Buzzer,
        ultrasonic::{Ultrasonic, Unit},
        led::{LED, Color},
        warner::Warner,
    };
}

pub mod consts {
    // region:    --- Hardware
    pub const BUZZER: u8 = 8;
    pub const WARNER: u8 = 23;
    // endregion: --- Hardware
    // region:    --- Servo
    pub const J1: u8 = 23;
    pub const J2: u8 = 11;
    pub const J3: u8 = 9;
    pub const J4: u8 = 10;
    pub const J5: u8 = 25;
    pub const J6: u8 = 2;
    // endregion: --- Servo
    // region:    --- LED
    pub const LED_R: u8 = 22;
    pub const LED_G: u8 = 27;
    pub const LED_B: u8 = 24;
    // endregion: --- LED
    // region:    --- Ultrasonic
    pub const ECHO: u8 = 30;
    pub const TRIG: u8 = 31;
    // endregion: --- Ultrasonic
}