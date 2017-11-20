class A:
	def __init__(self):
		print("A init")
		self.num1 = 100
		self.__num2 = 200
		
	def __del__(self):
		print("A del")
		
	def _test0(self):
		print("A _test0")
	
	def test1(self):
		print("A test1")
	
	def __test2(self):
		print("A __test2")
		
	def test3(self):
		print("A test3")
		self.__test2()
		print(self.__num2)
		
class B(A):
	#def __init__(self):
	#	print("B init")
	#	#super().__init__()
		
	def __del__(self):
		print("B del")

	def test4(self):
		self.test3()
		print("B test4")
	
	def test5(self):
		print("B test5")
		self._test0()
		
#a = A()
b = B()

#print(b.num1)#有了super().__init__()才会有b.num1
print("b.test3()执行中")
b.test3()
print("b.test4()执行中")
b.test4()
print("b.test5()执行中")
b.test5()
#print(dir(a))
#print(dir(b))
#print(a.__dir__())
#print(b.__dir__())

#B 不会继承A的私有方法

#似乎重写就是彻底重写，不会在其中再执行父类的方法