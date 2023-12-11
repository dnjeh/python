import RPi.GPIO as GPIO
import time
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3.0)

try:
    for high in range(30, 121):
        pwm.ChangeDutyCycle(high/10)
        time.sleep(0.02)
    pwm.ChangeDutyCycle(3.0)
    time.sleep(2.0)

except KeyboardInterrupt:
    pass
pwm.stop()
GPIO.cleanup()