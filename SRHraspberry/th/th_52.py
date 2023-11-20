import time
import Adafruit_DHT
import dht11
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin = 4

GPIO.setup(pin, GPIO.IN)

dhtDevice = Adafruit_DHT.DHT11(pin=pin)

while True:
    try:
        temperture = dhtDevice.temperture
        humidity = dhtDevice.humidity
        print("Temp : ", temperture)
        print("Humi : ", humidity)
        time.sleep(2)
    except RuntimeError as error:
        print(error.args[0])
    except KeyboardInterrupt:
        break

dhtDevice.exit()