# led_exam_01.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin1 = 23
led_pin2 = 24

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

GPIO.output(led_pin1, True)
GPIO.output(led_pin2, True)
time.sleep(2.0)

GPIO.output(led_pin1, False)
GPIO.output(led_pin2, False)
GPIO.cleanup()
