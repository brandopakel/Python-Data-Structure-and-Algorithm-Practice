def return_inter(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

list1 = [2,43,48,62,64,28,3]
list2 = [1,28,42,70,2,10,62,31,4,14]
new_list = return_inter(list1,list2)
print(new_list)