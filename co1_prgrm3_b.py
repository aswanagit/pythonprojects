#)3
n=int(input("enter the number of numbers:"))
list=[]
for i in range(n):
    x=int(input("enter the numbers:"))
    list.append(x)
print(list)
list2=[x**2 for x in list]
print(list2)