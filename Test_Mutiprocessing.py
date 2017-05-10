from multiprocessing import Process, Value
from time import sleep, time
from gpiozero import Motor, DistanceSensor, Button, InputDevice

def f(name,titi = 0):
	print('hello', name)
	titi.value += 2
	print("titi is ",titi.value)
	sleep(2)
	titi.value += 2
	print("titi is ",titi.value)

	
	
def Calculate_Wheel_Distance(sensorPin, wheelDistance, stopCounting):
	print("Initiating...")
	wheelSensor = InputDevice(sensorPin)
	sleep(2)
	currentSensorState = wheelSensor.is_active
	print("Current state ", currentSensorState)
	print("Calculating...")
	while stopCounting.value == 0:
		if currentSensorState != wheelSensor.is_active :
			wheelDistance.value += 1
			currentSensorState = wheelSensor.is_active
			print(wheelDistance.value)	
	
	
leftSensorPin = 26	
leftDistance = Value('i',0)
stopCounting = Value('i',0)
startTime = time()
if __name__ == '__main__':
	# p = Process(target=f, args=('bob',toto,))
	p = Process(target=Calculate_Wheel_Distance, args=(leftSensorPin, leftDistance, stopCounting,))
	p.start()
	while time() - startTime < 20 :
		print("leftDistance is ",leftDistance.value)
		sleep(1)
	stopCounting.value = 1
	p.join()
	print("leftDistance is ",leftDistance.value)