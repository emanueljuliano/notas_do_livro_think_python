#volume da esfera de raio 5
raio = 5
volume = 4/3 * 3.141592 * raio ** 3
print(volume)

#custo de atacado para 60 cópias de um livro
exemplar = 60
preço = 24.95
desconto = 0.4
transporte = 3 + 0.75 * (exemplar - 1)

custo_total = exemplar * preço * (1 - desconto) + transporte

print(custo_total)

#horário de chegar em casa
inicio = 6*60 + 52 #horário em minutos
corrida1 = 1 * (8 + 15/60)
corrida2 = 3 * (7 + 12/60)
corrida3 = corrida1
horario_min = (inicio + corrida1 + corrida2 + corrida3)

hora = horario_min // 60
minuto = (horario_min - hora*60) // 1
segundo = (horario_min - (minuto + hora*60)) * 60

print(hora, 'horas,', minuto, 'minutos e', segundo, 'segundos')
