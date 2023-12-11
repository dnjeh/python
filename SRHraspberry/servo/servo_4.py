import RPi.GPIO as GPIO
from time import sleep 
servo_pin = 18
sw1_pin = 20
sw2_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(sw1_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(sw2_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3.0)
servo_deg=0

def set_servo_degree(degree):
    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0
    duty = 3+degree/20
    pwm.ChangeDutyCycle(duty)

try:
    while 1:
        if GPIO.input(sw1_pin):
            servo_deg += 10
            if servo_deg >180:
                servo_deg=180
            set_servo_degree(servo_deg)
            print(servo_deg)
            sleep(1)
        elif GPIO.input(sw2_pin):
            servo_deg -= 10
            if servo_deg <0:
                servo_deg=0
            set_servo_degree(servo_deg)
            print(servo_deg)
            sleep(1)
except KeyboardInterrupt:
    pass
pwm.stop()
GPIO.cleanup()