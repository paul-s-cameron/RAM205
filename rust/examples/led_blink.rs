// region:    --- Modules

use yahboom_rover::prelude::*;
use yahboom_rover::Result;

use rppal::gpio::Gpio;

// endregion: --- Modules

fn main() -> Result<()> {
    let gpio = Gpio::new()?;
    let mut rover = Rover::new(gpio)?;
    
    for _ in 0..10 {
        rover.led.set_color(Color::WHITE, Some(1.0))?;
        sleep!(500);
        rover.led.set_color(Color::WHITE, Some(0.0))?;
        sleep!(500);
    }
    
    Ok(())
}