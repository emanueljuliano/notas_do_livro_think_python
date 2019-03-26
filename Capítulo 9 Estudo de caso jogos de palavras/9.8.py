for i in range(999999):
    string = str(i).zfill(6)
    if string[-4:] == string[-4:][::-1]:
        string = str(i+1).zfill(6)
        if string[-5:] == string[-5:][::-1]:
            string = str(i+2).zfill(6)
            if string[-5:-1] == string[-5:-1][::-1]:
                string = str(i+3)
                if string == string[::-1]:
                    print(i)
