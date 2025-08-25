fo=None
try:
    fo=open(r"D:\python_t\training_notes.txt")
    for i in fo:
        print(i)
except Exception as e:
    print(e)
finally:
    print('opened and wrote the file')
    if fo!=None:
        fo.close()

