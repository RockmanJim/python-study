import os
#获取文件夹路径
folder_path = input("Plz input your folder_path:\n")
#获取该文件夹下所有文件名
file_names = os.listdir(folder_path)
#通过基于完整路径执行
for name in file_names:
	new_file_name = name[name.rfind("[change]") + len("[change]"):]
	os.rename(folder_path + "/" + name, folder_path + "/" + new_file_name)
	print(new_file_name)
