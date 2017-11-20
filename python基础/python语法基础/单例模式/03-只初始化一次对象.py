class Dog(object):
	__instance = None
	__init_flag = False#为了只初始化一次对象设置的flag
		
	def __new__(cls, name):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
		return cls.__instance
		
	def __init__(self, name):
		if Dog.__init_flag == False:
			self.name = name
			Dog.__init_flag = True
		
d1 = Dog("d1")
d2 = Dog("d2")
print(id(d1))
print(d1.name)
print(id(d2))
print(d2.name)
