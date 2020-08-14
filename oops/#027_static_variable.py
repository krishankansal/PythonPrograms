class Student:
    "Static variable Demo"

    "cl_teacher is a static variable here"
    cl_teacher = 'Krishan Kansal'

    def __init__(self, name, roll_no):
        "name and roll_no are instance variables"
        self.name = name
        self.roll_no = roll_no

s1 = Student('Kavya', 123)
s2 = Student('manohar', 789)

print(s1.name,s1.roll_no,s1.cl_teacher)
print(s2.name,s2.roll_no,s2.cl_teacher)