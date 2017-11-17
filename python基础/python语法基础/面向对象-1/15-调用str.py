class Cat:
	"""
	定义了一个Cat类
	"""
	#初始化对象（构造方法？）
	def __init__(self, new_name, new_age):
		self.name = new_name
		self.age = new_age
	
	def __str__(self):
		return "%s的年龄是%d"%(self.name, self.age)
	
	#方法
	def eat(self):
		print("The cat is eating")
	
	def drink(self):
		print("The cat is drinking")
		
	def intro(self):
		print("%s的年龄是%d"%(self.name, self.age))
#创建对象
tom = Cat("Tom", 10)
garfield = Cat("Garfield", 20)
#输出一下
print(tom)
print(garfield)
