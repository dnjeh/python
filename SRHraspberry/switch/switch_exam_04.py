import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
sw_pin = 21
led_pin1 = 23

GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin1, GPIO.OUT)

pwm1 = GPIO.PWM(led_pin1, 500.0)
pwm1.start(0.0)

swState = 0

N_sw = 0
P_sw = 0

def swOn():
    global N_sw
    global P_sw
    N_sw = GPIO.input(sw_pin)

    if N_sw is not P_sw:
        P_sw = N_sw
        if N_sw == 1:
            return 1
    return 0

try:
    while True:
        if swOn() == 1:
            swState = swState + 1
            if swState >= 4:
                swState = 0
            time.sleep(0.2)
            print(swState)

            if swState == 0:
                pwm1.ChangeDutyCycle(0)
                print("duty:0")
            elif swState == 1:
                pwm1.ChangeDutyCycle(30)
                print("duty:30")    
            elif swState == 2:
                pwm1.ChangeDutyCycle(60)
                print("duty:60")
            elif swState == 3:
                pwm1.ChangeDutyCycle(100)
                print("duty:100")
            
except KeyboardInterrupt:
    pass

GPIO.cleanup()

