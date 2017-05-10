from gpiozero import Motor, DistanceSensor, Button, InputDevice
from time import sleep, time
from multiprocessing import Process, Value, Array


leftMotor = Motor(13,22)
rightMotor = Motor(12,23)

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

def Go_Forward(Power=0):
	leftMotor.forward(Power*0.945)
	rightMotor.forward(Power)

####################################################

# def Calculate_Wheel_Distance(wheelSensor, wheelDistance, wheelSide):
	# print("Calculating...")
	# currentSensorState = wheelSensor.is_active
	# print("Calculating...")
	# while True :
		# if currentSensorState != wheelSensor.is_active :
			# wheelDistance[wheelSide] += 1
			# currentSensorState = wheelSensor.is_active
		# print(wheelDistance[wheelSide])


def Calculate_Wheel_Distance(wheelDistance, wheelSide):
	print("Initiating...")
	# wheelSensor = InputDevice(26)
	# currentSensorState = wheelSensor.is_active
	print("Calculating...")
	while True :
		# if currentSensorState != wheelSensor.is_active :
		wheelDistance =+ 1
			# currentSensorState = wheelSensor.is_active
		sleep(0.5)
		print(wheelDistance)


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
		
wheelDistance = Value('i', 0)

p = Process(target=Calculate_Wheel_Distance, args=(wheelDistance, 0,))
# p = Process(target=Calculate_Wheel_Distance, args=(leftSensor, wheelDistance, 0))
p.start
# Go_Forward(0.8)
startTime = time()
while time() - startTime < 3 :
	print(wheelDistance.value)
	sleep(1)

	
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
