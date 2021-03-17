
list1=[1,2,3,4,5]
list2=[2,4,6,8]
print("elements in list one is",list1)
print("elemants in list two is",list2)
s1=0
s2=0
if(len(list1)==len(list2)):
 print("list have same length")
else:
 print("list have diff length")
for i in range(len(list1)):
  s1=s1+list1[i]
print("the sum of first list is",s1)
for i in range(len(list2)):
  s2=s2+list2[i]
print("the sum of list2 is",s2)
if(s1==s2):
  print("sum of lisys are same")
else:
 print ("the sum of list are different")
for i in list1:
  for j in list2:
    if i==j:
     print("the commen element are",i)