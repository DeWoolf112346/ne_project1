import random
import time
snow = '*'
snap = ' '
while True:
    snow_1 = snow * random.randint(1, 2)
    snap_1 = snap * random.randint(1, 3)
    print((snow_1 + snap_1*5) * 100)
    time.sleep(0.5)
