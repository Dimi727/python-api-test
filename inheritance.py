class People:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []


    def average(self):
        return sum(self.marks)/len(self.marks)
    
    @classmethod
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)

##

class WorkingStudent(People):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


anna = WorkingStudent("Anna", "Oxford", 22.00)
print(anna.salary)

friend = WorkingStudent.friend(anna, "Greg", 31.00)
friend2 = People.friend(anna, "Tom")
print(friend.name, friend.school)
print(friend.salary)
print(friend2.name, friend2.school)
