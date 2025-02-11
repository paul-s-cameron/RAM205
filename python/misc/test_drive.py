from time import sleep
from RPiC.Rover import Rover

rover = Rover(debug=True)

rover.drive.forward(1.0, 50)

sleep(2)

rover.drive.stop()

sleep(1)

rover.drive.LM_forward(50)

sleep(2)

rover.drive.RM_reverse(50)

sleep(2)

rover.drive.stop()