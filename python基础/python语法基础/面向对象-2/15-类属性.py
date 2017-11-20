class Tool(object):
	#类属性
	num = 0
	
	#方法
	def __init__(self, new_name):
		self.name = new_name
		Tool.num += 1

s = "现在Tool里的num有：%d个"
t1 = Tool(44)
print(s%Tool.num)
t2 = Tool(55)
print(s%Tool.num)
t3 = Tool(66)
print(s%Tool.num)
