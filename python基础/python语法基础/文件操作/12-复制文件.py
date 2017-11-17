#1.获取要复制的原文件的文件地址
file_name = input("Plz input path of origin file:\n")
#2.打开该文件
file = open(file_name, "r")
#3.新文件文件名
place = file_name.rfind(".")
new_file_name = file_name[:place] + "[copy]" + file_name[place:]
#4.新建文件
new_file = open(new_file_name, "w")
#5.复制内容
new_file.write(file.read())
#6.关闭通道
new_file.close()
file.close()
