class Test:

    'static varibale in class'
    x = 10

    def __init__(self, y,z):
        'static variable in constructor'
        Test.y = y
        self.z = z

    def meth(self):
        'static variable in instance method'
        Test.i = 60

    @classmethod
    def meth2(cls):
        'two static variables in class method'
        cls.j = 70
        Test.k = 80

    @staticmethod
    def meth3():
        'static variable in static method'
        Test.a = 80

'static variable outside the class'
Test.g = 100

test1 = Test(20,30)
test2 = Test(45,55)

'10 45 30'
print(test1.x,test1.y,test1.z)
'10 45 55'
print(test2.x,test2.y,test2.z)

print(Test.__dict__)