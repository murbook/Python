class Man:
	def __init__(self,name): #コンストラクタ
		self.name=name #インスタンス変数の作成
		print("Initialized!")
	def hello(self):
		print("Hello "+self.name+"!")
	def goodbye(self):
		print("Goodbye "+self.name+"!")

m=Man("David")
m.hello()
m.goodbye()
print(type(m))

#メソッドの第一引数に、selfと書かなきゃいけない！！