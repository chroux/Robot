# Using GPIO port numbers  
import wiringpi
import time       # allows us a time delay  

# Initialize
wiringpi.wiringPiSetupGpio()

# Identify GPIO port distribution
LEFTSIDE, RIGHTSIDE= 0, 1
FORWARDDIR, REVERSEDIR = 0, 1
SPEEDPORT=[26,16] 	# 26 and 16 for measuring speed
PWMPORT=[13,12]		# 13 and 12 for PWM speed control
DIRPORT=[22,23]		# 22 and 23 for Motor direction control




def GetPwmRatioAndDirection(powerRate=0) : # powerRate is between -1024 and 1024, 0 is idle
# returns a 2 element table as [directionPinValue,pwmDutyCycle]
	if powerRate >= 0 :
		return [FORWARDDIR, powerRate]
	if powerRate < 0 :
		return [REVERSEDIR, 1024 + powerRate]
		

def DriveWheel(powerRate=0,wheelSide=0) : # powerRate is between -1024 and 1024, 0 is idle
# Drives a wheel at the given powerRate 
	PwmRatioAndDirection = GetPwmRatioAndDirection(powerRate)
	wiringpi.digitalWrite(DIRPORT[wheelSide],PwmRatioAndDirection[0])
	wiringpi.pwmWrite(PWMPORT[wheelSide],PwmRatioAndDirection[1])


def GetSpeeds(timeInSeconds=0.01) :
	SpeedCount = [0,0]
	SpeedState=[wiringpi.digitalRead(SPEEDPORT[RIGHTSIDE]),wiringpi.digitalRead(SPEEDPORT[LEFTSIDE])]
	#print("etats depart:", SpeedState)
	StartTime = time.time()
	while time.time() - StartTime < timeInSeconds : 
		if SpeedState[LEFTSIDE] != wiringpi.digitalRead(SPEEDPORT[LEFTSIDE]):
			SpeedState[LEFTSIDE], SpeedCount[LEFTSIDE] = wiringpi.digitalRead(SPEEDPORT[LEFTSIDE]), SpeedCount[LEFTSIDE]+1
		if SpeedState[RIGHTSIDE] != wiringpi.digitalRead(SPEEDPORT[RIGHTSIDE]):
			SpeedState[RIGHTSIDE], SpeedCount[RIGHTSIDE] = wiringpi.digitalRead(SPEEDPORT[RIGHTSIDE]), SpeedCount[RIGHTSIDE]+1
		time.sleep(0.001)
	#print("Current Speed :", [SpeedCount[LEFTSIDE]/timeInSeconds,SpeedCount[RIGHTSIDE]/timeInSeconds])
	return [int(SpeedCount[LEFTSIDE]/timeInSeconds),int(SpeedCount[RIGHTSIDE]/timeInSeconds)]
	#return [SpeedCount[LEFTSIDE],SpeedCount[RIGHTSIDE]]
	



try : 

	# Drives each wheel from full reserve to full forward and check speed precision at each step
	# by changing variable SpeedTime, one can evaluate the precision of the speed readings


	# Set up Wheels
	for WheelSide in [LEFTSIDE, RIGHTSIDE] :
		wiringpi.pinMode(SPEEDPORT[WheelSide], 0) # sets to input
		wiringpi.pinMode(DIRPORT[WheelSide], 1) # sets to output
		wiringpi.pinMode(PWMPORT[WheelSide], 2) # sets to PWM mode

	
	SpeedTime = 0.3
	Increment = 10
	for WheelSide in [LEFTSIDE, RIGHTSIDE] :
		print("Wheel Side :",WheelSide)
		PowerRate = 650
		DriveWheel(PowerRate, WheelSide)
		time.sleep(2)
#		for AskedSpeed in range(-60, 61, 10) :
		AskedSpeed = 60
		if True :
			StartTime = time.time()
			# Give it 10 seconds to reach AskedSpeed
			StartSpeeds = GetSpeeds(SpeedTime)
			while time.time() - StartTime < 10 : 
				CurrentSpeed = GetSpeeds(SpeedTime)[WheelSide]				
				if AskedSpeed > 0 :
					if CurrentSpeed < AskedSpeed :
						PowerRate += Increment
						if PowerRate > 1024 : 
							PowerRate = 1024
					if CurrentSpeed > AskedSpeed :
						PowerRate -= Increment
						if PowerRate < 0 : 
							PowerRate = 0
				if AskedSpeed < 0 :
					if CurrentSpeed < -1 * AskedSpeed :
						PowerRate -= Increment
						if PowerRate < -1024 : 
							PowerRate = -1024
					if CurrentSpeed > -1 * AskedSpeed :
						PowerRate += Increment
						if PowerRate > 0 : 
							PowerRate = 0
				DriveWheel(PowerRate, WheelSide)
				print("Power, Speed : ", CurrentSpeed, PowerRate)
			#EndSpeeds = GetSpeeds(SpeedTime)
			#print("Power, Speed : ",PowerRate,  StartSpeeds[WheelSide], EndSpeeds[WheelSide])

		time.sleep(0.5)
		DriveWheel(0, WheelSide)	
	
	


finally:  # when you CTRL+C exit, we clean up

	# Reset Left Wheel
	for WheelSide in [LEFTSIDE, RIGHTSIDE] :
		wiringpi.pwmWrite(PWMPORT[WheelSide], 0) # PWM to 0
		wiringpi.pinMode(PWMPORT[WheelSide], 0) # sets to input
		wiringpi.pinMode(SPEEDPORT[WheelSide], 0) # set to input
		wiringpi.pullUpDnControl(SPEEDPORT[WheelSide], 0)
		wiringpi.digitalWrite(DIRPORT[WheelSide], 0) # set output to 0
		wiringpi.pinMode(DIRPORT[WheelSide], 0) # set to input
	
	print("finished")

