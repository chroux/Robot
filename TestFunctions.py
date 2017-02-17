LEFTSIDE, RIGHTSIDE= 0, 1
FORWARDDIR, REVERSEDIR = 0, 1
SPEEDPORT=[26,16] 	# 26 and 16 for measuring speed
PWMPORT=[13,12]		# 13 and 12 for PWM speed control
DIRPORT=[22,23]		# 22 and 23 for Motor direction control

print(SPEEDPORT)
print("left side speed port :",SPEEDPORT[LEFTSIDE])
print("right side speed port :",SPEEDPORT[RIGHTSIDE])



def GetPwmRatioAndDirection(powerRate=0) : # powerRate is between -1024 and 1024, 0 is idle
	if powerRate >= 0 :
		return [FORWARDDIR, powerRate]
	if powerRate < 0 :
		return [REVERSEDIR, 1024 + powerRate]
		


def DriveWheel(pwmRatioAndDirection=[0,0],wheelSide=0)
	wiringpi.digitalWrite(DIRPORT[wheelSide],pwmRatioAndDirection[0])
	wiringpi.pwmWrite(PWMPORT[wheelSide],pwmRatioAndDirection[1])

		
print(GetPwmRatioAndDirection(600))
