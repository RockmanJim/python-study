class Tool(object):
	#类属性
	num = 0
	
	#实例方法
	def __init__(self, new_name):
		self.name = new_name
		Tool.num += 1
		
	#类方法
	@classmethod
	def add_num(cls):
		cls.num += 20
	
	#静态方法
	@staticmethod 
	def print_hello():
		print("hello")
		print("num - 1 = %d"%(Tool.num - 1))
		Tool.num -= 1

#类方法可以直接用
Tool.add_num()
print(Tool.num)
#静态方法也可以直接用
Tool.print_hello()
print(Tool.num)
#也可以通过实例去调用
t = Tool(66)
t.add_num()
t.print_hello()
print(t.num)
