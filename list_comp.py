my_list = [1,2,3,4,0]

an_equal_list = [x + 2 for x in range(10)]

print(an_equal_list)

other_list = [x for x in range(100) if x % 3 == 0]

print(other_list)


people = ["dan", "dimi", "anna", "ANNNNNNAA"," FDFFF"]

norm_p = [person.lower().strip() for person in people]

print(norm_p)