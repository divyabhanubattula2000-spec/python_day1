import re

with open('D:\python_t\search_text.txt', 'r') as fo:
    for i in fo:
        #if re.search(r'python', i):
        #if re.search(pattern[])
        if re.search('[a-zA-Z]',i):
                    print(i,end='')

                    

