import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
sw_pin = 21
led_pin1 = 23
led_pin2 = 24


GPIO.setup(sw_pin, GPIO.IN)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

try:
    while True:
        swinput = GPIO.input(sw_pin)
        GPIO.output(led_pin1, swinput)
        GPIO.output(led_pin2, swinput)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
