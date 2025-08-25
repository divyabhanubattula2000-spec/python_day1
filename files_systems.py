with open('training_notes.txt','a+') as fo:
    fo.write('Hi python\n bye python')
    fo.seek(0)
    x=fo.readlines()
    print(x)

