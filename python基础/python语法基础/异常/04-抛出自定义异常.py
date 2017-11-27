class ShortInputException(Exception):
	"""自定义的异常类"""
	def __init__(self, length, atleast):
		#super().__init__()
		self.length = length
		self.atleast = atleast
		
def main():
	try:
		s = input("请输入 --> ")
		if len(s) < 3:
			# raise引发一个自定义的异常
			raise ShortInputException(len(s), 3)
	except ShortInputException as result: # result这个变量会在此获得刚刚raise出的那个Exception对象的引用
		print("ShortInputException：输入的长度是%d，长度至少应该是%d" % (result.length, result.atleast)) # 因为已经获得了异常的对象，所以也可以在此使用其属性
	else:
		print("没有异常发生")

main()
