class Dog(object):
	def print_self(self):
		print("Hi Dog")

class Snoopy(Dog):
	def print_self(self):
		print("Hi Snoopy")
		
def intro(t):
	t.print_self()#主要就是这里，事先并不知道用的是哪个类的
	
d1 = Dog()
d2 = Snoopy()

intro(d1)
intro(d2)
