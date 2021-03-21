def merge(dict1,dict2):
    return(dict1.update(dict2))
dict1={"a":4,"b":6}
dict2={"c":6,"d":7,"e":9}
print(merge(dict1,dict2))
print(dict1)