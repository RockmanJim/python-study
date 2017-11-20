class Base(object):
	#object是所有类的父类，不写也实际继承了它
	#写了(object)的就是新式类，不写就是经典类（要过时的写法），新式类比经典类多些功能，推荐新式类
	def test(self):
		print("Base")
	
class A(Base):
	def test1(self):
		print("A test1")
		
class B(Base):
	def test2(self):
		print("B test2")
		
class C(A, B):
	#C类就继承了A和B类
	pass
	
c = C()
c.test1()
c.test2()
c.test()
