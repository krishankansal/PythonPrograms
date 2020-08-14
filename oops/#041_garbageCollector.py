import time
class Test:
	def __init__(self):
		print('Object initialization...')	
		
	def __del__(self):
		print('Performing cleanup.....')
		
t = Test()
t = None
time.sleep(3)
print('End of application')
	
