# led_exam_03.py

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led_pin1 = 23
led_pin2 = 24
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

pwm1 = GPIO.PWM(led_pin1, 0.1)
pwm1.start(50.0)
pwm2 = GPIO.PWM(led_pin2, 0.1)
pwm2.start(50.0)

try:
	while True:
		pass
except KeyboardInterrupt:
	pass

pwm1.stop()
pwm2.stop()
GPIO.cleanup()
