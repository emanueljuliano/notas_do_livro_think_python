from datetime import date
import datetime

def dia_da_semana(date = date.today()):
    dias = {0:'segunda', 1:'terça', 2:'quarta', 3:'quinta', 4:'sexta', 5:'sábado', 6:'domingo'}
    return (dias[date.weekday()])

def aniverssauro(anos, niver):
    today = datetime.datetime.today()
    diferenca = today - niver
    idade = anos + diferenca.days // 365
    print(idade, end=' Próximo niver daqui a: ')

    niver_atual = niver.replace(today.year)
    if niver_atual > today:
        print((niver_atual - today))
    else:
        print(niver_atual.replace(today.year + 1) - today)

def dia_duplo(idade1, birthday1, idade2, birthday2, n=2):
    today = datetime.datetime.today()
    vida1 = today - birthday1.replace(today.year-idade1)
    vida2 = today - birthday2.replace(today.year - idade2)
    x = abs(vida1 - vida2)
    y = x/(n-1)
    print(y, x + y)

print(dia_da_semana())
niver = datetime.datetime(2017, 6, 27)
niver2 = datetime.datetime(2018, 11, 19)
aniverssauro(15, niver)
print(niver.time())

dia_duplo(18, niver, 19, niver2, 5)
