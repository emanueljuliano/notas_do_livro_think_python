class Time:
    """Represents the time of day.
    attributes: houe, minute, second"""

time = Time()
time.hour = 1
time.minute = 59
time.second = 30

atual = Time()
atual.hour = 23
atual.minute = 14
atual.second = 50

print('{:02}:{:02}:{:02}'.format(time.hour, time.minute, time.second))

def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

print(is_after(time, time))
