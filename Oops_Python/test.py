def repeat(list1):
    result = ''
    dict1=dict()
    for i in list1:
         count =0
         for j in list1:
             if i == j :
                 count +=1
                 dict1.update({i:count})
    c = max(dict1.values())
    for keys, values in dict1.items():
        if c == values:
            result = keys
            break

    return result
print(repeat(['Ram','Krishna','Ram','laxman']))
print(repeat(['Ram','Krishna','Krishna','laxman']))
print(repeat(['Krishna','Ram','Krishna','Ram']))
print(repeat(['Krishna','Ram','Krishna','Ram']))
print(repeat(['Ram','Ram','laxman','Ram','laxman']))
