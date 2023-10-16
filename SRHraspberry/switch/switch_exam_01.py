import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
sw_pin = 21

GPIO.setup(sw_pin, GPIO.IN)

try:
    while True:
        swinput = GPIO.input(sw_pin)
        print(swinput)

except KeyboardInterrupt:
    pass

GPIO.cleanup()