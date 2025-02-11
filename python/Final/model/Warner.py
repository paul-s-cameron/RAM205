import RPi.GPIO as GPIO
from .PWM import PWM

class Warner(PWM):
    def __init__(self, pin=25, debug=False):
        self.pin = pin
        self.frequency = 1
        self.duty_cycle = 50
        self.name = "Warner"
        self.debug = debug
        
        if not GPIO.getmode():
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.pin, GPIO.OUT, initial=self.default_state)
        self.gpio_pwm = GPIO.PWM(self.pin, self.frequency)