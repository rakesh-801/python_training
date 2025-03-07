D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
# union of keys, #value does not matter
#D_UNION = { 'ok': 1, 'nok': 2 , 'new':3  } 
# intersection of keys, #value does not matter
#D_INTERSECTION = {'ok': 1}
#D1- D2 = {'nok': 2 }
#values are added for same keys
#D_MERGE = { 'ok': 3, 'nok': 2 , 'new':3}

D_UNION = {**D1,**D2}
print(f"The union of the D1 and D2 is {D_UNION}")


dict1 = {}
for k in D1:
    if k in D2:
        dict1[k]=D1[k]
print(f"The Intersection of the {dict1}")


dict2 = {}
for k in D1:
    if k not in D2:
        dict2[k] = D1[k]
print(f" The difference between the D1 and D2 {dict2}")


dict3 = {}
for k in D1:
    if k in D2:
        dict3[k] = D1[k]+D2[k]
    else:
        dict3[k]=D1[k]
for k in D2:
    if k not in dict3:
        dict3[k] = D2[k]       
print(f"The merge data of the D1 and D2 {dict3}")        







