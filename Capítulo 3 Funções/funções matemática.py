import math

intensidade_do_barulho = 10 **(-12)
intensidade_sonora = 10**(-3)
fracao = intensidade_sonora / intensidade_do_barulho
decibeis = 10 * math.log10(fracao)
radianos = 0.7
altura = math.sin(radianos)

print(decibeis)
print(altura)

graus = 45
radianos2 = graus / 180 * math.pi
print (math.cos(radianos2))
