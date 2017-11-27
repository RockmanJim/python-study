try:
	open("xxx.txt")
	print(num)
	print("1~~~")

except FileNotFoundError:
	print("get FileNotFoundError")
except NameError:
	print("get NameError")
#按顺序捕获异常

print("2~~~")
