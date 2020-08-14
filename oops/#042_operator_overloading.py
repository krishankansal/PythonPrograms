class A: 
    def __init__(self, a): 
        self.a = a 
  
    # adding two objects  
    # magic method
    def __add__(self, x): 
        return self.a + x.a  
    
    def __sub__(self, x):
        return self.a - x.a
    
    def __mul__(self, x):
        return self.a * x.a
    
    def __truediv__(self, x):
        return self.a / x.a
    
    def __floordiv__(self, x):
        return self.a // x.a
    
    def __mod__(self, x):
        return self.a % x.a
    
    def __pow__(self, x):
        return self.a ** x.a
    
    def __str__(self):
        return str(self.a)

ob1 = A(30) 
ob2 = A(20) 
  
print('Addition =' , ob1 + ob2) 
print('Subtraction =' , ob1 - ob2) 
print('Multiplicaton =' , ob1 * ob2) 
print('Division =' , ob1 / ob2) 
print('Floor Div =' , ob1 // ob2) 
print('Modulus =' , ob1 % ob2) 
print('Power =' , ob1 ** ob2) 
print('ob1 = ', ob1)
print('ob2 = ', ob2)

ob3 = A("Swami ") 
ob4 = A("Vivekanand") 
print('String Addition =', end=' ')
print(ob3 + ob4) 



#print(ob3 - ob4) 

# We can't do this
'''Error Message
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
#print(ob1 + ob4)

