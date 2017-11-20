class Dog(object):
	__instance = None#用这个私有变量存放单例的对象
		
	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)#cls.__instance？难道还有self.__instance？
		return cls.__instance
		
	def __del__(self):
		print("del啦！")
		
d1 = Dog()
d2 = Dog()
print(id(d1))
print(id(d2))
#print(dir(d1))
#print(d1.__dir__)