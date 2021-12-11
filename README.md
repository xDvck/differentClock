# differentClock
A clock that displays time as x &lt;= 0. E.g: Time = 24:00 + (-11:30) = 12:30

Given: x <= 0; Time = 24:00 + x
    e.g.:
        12:30 = 24:00 + (-11:30)
        0:00 = 24:00 - 24:00
        !-x being displayed!

## Algorithm in Pseudocode

t = current time
x_hour = -23 + t: currentHour, x_min = -59 + t: currentMinure, x_sec = -59 + t: currentSecond

while True (while loop, runs forever):
    print x_hour, ":", x_min, ":", x_sec

        if x_sec <= 0
            x_sec += 1

        if x_sec == 1 and x_min == 1
            x_sec = -59
            x_min += 1
        elif x_sec == 1
            x_sec = -59
            x_min += 1

        if x_min == 1
            x_sec = -59
            x_min = -59
            x_hour += 1

        if x_hour == 1
            x_hour = -23
            x_min = -59

        wait one second (sleep)
