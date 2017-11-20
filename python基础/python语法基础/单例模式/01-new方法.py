import sys

class Dog(object):
	def __init__(self):
		print("init会在new之后")
		
	def __new__(cls):
		print("这是自定义的new")
		obj = object.__new__(cls)#这是用object类的方法去生成对象
		print("id：%s 引用个数：%d"%(id(obj), sys.getrefcount(obj)))#只是自己想看下id和引用的
		return obj
		
	def __del__(self):
		print("del啦！")
		
d = Dog()
print("id：%s 引用个数：%d"%(id(d), sys.getrefcount(d)))#只是自己想看下id和引用的，看起来没有变化，都是2
#new是java、C++里没有的，new和init（初始化）合并起来才相当于构造方法
