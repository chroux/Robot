from gpiozero import DistanceSensor, Robot, SmoothedInputDevice, Button, InputDevice
from time import sleep, time


robot = Robot(left=(13,22), right=(12,23))

# rightSensor = SmoothedInputDevice(16,queue_len=30)
# rightSensor._queue.start()


########################################
# rightSensor = InputDevice(16)

# sleep(1)
# print("Ready")

# sensorValues = []
# for i in range(100) :
	# sensorValues.append(rightSensor.is_active)

# print(sensorValues)

# def getChangeStateTime():
	# while True :
		# currentState = rightSensor.is_active
		# while currentState == rightSensor.is_active :
			# 0
		# return time()
	
# print("Transition Time: ", getChangeStateTime())
########################################

rightSensor = Button(16,bounce_time=0.1)

sleep(1)
print("Ready")
robot.forward(0.5)
def waitForOn():
	currentTime = time()
	while rightSensor.is_pressed :
		0
	while not rightSensor.is_pressed :
		0
	startTime = time()
	while rightSensor.is_pressed :
		0
	while not rightSensor.is_pressed :
		0
	endTime = time()
	return ["at", currentTime, " in ON position for ", int((endTime-startTime)*1000000), " microseconds"]

sensorInfo = []	
i = 0
nbRecords = 200
while i < nbRecords :
	triggerInfo = waitForOn()
	sensorInfo.append(triggerInfo)
	i += 1
for i in range(nbRecords):
	print(sensorInfo[i])

	#print(triggerInfo)
	#sleep(1)
	
# Test button
# while True:
	# print("Etat :", rightSensor.is_pressed)
	# print("Etat :", rightSensor.values)
	# sleep(1)



# robot.forward(0.5)
# while True :
	# nbSamples = 20
	# onTime = 0.0
	# for i in range(nbSamples):
		# rightSensor.wait_for_press
		# startTime = time()
		# rightSensor.wait_for_release
		# rightSensor.wait_for_press
		# onTime += (time()- startTime)
		# rightSensor.wait_for_release
	# speed = onTime  * 1000000
	# print("Speed in microseconds", speed)
	# print(startTime, onTime)
	# sleep(1)
	
# while True :
	# count = 0
	# rightSensor.wait_for_press
	# startTime = time()
	# while time()-startTime < 1 :
		# rightSensor.wait_for_release
		# count += 1
		# rightSensor.wait_for_press
	# print ("number of ticks :", count)