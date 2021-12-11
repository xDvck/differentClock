import time
from datetime import datetime

if __name__ == "__main__":
    t = datetime.now()
    x_hour = -23 + int(t.strftime("%H"))
    x_min = -59 + int(t.strftime("%M"))
    x_sec = -59 + int(t.strftime("%S"))

    while True:
        print(x_hour, ":", x_min, ":", x_sec)

        if x_sec <= 0:
            x_sec += 1

        if x_sec == 1 and x_min == 1:
            x_sec = -59
            x_min += 1
        elif x_sec == 1:
            x_sec = -59
            x_min += 1

        if x_min == 1:
            x_sec = -59
            x_min = -59
            x_hour += 1

        if x_hour == 1:
            x_hour = -23
            x_min = -59

        time.sleep(1)

