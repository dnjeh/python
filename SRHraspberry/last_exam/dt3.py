import Adafruit_DHT as dht
import datetime
import time

sensor = dht.DHT11
h, t = dht.read_retry(sensor, 4)

if h is not None and t is not None:
    while 1:
        now = time.localtime()
        str1=("%04d/%02d/%02d %02d:%02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
        h, t = dht.read_retry(sensor, 4)
        str2=("{} {}% {}*C".format(str1, h, t))
        print(str2)
        time.sleep(1)
else:
    print("error")