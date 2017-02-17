from gpiozero import LED, Button
from time import sleep

redled = LED(17)
yellowled = LED(18)
button = Button(6)

while button.wait_for_press():
    redled.on()
    yellowled.off()
    sleep(0.1)
    redled.off()
    yellowled.on()
    sleep(0.2)
