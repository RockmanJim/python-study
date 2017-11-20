class Animal:
	def eat(self):
		print("eat~")
	
	def sleep(self):
		print("sleep")
		
class Dog(Animal):
	def swim(self):
		print("swim")
		
class Xiaotq(Dog):
	def swim(self):
		print("swimswimswim")
	
	def sleep(self):
		print("huhuhu")
		#调用被重写的父类的方法
		#第一种方式
		#Dog.sleep(self)
		#第二种方式
		super().sleep()
		
x = Xiaotq()
x.swim()
x.sleep()
