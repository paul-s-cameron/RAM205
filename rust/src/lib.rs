// region:    --- Modules

mod error;
pub use error::{Error, Result};

#[macro_use]
pub mod utils;

mod peripherals;
use peripherals::prelude::*;
mod track;
use track::Track;

use rppal::gpio::Gpio;

pub mod prelude {
    pub use super::{
        Rover,
        peripherals::prelude::{Color, Unit},
        sleep,
    };
}

// endregion: --- Modules

#[allow(dead_code)]
pub struct Rover {
    pub gpio: Gpio,
    pub track: Track,

    // Peripherals
    pub buzzer: Buzzer,
    pub ultrasonic: Ultrasonic,
    pub led: LED,
    pub warner: Warner,
}

impl Rover {
    pub fn new(gpio: Gpio) -> Result<Self> {
        let track = Track::new(&gpio)?;
        let buzzer = Buzzer::new(&gpio, 1.0, 0.9)?;
        let ultrasonic = Ultrasonic::new(&gpio, None)?;
        let led = LED::new(&gpio)?;
        let warner = Warner::new(&gpio, 1.0, 0.5)?;
        
        Ok(Self {
            gpio,
            track,
            buzzer,
            ultrasonic,
            led,
            warner,
        })
    }
}