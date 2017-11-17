class Cat:
	"""
	定义了一个Cat类
	"""
	#方法
	def eat(self):
		print("The cat is eating")
	
	def drink(self):
		print("The cat is drinking")
		
	def intro(self):
		print("%s的年龄是%d"%(self.name, self.age))
#创建一个对象
tom = Cat()
#调用tom指向对象中的方法
tom.eat()
tom.drink()
#给tom指向的对象添加2个属性
tom.name = "Tom"
tom.age = 40
#获取属性的第一种方式
#print("%s的年龄是%d"%(tom.name, tom.age))
#获取属性的第二种方式
tom.intro()

garfield = Cat()
garfield.name = "Garfield"
garfield.age = 20
garfield.intro()