from sys import exception

print("Hi")

try:
    x=int(input("Enter a number:"))
    y=int(input("Enter another number:"))
    result=x/y
    print(result)
except exception as e:
    print(e)
print('Bye')
