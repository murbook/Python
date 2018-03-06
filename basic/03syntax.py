# ## 制御構文
# ### if文
list1 = ['A','B','C','D','E']
if 'A' in list1:
    print("a")
elif 'G' in list1:
    print("b")
else:
    print("c")
# タブが必要
print("\n")

# ### for文
for i in list1:
    print(i, end="")
print("")
for i in range(1,11): #1-10
    print(i, end="")
for i in range(5): #0-4
    print(i, end="")
print("")

# break=for文から抜ける
for i in range(5):
    if i == 3:
        break
    print(i, end="")
print("")
# continue=for文の先頭に戻る
for i in range(5):
    if i == 3:
        continue
    print(i, end="")
print("")

# ## 関数
def hello():
    print("Hello!")
# タブが必要
hello()
def hello(name):
    #print("Hello {}!".format(name))
    print("Hello %s!" % name)
hello("murbook")
print("\n")


# ## クラス(=オブジェクト、変数と関数をまとめたもの)
# 引数にselfは必須
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHello(self):
        print("Hello! I'm {}!".format(self.name))
human = Human("murs", 20)
print(human.age)
print(human.name)
human.sayHello()
