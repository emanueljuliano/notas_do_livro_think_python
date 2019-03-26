import os

def search_mp3(directory):
    t = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename[-4:] == '.mp3':
                t.append(os.path.join(root, filename))
    return t


def main():
    directory = 'C:\\Users\\emanu\\Music'
    files = search_mp3(directory)
    for line in files:
        print(line)

if __name__ == '__main__':
    main()