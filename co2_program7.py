s=input("enter a string:")
if(len(s)>2):
    if(s[-3:]=='ing'):
        s=s+'ly'
    else:
        s=s+'ing'
print(s)