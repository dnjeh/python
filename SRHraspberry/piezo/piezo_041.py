import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Melody = (262, 294, 330, 349, 392, 440, 493, 523)

piezo = 21
GPIO.setup(piezo, GPIO.OUT)

Buzz = GPIO.PWM(piezo, 50)
Buzz.start(50)

try:
    for i in Melody:
        Buzz.ChangeFrequency(i)
        time.sleep(0.5)
    Buzz.stop()

except KeyboardInterrupt:
    pass

GPIO.cleanup()
