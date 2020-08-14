class Demo:
    ' use of class method'

    count = 0 

    def __init__(self):
        Demo.count = Demo.count + 1

    @classmethod
    def getNumObjects(cls):
        print('The number of objects = ',cls.count)

for i in range(10):
    Demo()

Demo.getNumObjects()

    

