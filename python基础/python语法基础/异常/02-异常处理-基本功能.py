try:
	"""
	1/0
	open("xxx.txt")
	print(num)
	print("1~~~")
	"""
except (NameError, FileNotFoundError):#p3要写成元组的形式，p2不用
	print("把 NameError，FileNotFoundError 这俩异常一期处理")
except Exception as ret:
	print("所有的异常都会在此被捕获")
	print(ret)
else:
	print("没遇到异常才会执行的")
finally:
	print("怎么都会执行的一段")
print("2~~~")



#ctrl+c其实也是个异常，会被捕获 KeyboardInterrupt