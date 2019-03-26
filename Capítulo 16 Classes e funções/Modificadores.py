class Time:
    'tempo'

hora = Time()
hora.hour = 00
hora.minute = 59
hora.second = 50

def print_time(time):
    print(f'{time.hour:02}:{time.minute:02}:{time.second:02}')

def increment(time, seconds):
    tempo = Time()
    tempo.hour = time.hour
    tempo.minute = time.minute
    tempo.second = time.second

    tempo.second += seconds
    if tempo.second >= 60:
        tempo.minute += tempo.second // 60
        tempo.second = tempo.second % 60

    if tempo.minute >= 60:
        tempo.hour += tempo.minute // 60
        tempo.minute = tempo.minute % 60

    return tempo

print_time(increment(hora, 100))
