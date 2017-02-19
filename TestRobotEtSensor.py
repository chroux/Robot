from gpiozero import DistanceSensor, Robot, SmoothedInputDevice
from time import sleep


sensor = DistanceSensor(echo=6, trigger=5)
robot = Robot(left=(13,22), right=(12,23))

power = 0.5
maxDistance = 0.3
i = 0
side = 0
sleep(1)
while True :
	Distance = sensor.distance
	# print(Distance)
	if Distance < maxDistance :
		robot.stop
		print("Obstacle : ", Distance)
		robot.backward(power)
		sleep(1)
		if side == 1 :
			robot.right(power)
			side = 0
		else :
			robot.left(power)
			side = 1
		sleep(0.3)
		robot.stop
	if Distance > maxDistance :
		i += 1
		if i > 1 :
			print("Tout va bien : ", Distance)
			i = 0
		robot.forward(power)
	sleep(0.5)
	


		
		
		
# sleep(1)
# print(sensor.distance*100)
# sensor.when_in_range=robot.backward(0.5)
# sleep(1)
# print(sensor.distance*100)
# sensor.when_out_of_range=robot.stop()


# while True:
	# if sensor.when_in_range :
		# print("in range")
	# if sensor.when_out_of_range :
		# print("out of range")
	# print(sensor.distance)
	# sleep(1)
	