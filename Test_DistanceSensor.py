from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=6, trigger=5)
while True:
    print('Distance: ', sensor.distance * 100)
    sleep(1)
	
	
# import gpiozero
# import time

# trigger = gpiozero.LED(5)
# print("Starting")
# for i in range(10) :
	# print("on")
	# trigger.on()
	# time.sleep(1)
	# print("off")
	# trigger.off()
	# time.sleep(0.5)
# trigger.close()