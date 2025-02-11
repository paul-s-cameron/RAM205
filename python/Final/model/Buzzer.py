import RPi.GPIO as GPIO
from .PWM import PWM

class Buzzer(PWM):
    def __init__(self, pin=8, debug=False):
        self.pin = pin
        self.frequency = 1
        self.duty_cycle = 80
        self.invert_duty = True
        self.default_state = 1
        self.name = "Buzzer"
        self.debug = debug
        
        if not GPIO.getmode():
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.pin, GPIO.OUT, initial=self.default_state)
        self.gpio_pwm = GPIO.PWM(self.pin, self.frequency)
        
    def beep(self, frequency=8, duty_cycle=80):
        self.set_frequency(frequency)
        self.set_duty_cycle(duty_cycle)
        self.start()