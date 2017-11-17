class Cat:
	"""
	定义了一个Cat类
	"""
	#初始化对象（构造方法？）
	def __init__(self, new_name, new_age):
		print("Cat is coming!")
		self.name = new_name
		self.age = new_age
	
	#方法
	def eat(self):
		print("The cat is eating")
	
	def drink(self):
		print("The cat is drinking")
		
	def intro(self):
		print("%s的年龄是%d"%(self.name, self.age))
#创建对象
tom = Cat("Tom", 10)
tom.intro()

garfield = Cat("Garfield", 20)
garfield.intro()