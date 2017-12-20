# class lotteryPlayer:
#     def __init__(self, name):
#         self.name = name
#         self.numbers = (5,6,7,8,49)

#     def total(self):
#         return sum(self.numbers)


# player = lotteryPlayer("John")
# player2 = lotteryPlayer("John")

# print(player.name)
# print(player.numbers)
# print(player.total())
# print(player.name == player2.name)

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        return sum(self.marks)/len(self.marks)

    # def add_marks(self, name, price):
    #     dictionary = {"name": name, "price": price}
    #     self.marks.append(dictionary["price"])

    # def go_to_school(self):
    #     print("lets go to {} university!".format(self.school))
    
    # @classmethod
    # def go_to_school(cls):
    #     print("lets go to university!")
    #     print("wo sind wir {}".format(cls))
        

    @staticmethod
    def go_to_school():
        print("some stuff")

Anna = Student("Anna", "MIT")
jens = Student("Jens", "oxford")
Anna.marks.append(100)
Anna.marks.append(155)
# # Anna.add_marks("test", 200)
# print(Anna)
# print(Anna.marks , Anna.school)
# print(Anna.avg())
# print(sum(Anna.marks))
print(jens.go_to_school())
print(Student.go_to_school)