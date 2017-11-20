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
		
x = Xiaotq()
x.swim()
x.sleep()
