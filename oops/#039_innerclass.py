class Outer:	
	def __init__(self):
		print("Outer class constructor")
		
	def m2(self):
			print("Outer class method m2()")
		
	class Inner:	
		def __init__(self):
			print("Inner class constructor")			
			
		def m1(self):
			print("Inner class method m1()")
			
i = Outer().Inner()
i.m2()



