import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
sw_pin = 21
led_pin1 = 23
led_pin2 = 24

GPIO.setup(sw_pin, GPIO.IN)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

P_sw = False
ledOn = False

try:
    while True:
        N_sw = GPIO.input(sw_pin)

        if N_sw and not P_sw:
            print("rising edge")
            ledOn = not ledOn
            GPIO.output(led_pin1, ledOn)
            GPIO.output(led_pin2, ledOn)
        elif not N_sw and P_sw:
            print("falling edge")

        else:
            pass
        P_sw = N_sw

except KeyboardInterrupt:
    pass

GPIO.cleanup()
