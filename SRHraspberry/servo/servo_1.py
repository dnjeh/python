import RPi.GPIO as GPIO
import time
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3.0)

try:
    for i in range(0, 3):
        pwm.ChangeDutyCycle(3.0)
        time.sleep(1)
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)
        pwm.ChangeDutyCycle(12.0)
        time.sleep(1)
    pwm.ChangeDutyCycle(0.0)
    pwm.stop()

except KeyboardInterrupt:
    pass
GPIO.cleanup()