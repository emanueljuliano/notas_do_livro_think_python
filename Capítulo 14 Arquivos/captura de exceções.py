#fin = open('bad_file') -> erro arquivo não existe
#fout = open('\etc\passwd', 'w') -> erro não possui permissão para acessar
#cake = open('C:\\Users\\emanu\\OneDrive\\Documentos\\mangas') -> não é possível ler um diretório

try:
    fin = open('bad_file')
except:
    print('Something went wrong')

fin.close()