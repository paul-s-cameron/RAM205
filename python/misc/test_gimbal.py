from time import sleep
from RPiC.Rover import Rover

rover = Rover(debug=True)

rover.gimbal.set_pos(90, 90)

sleep(2)

rover.gimbal.set_pos(180, 180)

sleep(2)

rover.gimbal.set_pos(0, 0)

sleep(2)

rover.gimbal.set_pos(90, 90)