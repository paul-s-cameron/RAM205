from dataclasses import dataclass

@dataclass
class RoverPins:
    WARNER: int = 25
    BUZZER: int = 8
    
    LED_RED_PIN: int = 22
    LED_GREEN_PIN: int = 27
    LED_BLUE_PIN: int = 24
    
    LINE_FOLLOWER_PIN_1: int = 3
    LINE_FOLLOWER_PIN_2: int = 5
    LINE_FOLLOWER_PIN_3: int = 4
    LINE_FOLLOWER_PIN_4: int = 18
    
    DRIVE_LEFT_IN1_PIN: int = 20
    DRIVE_LEFT_IN2_PIN: int = 21
    DRIVE_LEFT_ENA_PIN: int = 16
    
    DRIVE_RIGHT_IN1_PIN: int = 19
    DRIVE_RIGHT_IN2_PIN: int = 26
    DRIVE_RIGHT_ENB_PIN: int = 13
    
    SONAR_ECHO_PIN: int = 0
    SONAR_TRIG_PIN: int = 1
    
    SERVO_HEADER_1: int = 23
    SERVO_HEADER_2: int = 11
    SERVO_HEADER_3: int = 9
    SERVO_HEADER_4: int = 10
    SERVO_HEADER_5: int = 25
    SERVO_HEADER_6: int = 2