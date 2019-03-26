def sed(s1, s2, filename1, filename2):
    try:
        finn = open(filename1, 'r') #opens a file for reading
        jake = open(filename2, 'w') #open a file for writing
        for line in finn:
            line = line.replace(s1, s2)
            jake.write(line)
    except:
        print('Algo deu errado')

if __name__ == '__main__':
    sed('wattle', 'agua', 'output.txt', '14.1_hidratado.txt')