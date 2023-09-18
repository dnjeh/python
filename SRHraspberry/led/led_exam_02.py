# led_exam_02.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin1 = 23
led_pin2 = 24
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

try:
	while True:
		for t_high in range(1, 11):
			cnt=1
			while True:
				GPIO.output(led_pin1, True)
				GPIO.output(led_pin2, True)
				time.sleep(t_high * 0.001)
				GPIO.output(led_pin1, False)
				GPIO.output(led_pin2, False)
				time.sleep((10 - t_high) * 0.001)
				cnt += 1
				if cnt==10:
					break
		for t_high in range(10, 0, -1):
			cnt=1
			while True:
				GPIO.output(led_pin1, True)
				GPIO.output(led_pin2, True)
				time.sleep(t_high * 0.001)
				GPIO.output(led_pin1, False)
				GPIO.output(led_pin2, False)
				time.sleep((10 - t_high) * 0.001)
				cnt += 1
				if cnt==10:
					break

except KeyboardInterrupt:
	pass
	
GPIO.cleanup()
