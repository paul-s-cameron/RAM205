import RPi.GPIO as GPIO

@dataclass
class Signal:
    pin:    int
    active: int

    def __post_init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        
    def __del__(self):
        GPIO.cleanup(self.pin)

def get_signal(signal: Signal):
    """Get the state of a signal

    Args:
        signal (Signal): Signal object

    Returns:
        _type_: _bool_ True if the signal is active
    """
    return GPIO.input(signal.pin) == signal.active