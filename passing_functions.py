def methodception(another):
    return another()


def do_stuff():
    return 1+1

print(methodception(do_stuff))

print(methodception(lambda: 1+1))

my_list = [1,3,4,5]

#delete values

print(list(filter(lambda x: x!= 4, my_list))) #filter functions have to be wrapped with list if result has to be a list

#or:

def not_four(x):
    return x != 4

print(list(filter(not_four, my_list)))

#list comprehens ..but only in python, obove can be also used in javascript

print([x for x in my_list if x != 4])

