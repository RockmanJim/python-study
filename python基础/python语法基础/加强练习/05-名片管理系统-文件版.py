# 用来存储名片
card_infos = []

def print_menu():
	"""完成打印功能菜单"""
	print("=" * 50)
	print("名片管理系统")
	print("1、添加一个新的名片")
	print("2、删除一个名片")
	print("3、修改一个名片")
	print("4、查询一个名片")
	print("5、显示所有的名片")
	print("6、保存名片")
	print("7、退出系统")
	print("=" * 50)
	
def add_new_card_info():
	"""完成添加一个新的名片"""
	new_name = input("请输入名字：")
	new_qq = input("请输入QQ：")
	new_wx = input("请输入微信：")
	new_addr = input("请输入地址：")
	
	# 定义一个新的字典，用来存储一个新的名片
	new_infor = {}
	new_infor['name'] = new_name
	new_infor['qq'] = new_qq
	new_infor['wx'] = new_wx
	new_infor['addr'] = new_addr
	
	# 将一个字典，添加到列表中
	global card_infos
	card_infos.append(new_infor)
	
def find_card_infor():
	"""用来查询一个名片"""
	global card_infos
	find_name = input("请输入要查询的名字：")
	find_flag = False # 默认未找到
	for temp in card_infos:
		if find_name == temp['name']:
			print("%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['wx'], temp['addr']))
			find_flag = True # 表示找到了
			break
			
	# 判断是否找到了
	if find_flag:
		print("查无此人……")
		
		
def show_all_infor():
	"""显示所有名片信息"""
	global card_infos
	print("姓名\tQQ\t微信\t地址")
	for temp in card_infos:
		print("%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['wx'], temp['addr']))
		

def save_2_file():
	"""把已经添加的信息保存到文件中"""
	f = open("backup.data", "w")
	f.write(str(card_infos))
	f.close()
	
	
def load_infor():
	"""在开启时载入先前的数据"""
	global card_infos
	try:
		f = open("backup.data")
		card_infos = eval(f.read())
		f.close()
	except Exception:
		pass

def main():
	"""对整个程序的控制函数"""
	# 0、加载之前的数据到程序中
	load_infor()
	
	# 1、打印功能显示
	print_menu()
	
	while True:
		# 2、获取用户的输入
		num = int(input("请输入操作序号："))
		
		# 3、根据用户的数据执行相应的功能
		if num == 1:
			add_new_card_info()
		elif num == 2:
			pass
		elif num == 3:
			pass
		elif num == 4:
			find_card_infor()
		elif num == 5:
			show_all_infor()
		elif num == 6:
			save_2_file()
		elif num == 7:
			break
		else:
			print("输入有误，请重新输入")
			
		print()
		

if __name__ == '__main__':
	# 调用主函数
	main()