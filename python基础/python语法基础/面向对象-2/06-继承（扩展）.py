class Animal:
	def eat(self):
		print("eat~")
	
	def sleep(self):
		print("sleep")
		
class Dog(Animal):
	def swim(self):
		print("swim")
		
class Xiaotq(Dog):
	def fly(self):
		print("fly")
		
x = Xiaotq()
x.fly()
x.swim()
x.eat()
