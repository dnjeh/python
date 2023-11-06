import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

piezo = 21
GPIO.setup(piezo, GPIO.OUT)
Buzz = GPIO.PWM(piezo, 50)

Melody = (262, 294, 330, 349, 392, 440, 493, 523)

def Buzz_Freq(Piano):
    print("주파수 : %d 입력"%Piano)
    Buzz.ChangeFrequency(Piano)
    time.sleep(0.3)
    Buzz.stop()

try:
    while 1:
        key = int(input())
        Buzz.start(50)
        for i in range(0, 8):
            if(key - 1 == i):
                Buzz_Freq(Melody[i])
                break
except KeyboardInterrupt:
    pass
GPIO.cleanup()