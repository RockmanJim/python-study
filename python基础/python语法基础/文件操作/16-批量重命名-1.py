import os
#获取文件夹路径
folder_path = input("Plz input your folder_path:\n")
#获取该文件夹下所有文件名
file_names = os.listdir(folder_path)
#通过更改工作目录执行
#os.chdir(folder_path)
#for name in file_names:
#	os.rename(name, "[change]" + name)
#	print("[change]" + name)
#通过基于完整路径执行
for name in file_names:
	old_file_name = folder_path + "/" + name
	new_file_name = folder_path + "/" + "[change]" + name
	os.rename(old_file_name, new_file_name)
	print("[change]" + name)
