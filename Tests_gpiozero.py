import gpiozero
import time
# import signal

# motor = gpiozero.Motor(13, 22)
# robot = gpiozero.Robot((13,22), (12,23))

# robot.left(1)
# time.sleep(5)

# robot.forward(1)
# time.sleep(1)

# robot.right(0.5)
# time.sleep(1.2)

# robot.stop()

print("setting up sensor")
sensor = gpiozero.DistanceSensor(echo=6, trigger=5, max_distance=1, threshold_distance=0.3)
print("Sensor ready, Trigger is :", sensor.trigger)
while True:
	print("Ready")
	print('Distance: ', sensor.distance * 100)
	time.sleep(1)



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
print("Stop")
