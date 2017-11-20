class Dog:
	def set_age(self, new_age):
		if new_age > 0 and new_age < 100:
			self.age = new_age
		else:
			self.age = 0
			print("Plz input true age~")
			
	def get_age(self):
		return self.age
		
d = Dog()
d.set_age(-2)
print(d.get_age())

d.set_age(4)
print(d.get_age())
