from gpiozero import Motor, DistanceSensor, Button, InputDevice
from time import sleep, time


#robot = Robot(left=(13,22), right=(12,23))
leftMotor = Motor(13,22)
rightMotor = Motor(12,23)

# rightSensor = Button(16,bounce_time=0.001)
# leftSensor = Button(26,bounce_time=0.001)

rightSensor = InputDevice(16)
leftSensor = InputDevice(26)

sonarSensor = DistanceSensor(echo=6, trigger=5)


sleep(1)
print("Ready")
while sonarSensor.distance < 0.3 :
	print("Sonar not Ready yet", sonarSensor.distance)
	sleep(2)
print(sonarSensor.distance)

####################################################

def GoForward(Power=0):
	leftMotor.forward(Power*0.945)
	rightMotor.forward(Power)

####################################################

# def GetSpeed(Sensor,Timeout=0.2) :
	# currentTime = time()
	# if Sensor.is_pressed :
		# while Sensor.is_pressed and time() - currentTime < Timeout :
			# 0
		# startTime = time()
		# while not Sensor.is_pressed and time() - currentTime < Timeout :
			# 0
		# while Sensor.is_pressed and time() - currentTime < Timeout :
			# 0
		# endTime = time()	
	
	# else :
		# while not Sensor.is_pressed and time() - currentTime < Timeout :
			# 0
		# startTime = time()
		# while Sensor.is_pressed and time() - currentTime < Timeout :
			# 0
		# while not Sensor.is_pressed and time() - currentTime < Timeout :
			# 0
		# endTime = time()
	# if time() - currentTime < Timeout :
		# return 0.011/(endTime-startTime)
	# else :
		# return 0.0


		
		
####################################################

def incrementCount():
	rightWheelDistance += 1
	print("it is moving!")
		
sensorInfo = []
rightWheelDistance=0
leftWheelDistance=0
startTime = time()
refDistance = 200
rightSensorState = rightSensor.is_active
leftSensorState = leftSensor.is_active

while ( rightWheelDistance < refDistance ) and (sonarSensor.distance > 0.3 ):
	GoForward(1-0.8*rightWheelDistance/refDistance)
	if rightSensorState != rightSensor.is_active :
		rightWheelDistance += 1
		sensorInfo.append(["time :" ,time() - startTime ,"Power: ", 1,1, "Distance : ", leftWheelDistance, rightWheelDistance, "m/s"])
		rightSensorState = rightSensor.is_active
	if leftSensorState != leftSensor.is_active :
		leftWheelDistance += 1
		sensorInfo.append(["time :" ,time() - startTime ,"Power: ", 1,1, "Distance : ", leftWheelDistance, rightWheelDistance, "m/s"])
		leftSensorState = leftSensor.is_active
	
GoForward()
print("number of records :",len(sensorInfo))	
for i in range(len(sensorInfo)):
	print(sensorInfo[i])
print("number of records :",len(sensorInfo))	
	
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


	
########### Records Power vs Speed ########################################
	
# nbRecords = 200	
# sensorInfo = []
# power = 0.0	
# i = 0

# while i < nbRecords :
	# power = i/nbRecords
	# robot.forward(power)
	# sleep(0.1)
	# sensorInfo.append(["power : ", power, "speed : ", GetSpeed(leftSensor), "m/s"])
	# i += 1
# for i in range(nbRecords):
	# print(sensorInfo[i])

	
###########################################################################

########### Ridding only the Right wheel ########################################
	
# RefSpeed = 0.5
# nbRecords = 200	
# sensorInfo = []
# power = 0.0	
# i = 0
# while i < nbRecords :
	# currentSpeed = GetSpeed(rightSensor)
	# if currentSpeed < 1 :
		# power += 1.0*(RefSpeed - currentSpeed)
		# if power < 0 :
			# power = 0
		# if power > 1 :
			# power = 1
		# sensorInfo.append(["power : ", power, "speed : ", currentSpeed, "m/s"])
		# rightMotor.forward(power)
		# i += 1

# for i in range(nbRecords):
	# print(sensorInfo[i])
###########################################################################

# LEFTWHEEL = 0
# RIGHTWHEEL = 1
# RefSpeed = 0.5
# nbRecords = 100
# sensorInfo = []
# power=[0,0]
# i = 0
# StartTime = time()
# currentSpeed = [0,0]
# while i < nbRecords :
	##currentSpeed = [GetSpeed(leftSensor),GetSpeed(rightSensor)]
	# currentSpeed[LEFTWHEEL] = GetSpeed(leftSensor)
	# currentSpeed[RIGHTWHEEL] = GetSpeed(rightSensor)
	
	# if currentSpeed[LEFTWHEEL] < 1 and currentSpeed[RIGHTWHEEL] < 1 :
		# power[LEFTWHEEL] += 1.0*(RefSpeed - currentSpeed[LEFTWHEEL]) 
		# power[RIGHTWHEEL] += 1.0*(currentSpeed[LEFTWHEEL] - currentSpeed[RIGHTWHEEL])
				##power[RIGHTWHEEL] += 1.0*(RefSpeed - currentSpeed[RIGHTWHEEL]) + 1.0*(currentSpeed[LEFTWHEEL] - currentSpeed[RIGHTWHEEL])
		
		# if power[LEFTWHEEL] < 0 :
			# power[LEFTWHEEL] = 0
		# if power[LEFTWHEEL] > 1 :
			# power[LEFTWHEEL] = 1
		# if power[RIGHTWHEEL] < 0 :
			# power[RIGHTWHEEL] = 0
		# if power[RIGHTWHEEL] > 1 :
			# power[RIGHTWHEEL] = 1
		# leftMotor.forward(power[LEFTWHEEL])
		# rightMotor.forward(power[RIGHTWHEEL])
		# sensorInfo.append(["time :" ,time() - StartTime ,"Power: ", power[LEFTWHEEL],power[RIGHTWHEEL], "Speed : ", currentSpeed[LEFTWHEEL], currentSpeed[RIGHTWHEEL], "m/s"])
		# i += 1

# leftMotor.forward(0)
# rightMotor.forward(0)
# for i in range(nbRecords):
	# print(sensorInfo[i])
