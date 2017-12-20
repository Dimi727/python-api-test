# test = True

# if test:
#     print("test")

# test_list = ["dimi","aba"]

# number = input("nenn mir eine Zahl")

# if number in test_list:
#     print("yo {}!".format(number))

# else:
#     print("falsch gedacht, {}".format(number))



def who_do_you_know():
    people = input("Gib mir namen yo: ")
    people_list = people.split(",")
    people_ws=[x.strip() for x in people.split()]
    print(people_ws)
    return people_ws


def ask_user():
    person = input("tell me a name! ")
    people = who_do_you_know()
    if person in people:
         print("YOu know {}!!!!".format(person))

ask_user()