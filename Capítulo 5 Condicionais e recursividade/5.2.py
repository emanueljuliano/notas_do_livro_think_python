#a**n + b**n == c**n

def check_Fernant(a, b, c, n):
    if a**n + b**n == c**n:
        print('Holly smokes, Fermant was wrong')
    else:
        print('No, that doesn´t work')

print('O último teorema de Fermat diz que não existem números inteiros a, b e c tais que a**n + b**n == c**n para '
      'quaisquer valores de n maiores que 2.\n Vamos ver se ele está certo?')
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
n = int(input('Digite o valor de n: '))
check_Fernant(a, b, c, n)
