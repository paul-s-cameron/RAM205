import sys, time
sys.path.append('/home/ram/model')

from BTCommands import CommandID, CommandType
from BTCommandService import BTCommandService
from Rover import Rover

def obstacle_avoidance(rover: Rover):
    rover.drive.set_speed(10)
    rover.sonar.set_pos(90)
    for i in range(5):
        rover.drive.forward()
        while rover.sonar.distance() > 25:
            time.sleep(0.1)
        print(f"Obstacle detected: {rover.sonar.distance()}")
        rover.drive.stop()
            
        # Scan for a clear path
        rover.sonar.set_pos(130)
        time.sleep(0.1)
        left_distance = rover.sonar.distance()
        rover.sonar.set_pos(50)
        time.sleep(0.1)
        right_distance = rover.sonar.distance()
        rover.sonar.set_pos(90)
        
        rover.drive.set_speed(30)
        if left_distance > right_distance:
            rover.drive.rotate_left()
            time.sleep(1)
        else:
            rover.drive.rotate_right()
            time.sleep(1)
        rover.drive.stop()
        rover.drive.set_speed(10)
        time.sleep(0.3)
    rover.drive.stop()

def main():
    rover = Rover()
    bt_service = BTCommandService()
    last_command = None
    
    while True:
        command = bt_service.get_command()
        
        # Quit logic
        if command.command_id == CommandID.LED_ON and last_command == CommandID.LED_OFF:
            print("Quitting")
            break
        
        if command.command_id == CommandID.STOP:
            rover.drive.stop()
        elif command.command_id == CommandID.FORWARD:
            rover.drive.forward()
        elif command.command_id == CommandID.BACKWARD:
            rover.drive.reverse()
        elif command.command_id == CommandID.LEFT:
            rover.drive.turn_left()
        elif command.command_id == CommandID.RIGHT:
            rover.drive.turn_right()
        elif command.command_id == CommandID.LEFT_ALT:
            rover.drive.rotate_left()
        elif command.command_id == CommandID.RIGHT_ALT:
            rover.drive.rotate_right()
        elif command.command_id == CommandID.BEEP:
            rover.buzzer.toggle()
        elif command.command_id == CommandID.SPEED_UP:
            rover.drive.delta_speed(10)
        elif command.command_id == CommandID.SPEED_DOWN:
            rover.drive.delta_speed(-10)
        elif command.command_id == CommandID.SERVO_ANALOG:
            rover.drive.set_speed(command.value / 180 * 100)
        elif command.command_id == CommandID.SERVO_LEFT:
            rover.sonar.set_pos(160)
        elif command.command_id == CommandID.SERVO_RIGHT:
            rover.sonar.set_pos(20)
        elif command.command_id == CommandID.SERVO_MID:
            rover.sonar.set_pos(90)
        elif command.command_id == CommandID.LED_OFF:
            rover.led.off()
        elif command.command_id == CommandID.LED_ON:
            rover.led.set_color(255, 255, 255)
            rover.led.on()
        elif command.command_id == CommandID.LED_RED:
            rover.led.set_color(255, 0, 0)
            rover.led.on()
        elif command.command_id == CommandID.LED_GREEN:
            rover.led.set_color(0, 255, 0)
            rover.led.on()
        elif command.command_id == CommandID.LED_BLUE:
            rover.led.set_color(0, 0, 255)
            rover.led.on()
        elif command.command_id == CommandID.LED_RED_ANALOG:
            rover.led.set_color(red=command.value)
        elif command.command_id == CommandID.LED_GREEN_ANALOG:
            rover.led.set_color(green=command.value)
        elif command.command_id == CommandID.LED_BLUE_ANALOG:
            rover.led.set_color(blue=command.value)
        elif command.command_id == CommandID.OBSTACLE_START:
            obstacle_avoidance(rover)
        else:
            print(f"Unknown command: {command}")
            
        last_command = command.command_id

if __name__ == '__main__':
    main()