class Hero:
	def __del__(self):
		print("Ah~~~~~")

h1 = Hero()
h2 = h1
del h1#此时不会调用__del__，因为这个Hero()对象还有其他的变量（h2）指向它，即引用计数不是0
#del h2 #若此处删除h2，__del__便在此刻执行，因为没有变量指向它了，引用计数变成了0
print("=" * 5)
#如果程序结束时，有些对象仍存在，那么PYTHON解释器会自动调用他们的__del__方法来完成清理工作