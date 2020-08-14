class Test:
    
    def __init__(self):
        self.x = 10
    
    def m1(self):  
        self.y = 20       

    def m2(self):
        self.z = 30
        
        


t = Test()
t.a = 40
print(t.x)
t.m1()
print(t.y)
t.m2()
print(t.z)
print('---------t1------')
t1 = Test()
print(t1.x)


