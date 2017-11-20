class Animal:
	def eat(self):
		print("eat~")
	
	def sleep(self):
		print("sleep")
		
class Cat(Animal):
	def catch(self):
		print("catch mouse")
		
class Dog(Animal):
	def swim(self):
		print("swim")
		
tom = Cat()
tom.eat()
tom.catch()

snoopy = Dog()
snoopy.sleep()
snoopy.swim()
