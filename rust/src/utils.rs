#[macro_export]
macro_rules! sleep {
    ($millis:expr) => {
        std::thread::sleep(std::time::Duration::from_millis($millis))
    };
}

#[macro_export]
macro_rules! pause {
    ($text:expr) => {
        {
            use std::io::{stdin, stdout, Read, Write};
            let mut stdout = stdout();
            stdout.write($text).unwrap();
            stdout.flush().unwrap();
            stdin().read(&mut [0]).unwrap();
        }
    };
}

/// Defines the pins default state
#[allow(dead_code)]
pub enum Polarity {
    DefaultHigh,
    DefaultLow,
}