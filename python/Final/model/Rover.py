import RPi.GPIO as GPIO
from .Drive import Drive
from .Gimbal import Gimbal
from .LED import LED
from .RoverPins import RoverPins
from .TrackSensor import TrackSensor
from .Sonar import Sonar
from .Buzzer import Buzzer
from .Warner import Warner

class Rover:
    def __init__(self, debug=False):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        self.drive = Drive(
            RoverPins.DRIVE_LEFT_IN1_PIN,
            RoverPins.DRIVE_LEFT_IN2_PIN,
            RoverPins.DRIVE_LEFT_ENA_PIN,
            RoverPins.DRIVE_RIGHT_IN1_PIN,
            RoverPins.DRIVE_RIGHT_IN2_PIN,
            RoverPins.DRIVE_RIGHT_ENB_PIN,
            debug=debug
        )
        self.gimbal = Gimbal(
            RoverPins.SERVO_HEADER_2,
            RoverPins.SERVO_HEADER_3,
            debug=debug
        )
        self.led = LED(
            RoverPins.LED_RED_PIN,
            RoverPins.LED_GREEN_PIN,
            RoverPins.LED_BLUE_PIN,
            debug=debug
        )
        self.track_sensor = TrackSensor(
            RoverPins.LINE_FOLLOWER_PIN_1,
            RoverPins.LINE_FOLLOWER_PIN_2,
            RoverPins.LINE_FOLLOWER_PIN_3,
            RoverPins.LINE_FOLLOWER_PIN_4,
            debug=debug
        )
        self.sonar = Sonar(
            RoverPins.SERVO_HEADER_1,
            RoverPins.SONAR_ECHO_PIN,
            RoverPins.SONAR_TRIG_PIN,
            debug=debug
        )
        self.buzzer = Buzzer(RoverPins.BUZZER, debug=debug)
        self.warner = Warner(RoverPins.WARNER, debug=debug)
        
        if debug:
            print("Rover initialized")
        
    def __del__(self):
        del(self.buzzer)
        del(self.warner)
        del(self.drive)
        del(self.gimbal)
        del(self.led)
        del(self.track_sensor)
        del(self.sonar)