# import gpiozero
# import time
# import signal

# sleep = time.sleep

# motor = gpiozero.Motor(13, 22)
# artee = gpiozero.Robot((13,22), (12,23))

# artee.left(1)
# time.sleep(5)

# artee.forward(1)
# time.sleep(1)
# for i in range(3):
	# artee.left(0.5)
	# time.sleep(4)
	# artee.forward(0.4)
	# time.sleep(2)
# artee.right(0.5)
# time.sleep(1.2)

# for i in range(8):
    # artee.forward(0.5)
    # sleep(1)
    # artee.left(0.5)
    # sleep(0.40)

# for i in range(4):
	# artee.forward(0.5)
	# sleep(1)
	# artee.stop()
	# sleep(1)
	# artee.left(0.4)
	# sleep(0.4)
	# artee.stop()
	# sleep(1)

# artee.stop()
# print("setting up sensor")
# sensor = gpiozero.DistanceSensor(echo=6, trigger=5, max_distance=1, threshold_distance=0.3)
# print("Sensor ready, Trigger is :", sensor.trigger)
# while True:
	# print("Ready")
	# print('Distance: ', sensor.distance * 100)
	# time.sleep(1)



# sensor.when_in_range = robot.backward
# sensor.when_out_of_range = robot.stop
# signal.pause()

# motor.forward(0.2)
# print("Forward")
# time.sleep(2)
# motor.forward(0.5)
# time.sleep(2)
# motor.backward(0.3)
# print("Backward")
# time.sleep(2)


# speed = 0.0
# for power in range(0, 110, 10):
	# speed = power / 100.0
	# print("forward power :", speed)
	# motor.forward(speed)
	# time.sleep(2)

# motor.stop

# essai clavier
import curses
from gpiozero import Robot

robot = Robot(left=(13,22), right=(12,23))

# actions = {
    # curses.KEY_UP:    print ("avant"), #robot.forward,
    # curses.KEY_DOWN:  print ("arrière"), #robot.backward,
    # curses.KEY_LEFT:  print ("gauche"), #robot.left,
    # curses.KEY_RIGHT: print ("droite"), #robot.right,
    # }
actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.left,
    curses.KEY_RIGHT: robot.right,
    }
	
def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY DOWN
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY UP
            robot.stop()

curses.wrapper(main)

robot.stop()
print("Stop")
