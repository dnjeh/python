import RPi.GPIO as GPIO
import time
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3.0)

def angleToDutyConvert(angle):
    dutyCycle = angle/18+2
    GPIO.output(servo_pin, GPIO.HIGH)
    pwm.ChangeDutyCycle(dutyCycle)
    time.sleep(0.15)
    GPIO.output(servo_pin, GPIO.LOW)
    time.sleep(0.15)

def sweep(degrees):
    for pos in range(0, degrees, 5):
        print(pos)
        angleToDutyConvert(pos)
    for pos in range(degrees, 0, -5):
        print(pos)
        angleToDutyConvert(pos)
try:
    while True:
        sweep(45)
        time.sleep(1)
        sweep(90)
        time.sleep(1)
except KeyboardInterrupt:
    pass
pwm.stop()
GPIO.cleanup()