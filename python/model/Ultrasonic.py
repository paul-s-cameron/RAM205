import RPi.GPIO as GPIO, time
from .PWM import PWM

class Ultrasonic():
    debug: bool = False
    
    INVALID_DISTANCE = -1
    
    t1: float = 0
    t2: float = 0
    distance: float = INVALID_DISTANCE
    
    trigger: PWM
    
    def __init__(self, echoPin=0, trigPin=1, sample_freq=5, debug=False) -> None:
        self.EchoPin, self.TrigPin = echoPin, trigPin
        
        if not GPIO.getmode():
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
        
        self.trigger = PWM(trigPin, sample_freq, 1)
        self.trigger.start()
        
        GPIO.setup(self.EchoPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.EchoPin, GPIO.BOTH, callback=self.sonar_callback)
        
        self.debug = debug
        
    def __del__(self):
        GPIO.cleanup(self.EchoPin)
        
    def sonar_callback(self, channel):
        if self.t1 == self.t2:
            self.t1 = time.time()
        else:
            self.t2 = time.time()
            delta = self.t2 - self.t1
            self.distance = (delta * 340 / 2) * 100
            if self.distance > 100:
                self.distance = self.INVALID_DISTANCE
            self.t1 = self.t2