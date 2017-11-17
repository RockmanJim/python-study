class SweetPotato:
	def __init__(self):
		self.cookedString = "生的"
		self.cookedLevel = 0
		self.condiments = []
		
	def __str__(self):
		return "地瓜的状态：%s	已经烤的时间：%d	添加的作料：%s"%(self.cookedString, self.cookedLevel, str(self.condiments))
		
	def cook(self, cooked_time):
		self.cookedLevel += cooked_time
		if self.cookedLevel < 3:
			self.cookedString = "生的"
		elif self.cookedLevel >=3 and self.cookedLevel < 5:
			self.cookedString = "半生不熟"
		elif self.cookedLevel >=5 and self.cookedLevel < 8:
			self.cookedString = "熟了"
		elif self.cookedLevel >=8:
			self.cookedString = "糊了"
			
	def addConidments(self, item):
		self.condiments.append(item)
		
#创建一个地瓜对象
di_gua = SweetPotato()
print(di_gua)

#开始烤地瓜
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addConidments("芥末")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addConidments("辣椒")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addConidments("盐")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
