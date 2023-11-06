import RPi.GPIO as GPIO
import time
Piezo = 21
sw = 18
sing = (391, 391, 440, 440, 391, 391, 330, 330,
        391, 391, 330, 330, 294, 294, 294, 0.1,
        391, 391, 440, 440, 391, 391, 330, 330,
        391, 330, 294, 330, 262, 262
        )
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Piezo, GPIO.OUT)
GPIO.setup(sw, GPIO.IN)

Buzz = GPIO.PWM(Piezo, 50)

def Buzz_Freq(Piano):
    Buzz.ChangeFrequency(Piano)
    time.sleep(0.4)

try:
    while 1:
        if GPIO.wait_for_edge(sw, GPIO.RISING):
            Buzz.start(50)
            for i in sing:
                Buzz_Freq(i)
                time.sleep(0.1)
            Buzz.stop()
except KeyboardInterrupt:
    pass
GPIO.cleanup()