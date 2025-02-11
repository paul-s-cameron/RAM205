from time import sleep
from model.Rover import Rover

rover = Rover(debug=True)

rover.sonar.set_pos(90)
print(rover.sonar.distance())

sleep(2)

rover.sonar.set_pos(180)
print(rover.sonar.distance())

sleep(2)

rover.sonar.set_pos(0)
print(rover.sonar.distance())

sleep(2)

rover.sonar.set_pos(90)
print(rover.sonar.distance())