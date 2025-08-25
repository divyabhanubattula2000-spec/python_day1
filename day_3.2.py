import re
with open(r'D:\python_t\search_text.txt', 'r') as fo:
    for i in  fo:
        if re.search(r'\w+[@][a-z]+[.][a-z]+',i):
            print(i,end='')