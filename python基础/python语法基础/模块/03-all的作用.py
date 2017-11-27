# 这里赋值之后，就能限定该模块被import时，会被引入的内容了
#__all__ = ["test1", "Test"]


def test1():
	print("test1")
	
def test2():
	print("test2")
	
num = 10

class Test(object):
	pass
