import time

seg_tot = time.time() #tempo decorrido desde que a época ocorreu

min_tot = seg_tot // 60
hr_tot = min_tot // 60
dias = int(hr_tot // 24)
horas = int((hr_tot / 24 - dias)*24)
min = int((min_tot / 60 - hr_tot)*60)
seg = int((seg_tot / 60 - min_tot)*60)
print(f'Já se passaram {dias} dias, {horas} horas, {min} e {seg} segundos ')