n=int(input("enter the number of numbers:"))
list=[]
for i in range(n):
 x=int(input("enter the number:"))
 if x<100:
  list.append(x)
 else:
  list.append("over")
print(list)