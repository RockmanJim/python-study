class Base(object):
	def test(self):
		print("Base")
	
class A(Base):
	def test(self):
		print("A test1")
		
class B(Base):
	def test(self):
		print("B test2")
		
class C(A, B):
	#def test(self):
	#	print("C test3")
	pass
	
c = C()
#看看到底运行了哪个test方法？
c.test()
print(C.__mro__)
#C.__mro__决定了调用方法时的搜索类的顺序，如果某个类中找到了方法，就停住 顺序由C3算法决定