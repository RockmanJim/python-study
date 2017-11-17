class House:
	def __init__(self, new_addr, new_area):
		self.addr = new_addr
		self.area = new_area
		self.contain = []
		
	def __str__(self):
		return "地址：%s 面积：%d 包含的物品：%s"%(self.addr, self.area, str(self.contain))
		
	def add_item(self, item):
		self.contain.append(item.get_name())
		self.area -= item.get_area()
		
class Item:
	def __init__(self, new_name, new_area):
		self.name = new_name
		self.area = new_area
		
	def __str__(self):
		return "物品名：%s 占地面积：%s"%(self.name, self.area)
		
	def get_name(self):
		return self.name
		
	def get_area(self):
		return self.area
		
h = House("中南海", 200)
print(h)
i1 = Item("烤箱", 2)
print(i1)
i2 = Item("冰箱", 2)
print(i2)

h.add_item(i1)
print(h)
h.add_item(i2)
print(h)