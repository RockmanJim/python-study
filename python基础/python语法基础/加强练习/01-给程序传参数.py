import sys

print(sys.argv) # 用sys.argv来接受传入的参数，这里就是让它显示一下。传入的内容，会按空格拆分成一个个对象，放入列表中。列表的第一位文件名。

name = sys.argv[1] # 获取第一个参数

print("热烈欢迎%s" % name) # 把传入的第一个参数输出
