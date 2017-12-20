my_set = {1,3,5}
my_dict = {'name': "Jon", 'age': 22, 'grades': [1,3,4]}

lottery_players = [
    {
    "name": "Rolf",
    "age": 20
    },
    {"name": "Dim",
    "age": 100}
]

print(sum(my_dict["grades"]))

##

students = [
    {"name": "Jose", "school": "Computing", "grades": (1,2,3)},
    {"name": "Dmi", "school": "Computing", "grades": (1,1,1)},
    {"name": "Jon", "school": "Computing", "grades": (3,2,4)},
    {"name": "Anna", "school": "Computing", "grades": (4,5,4)}
]

def average_grade(data):
    grades = data["grades"]  # Change this!
    return sum(grades) / len(grades)


def ask_user():
    a = {"name": "Jose", "school": "Computing", "grades": (1,2,3)}
    print(len(students))
    print(average_grade(a))

ask_user()