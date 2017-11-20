import sys

class T:
	pass
	
print("因为调用sys.getrefcount(t)时，该方法就得找个变量来接受t这个参数，所以会导致引用计数多1的情况")
t = T()
print("t = T()后，T()的引用计数为：%d"%(sys.getrefcount(t)))
tt = t
print("tt=t后，T()的引用计数为：%d"%(sys.getrefcount(t)))
del tt
print("del tt后，T()的引用计数为：%d"%(sys.getrefcount(t)))
