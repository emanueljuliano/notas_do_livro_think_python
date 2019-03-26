import os # trabalha com diretórios
cwd = os.getcwd()
print(cwd)
print(os.path.relpath('output.txt')) # -> caminho relativo
print(os.path.abspath('output.txt')) # -> caminho absoluto

print(os.path.exists('memo.txt'))
print(os.path.isdir('output.txt'))
print(os.path.isdir('C:\\Users\\emanu\\PycharmProjects\\python\\Capítulo 14 Arquivos'))
#os.path.isfile verifica se é arquivo
print(os.listdir(cwd)) #retorna uma lista doq está no diretório

def walk(dirname):
    #passeia por um diretório, exibe os nomes dos arquivos e chama a si mesmo em todos os diretórios
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name) #join une um nome de uma arquivo a um diretório
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

#walk('C:\\Users\\emanu\\OneDrive\\Documentos\\mangas')
def walk2(dirname):
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))

walk2(':\\Users\\emanu\\OneDrive\\Documentos\\mangas')
