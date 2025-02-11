import RPi.GPIO as GPIO, time
from .PWM import PWM

class Servo(PWM):
    limiter: int = 25
    position: int = 90
    
    def __init__(self, pin=None, debug=False):
        self.frequency = 50
        self.duty_cycle = 0
        self.debug = debug
        if pin: self.pin = pin
        
        if not GPIO.getmode():
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.pin, GPIO.OUT, initial=self.default_state)
        self.gpio_pwm = GPIO.PWM(self.pin, self.frequency)
        
    def cw(self, value):
        self.delta_pos(-value)
    
    def ccw(self, value):
        self.delta_pos(value)
        
    def set_pos(self, value=None):
        """ Set servo position

        Args:
            value (int, optional): _int_ 0-180 Degrees. Defaults to 90.
        """
        if value is None: value = self.position
        if value > 180 - self.limiter:
            if self.debug: print(f"Servo: {value} out of range, limiting to {180 - self.limiter}")
            value = 180 - self.limiter
        elif value < self.limiter:
            if self.debug: print(f"Servo: {value} out of range, limiting to {self.limiter}")
            value = self.limiter
            
        if self.debug: print(f"Setting Servo {self.name if self.name is not None else self.pin} to {value}")
        self.set_duty_cycle(duty_cycle=(2.5 + 10 * value/180))
        self.start()
        time.sleep(0.3)
        self.stop()
        self.position = value
        
    def delta_pos(self, delta):
        self.position += delta
        if self.position > 180 - self.limiter:
            self.position = 180 - self.limiter
        elif self.position < self.limiter:
            self.position = self.limiter
        self.set_pos()