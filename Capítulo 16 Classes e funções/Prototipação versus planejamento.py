class Time:
    'tempo'

def time_to_int(time):
    minutes = time.hour*60 + time.minute
    seconds = minutes*60 + time.seconds
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increment(t1, seconds):
    seconds += time_to_int(t1)
    return int_to_time(seconds)
