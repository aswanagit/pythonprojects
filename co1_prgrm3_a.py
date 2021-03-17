#)3
n=int(input("enter the number of numbers:"))
list=[]
for i in range(n):
    x=int(input("enter the numbers:"))
    list.append(x)
print(list)
b=[x for x in list if x>0]
print(b)