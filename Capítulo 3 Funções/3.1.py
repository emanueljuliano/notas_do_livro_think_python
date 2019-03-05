#Right_justify -> última letra da string na coluna 70 da tela

def right_justify(palavra):
    num_de_espaços = 70
    espaços_antes = num_de_espaços - len(palavra)
    resultado = ' ' * espaços_antes + palavra
    print(resultado)
    print(len(resultado))

right_justify('Monty')
