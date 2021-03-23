n=int(input("enter the limit:"))
list=[]
for i in range(n):
    x=int(input("enter the numbers:"))
    list.append(x)
sum=0
for i in list:
    sum=sum+i
print(sum)