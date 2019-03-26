fout = open('output.txt', 'w') #se o arquivo já existir, seus dados são apagados e outro é criado

line1 = "This here's the wattle,\n"
fout.write(line1) #escreve e retorna o número de caracteres
line2 = "the emblem of our land. \n"
fout.write(line2)
fout.close()
#argumento de write precisa ser str

