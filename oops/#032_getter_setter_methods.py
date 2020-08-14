class Student:

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setMarks(self, marks):
        self.marks = marks
    def getMarks(self):
        return self.marks

    def display(self):
        '''
        This is intance method, since we are using 
        instance variables
        '''
        print('Name : ', self.getName())
        print('Your marks : ', self.getMarks())

    def grade(self):
        'Another instance method'
        if self.getMarks() >= 60:
            print('A grade')
        elif self.getMarks() >= 50:
            print('B grade')
        elif self.getMarks() >= 35:
            print('C grade')
        else:
            print('You are failed')

n = int(input('Enter number of students : '))
for i in range(n):
    name = input('Enter student name : ')
    marks = int(input('Enter student marks'))
    s = Student()
    s.setName(name)
    s.setMarks(marks)
    s.display()
    s.grade()
    print('*'*20)


