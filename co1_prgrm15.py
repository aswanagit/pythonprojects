col1=['red','blue','yellow']
col2=['green','blue']

for i in col1:
    for j in col2:
        if i==j:
            col1.remove(i)
print("the colours not in col2 are:",col1)