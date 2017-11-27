__all__ = ["sendmsg"]
# 告诉调用者，import了这个文件夹的后，可以再import的文件有哪些。即文件夹和其下文件关联上。

# import sendmsg
# 这个是python2可用的方法，但在Python3下会报错

from . import sendmsg
# 这个是python3可用的方法，意思是在当前目录下（.就是当前目录），载入sendmsg