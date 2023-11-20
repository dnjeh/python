import datetime
import Adafruit_DHT as dht

t, h = dht.read_retry(dht.DHT11, 4)

print(h)
print(t)