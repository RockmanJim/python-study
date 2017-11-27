class Test(object):
	def __init__(self, switch):
		self.switch = switch
	
	def calc(self, a, b):
		try:
			return a / b
		except Exception as result:
			if self.switch:
				print("捕获开启，已经捕获到了异常，信息如下：")
				print(result)
			else:
				# 重写抛出这个异常，交由外层处理（外层没有处理就只能默认处理了）
				raise
				
a = Test(True)
a.calc(11, 0)

print("-" * 20)

a.switch(False)
a.calc(11, 0)