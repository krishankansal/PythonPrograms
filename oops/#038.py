class Employee:

	def __init__(self, id, name, sal):
		self.id = id
		self.name = name
		self.sal = sal
		
	def display(self):
		print("Employee id : ", self.id)
		print("Employee Name : ", self.name)
		print("Employee Salary : ", self.sal)

class Test:

	def modify(emp):
		emp.sal = emp.sal + 10000
		emp.display()
		
e = Employee(21, "Ramesh Tomar", 45000)
Test.modify(e) 
