import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Melody = (262, 294, 330, 349, 392, 440, 493, 523)

piezo = 21
GPIO.setup(piezo, GPIO.OUT)

Buzz = GPIO.PWM(piezo, 50)
def Buzz_Freq(Piano):
    print("주파수 : %d 입력"%Piano)
    Buzz.ChangeFrequency(Piano)
    time.sleep(0.3)
    Buzz.stop()
try:
    while 1:
        key = input()
        key = key[0]
        Buzz.start(50)
        if(key == '1'):
            Buzz_Freq(262)
        elif(key == '2'):
            Buzz_Freq(294)
        elif(key == '3'):
            Buzz_Freq(330)
        elif(key == '4'):
            Buzz_Freq(349)
        elif(key == '5'):
            Buzz_Freq(392)
        elif(key == '6'):
            Buzz_Freq(440)
        elif(key == '7'):
            Buzz_Freq(493)
        elif(key == '8'):
            Buzz_Freq(523)

except KeyboardInterrupt:
    pass
GPIO.cleanup()
