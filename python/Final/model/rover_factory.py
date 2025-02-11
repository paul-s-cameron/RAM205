from Rover import Rover
from RoverPins import RoverPins
from Buzzer import Buzzer
from Drive import Drive
from Gimbal import Gimbal
from LED import LED
from TrackSensor import TrackSensor
from Sonar import Sonar
from Warner import Warner

def make_rover(debug=False):
    
    rover = Rover()
    
    rover.drive = Drive(
        RoverPins.DRIVE_LEFT_IN1_PIN,
        RoverPins.DRIVE_LEFT_IN2_PIN,
        RoverPins.DRIVE_LEFT_ENA_PIN,
        RoverPins.DRIVE_RIGHT_IN1_PIN,
        RoverPins.DRIVE_RIGHT_IN2_PIN,
        RoverPins.DRIVE_RIGHT_ENB_PIN,
        debug=debug
    )
    rover.gimbal = Gimbal(
        RoverPins.SERVO_HEADER_2,
        RoverPins.SERVO_HEADER_3,
        debug=debug
    )
    rover.led = LED(
        RoverPins.LED_RED_PIN,
        RoverPins.LED_GREEN_PIN,
        RoverPins.LED_BLUE_PIN,
        debug=debug
    )
    rover.track_sensor = TrackSensor(
        RoverPins.LINE_FOLLOWER_PIN_1,
        RoverPins.LINE_FOLLOWER_PIN_2,
        RoverPins.LINE_FOLLOWER_PIN_3,
        RoverPins.LINE_FOLLOWER_PIN_4,
        debug=debug
    )
    rover.sonar = Sonar(
        RoverPins.SERVO_HEADER_1,
        RoverPins.SONAR_ECHO_PIN,
        RoverPins.SONAR_TRIG_PIN,
        debug=debug
    )
    rover.buzzer = Buzzer(RoverPins.BUZZER, debug)
    rover.warner = Warner(RoverPins.WARNER, debug)
    
    return rover