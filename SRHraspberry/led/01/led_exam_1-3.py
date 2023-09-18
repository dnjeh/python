# led_exam_1-3.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin1 = 23
led_pin2 = 24

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

try:
	while True:
		GPIO.output(led_pin1, True)
		GPIO.output(led_pin2, True)
		time.sleep(0.009)

		GPIO.output(led_pin1, False)
		GPIO.output(led_pin2, False)
		time.sleep(0.001)

except KeyboardInterrupt:
	pass
	
GPIO.cleanup()
