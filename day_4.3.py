print("Hi")

try:
    x=int(input("Enter a number:"))
    y=int(input("Enter another number:"))
    result=x/y
    print(result)
except ValueError:
    print("both values should be int type")
except ZeroDivisionError:
    print('cant give zero')
except :
    print('something went wrong')
print('Bye')