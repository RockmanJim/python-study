class Employee:
	'''
	this is a test deme class
	'''
	classSpec="it is a test class"
	def __init__(self, name, pay):
		self.name=name
		self.pay=pay
		
	def hello(self):
		print self.name
		print "hello"