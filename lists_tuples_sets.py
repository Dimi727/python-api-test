g1 = 77
g2 = 88
g2 = 18

#but better:

ages = [1,2,3,4]
tuple_age = (1,2,3,4) #cant be appended => immutable
set_age = {1,2,3,4} #unique & unordered

set_age.add(6)
set_age.add(6)

set1 = {1,2,3,4}
set2 = {1,3}

print(set1.union(set2))
print(tuple_age)