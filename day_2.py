
"""print("welocome day2")"""
"""
my_list =[10,100,50.88,"list",90]
print(my_list)
for i in my_list:
    print(i)
print("list is completed")

employee_list=['ram','sita','divya']
for x in employee_list:
    print(x)
print('list ended')

for i in range (10,20):
    print(i)
    


my_list=[10,100,"divya","pup"]
print(f"total length is:",len(my_list))
print(my_list[0])
print (my_list[-1])
print(id(my_list))

my_list=[10,100,"divya","pup"]
my_list.append(100)
print(my_list)

my_list=[10,100,"divya","pup"]
new=['java','c']
for i in new:
    my_list.append(i)
print(my_list)


my_list=[10,100,"divya","pup"]
my_list.extend(["dog"])
print(my_list)
print(id(my_list))
my_list.clear()
print(my_list)
print(id(my_list))
#del(my_list)
print(my_list)


my_list=[10,100,"divya","pup"]
print(my_list.index(100))
print(my_list.count(100))
#my_list.insert(__index:10,__index:100)
my_list.remove("divya")
print(my_list)
"""
"""
list=[10,20,50,40,30]
print(sorted(list))
print(list)

list2=["pup","divya","dog","apple"]
print(sorted(list2))
 """
"""
list1=[10,20,50,40,30]
list2=list1
print(list1)
print(list2)
list1.append(100)
print(list1)
print(list2)

list3=[10,20,50,40,30]
list4=list3.copy()
print(list3)
print(list4)
list3.append(100)
print(list3)
print(list4)
"""
"""
list5=[23,29,31]
list5.append([100,20])
print(list5)
print(list5[-1])
print(list5[-1][-1])

"""
"""
x=10
tuple=23,78,90
tuple1=(10,20,30)
print(tuple1)
print(type(tuple1))
print(type(tuple))
print(type(x))
print(tuple)

tuple=((20,90,80),["k","l","m"],100)
print(index(tuple[-1]))
"""

"""
k=(20,90,80)
j=(23,40,50)
print(k)
print(k[0])
#k[0]=100
l=k+j
print(k+j)
print(l)
print(sorted(l))

"""

"""
k={1:("ram","janaki"),2:("sita",0),3:("laxman","urmila")}
l=k.keys()
v=k.values()
print(v)
print(k)
print(1 in k)

for i in l:
    print(i)
print(l)

k[4]="raghav"
for l,v in k.items():
    print(k,"=>",v)
print(k)


emp={1:"bob",2:"ram",3:"siya"}
print(emp)
print(emp[3])

for i in emp:
    print(i,">=" ,emp[i])
"""
"""

x={10,10,20,20,35,55}
y={34,89,90,67,10}
print(x)
print(id(x))
for i in x:
    print(i)
x.add(100)
print(x)
print(id(x))
print(sorted(x))
print(x.intersection(y))
print(x.union(y))
#x.intersection_update(y)
print(x)
print(x.difference(y))
"""


"""
x=int(input("enter a num1:"))
Y=int(input("enter a num2:"))
print(f"sum of {x} and {Y} is {x+Y}")
print(f"sub of {x} and {Y} is {x-Y}")
print(f"mul of {x} and {Y} is {x*Y}")
print(f"div of {x} and {Y} is {x/Y}")
print(f"power of {x} and {Y} is {x**Y}")
print(f"mode of {x} and {Y} is {x%Y}")
print(f"floor of {x} and {Y} is {x//Y}")
print(x>Y)
print(x<Y)
print(x>Y or x<Y)
print(x>Y and x<Y)




x=int(input("enter a number:"))
if  x > 0:
    print(f"{x} is positive")
else:
    print(f"{x} is negative")
print("Bye")


x=int(input("enter a number:"))
if x%2==0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")
print("bye")



x=int(input("enter a number:"))
if x>10:
    print(f"x is greater than 10")
    if x>20:
        print(f"x is greater than 20")
    else :
        print(f"x is less than 20")
else:
    print(f"x is less than 10")
print("done")

"""
"""
x=int(input("enter a number:"))
if x>0:
    print(f"{x} is greater than 0")
elif x<0:
    print(f"{x} is less than 0")
else :
    print(f"{x} is zero")

print("done")
"""

