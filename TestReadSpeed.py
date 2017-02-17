# GPIO port numbers  
import wiringpi
import time       # allows us a time delay  

LeftSpeedPort = 26
RightSpeedPort = 16

LeftPwmPort = 13
RightPwmPort = 12

LeftDirPort = 22
RightDirPort = 23

RightPwmSpeed = 0
RightPwmSpeed = input("Vitesse : ")

# Initialize
wiringpi.wiringPiSetupGpio()

try : 

	# Set up Left Wheel
	wiringpi.pinMode(LeftSpeedPort, 0) # sets to input
	wiringpi.pinMode(LeftDirPort, 1) # sets to output
	wiringpi.pinMode(LeftPwmPort, 2) # sets to PWM mode

	# Set up Right Wheel
	wiringpi.pinMode(RightSpeedPort, 0) # sets to input
	wiringpi.pinMode(RightDirPort, 1) # sets to output
	wiringpi.pinMode(RightPwmPort, 2) # sets to PWM mode

	# Start Right Wheel
	wiringpi.digitalWrite(RightDirPort,0) #Forward
	wiringpi.pwmWrite(RightPwmPort,RightPwmSpeed) #Start slow

	#wiringpi.pullUpDnControl(RightSpeedPort, 2)

	RightSpeedCount = 0
	RightSpeedState=wiringpi.digitalRead(RightSpeedPort)
	print("etat depart:", RightSpeedState)
	StartTime = time.time()
	while time.time() - StartTime < 5 : 
		if RightSpeedState != wiringpi.digitalRead(RightSpeedPort):
			RightSpeedState=wiringpi.digitalRead(RightSpeedPort)
			RightSpeedCount += 1
			print("count :", RightSpeedCount)
		time.sleep(0.001)
	print(RightSpeedCount)	
	


finally:  # when you CTRL+C exit, we clean up
        wiringpi.digitalWrite(LeftDirPort, 0) # sets port to 0 (0V, off)
        wiringpi.pinMode(LeftDirPort, 0)      # sets back to input Mode
        wiringpi.pwmWrite(LeftPwmPort, 0) # sets port to 0 (0V, off)
        wiringpi.pinMode(LeftPwmPort, 0) # Sets back to input Mode

        wiringpi.digitalWrite(RightDirPort, 0) # sets port to 0 (0V, off)
        wiringpi.pinMode(RightDirPort, 0)      # sets back to input Mode
        wiringpi.pwmWrite(RightPwmPort, 0) # sets port to 0 (0V, off)
        wiringpi.pinMode(RightPwmPort, 0) # Sets back to input Mode

	wiringpi.pullUpDnControl(RightSpeedPort, 0)
	print("finished")

