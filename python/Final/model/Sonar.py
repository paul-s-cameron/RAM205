import RPi.GPIO as GPIO, time
from .Servo import Servo
from .Ultrasonic import Ultrasonic

class Sonar(Servo):
    name: str = "Sonar"
    ultrasonic: Ultrasonic
    
    def __init__(self, pin=23, echoPin=0, trigPin=1, sample_freq=5, debug=False):
        super().__init__(pin, debug)
        self.ultrasonic = Ultrasonic(echoPin, trigPin, sample_freq, debug)
        
    def distance(self):
        return self.ultrasonic.distance