class Time:
    'tempo'

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

#modos de usar

def add_time(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        return ValueError('invalid Time object in add_time')

    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

#ou

def add_time2(t1, t2):
    assert valid_time(t1) and valid_time(t2) #assert verifica determinados requisitos e cria uma exceção
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
