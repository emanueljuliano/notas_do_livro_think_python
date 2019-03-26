class Time:
    'tempo'

def time_to_int(time):
    minutes = time.hour*60 + time.minute
    seconds = minutes*60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def mul_time(time, n):
    seconds = time_to_int(time)
    mul_sec = seconds * n
    return int_to_time(mul_sec)

def tempos_por_milha(time, distance):
    return mul_time(time, 1.0/distance)


tempo = Time()
tempo.hour = 1
tempo.minute = 20
tempo.second = 30
print(tempos_por_milha(tempo, 4).minute)
