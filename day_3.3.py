"""
print('hi')
x=int(input('enter a number:'))
y=int(input('enter a number:'))
def f1():
    print("this is my function for addition")
    print("addition of {x} and {y}=",x+y)
f1()
print("Bye")
f1()


def calc(x,y):
    print('addition',x+y)
    print ('diff',x-y)
    print ('mul',x*y)
    print ('div',x/y)
    print('percentage',x%y)
    print('end')
calc(50,70)
calc(6,7)

x=10
def calc(x,y):
    print('addition',x+y)
    print('end')
calc(10,40)



def f1(x,y):
    return(x+y)
k=f1(30,40)
print(k)
print(f1(11,19))
f1(4,5)


def intro(name,city,job):
    print(f'my name is {name}, I am from {city} , and my job is {job})
intro(name="divya",city="guntur",job="dw")
#intro(name='xyz',city='gyh',job='SAP')




def f1(x,y,op='+'):
    if op=='+':
        print(x+y)
    elif op=='-':
        print(x-y)
    k=f1(10,20,'+')
    print (k)


def intro(**kwargs):
    for key ,value in kwargs.items():
        print(f'{key}: {value}')
intro(name='rama',city='hgu',job='yuu')



def intro(**kwargs):
    for key,value in kwargs.item():
        print(f'{key}: {value}')
intro(name='rama',city='hgu',job='yuu')


def f1(a,b,*c,**d):
    print(a)
    print(b)
    print(c)
    print(d)
f1(1,2,3,4,5,name='divya',city='hyd')
"""
import divya.divya_sub.mult as mult
