n=int(input("enter the limit:"))
list=[]

for i in range(n):
    x=int(input("enter the numbers:"))
    list.append(x)
print(list)
list2=[]
for i in list:
    if i%2!=0:
        list2.append(i)
print(list2)