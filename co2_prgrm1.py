num=int(input("enter a number:"))
factorial=1
if num<0:
    print("factorial does not exist")
elif num==0:
    print("factorial of 0 is 1")
else:
    for x in range(1,num+1):
        factorial=factorial*x
    print("factorial of",num,"is",factorial)