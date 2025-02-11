import sys
sys.path.append("/home/ram/model/")

from Rover import Rover
from rover_factory import make_rover
from time import sleep

rover1 = make_rover()
sleep(1)
rover1.buzzer.beep()
sleep(2)
rover1.buzzer.stop()
rover1.warner.start()
sleep(4)
rover1.warner.stop()

rover1.drive.forward(speed=30)
sleep(4)
rover1.drive.stop()