// region:    --- Modules

use yahboom_rover::pause;
use yahboom_rover::prelude::*;
use yahboom_rover::Result;

use rppal::gpio::Gpio;

// endregion: --- Modules

fn main() -> Result<()> {
    let gpio = Gpio::new()?;
    let mut rover = Rover::new(gpio)?;
    
    for _ in 0..10 {
        rover.warner.pin.set_high();
        pause!(b"Warner on...");
        rover.warner.pin.set_low();
        pause!(b"Warner off...");
    }

    Ok(())
}