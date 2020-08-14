class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        '''
        This is intance method, since we are using 
        instance variables
        '''
        print('Name : ', self.name)
        print('Your marks : ', self.marks)
    def grade(self):
        'Another instance method'
        if self.marks >= 60:
            print('A grade')
        elif self.marks >= 50:
            print('B grade')
        elif self.marks >= 35:
            print('C grade')
        else:
            print('You are failed')

n = int(input('Enter number of students : '))
for i in range(n):
    name = input('Enter student name : ')
    marks = int(input('Enter student marks'))
    s = Student(name,marks)
    s.display()
    s.grade()
    print('*'*20)


