# 数値型、文字列、論理値、比較、コメント

#Pythonのバージョン確認
import platform
print(platform.python_version())
print("\n")

# 日本語入力に対応させる
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# # 数値型
# int, float, complex
# 加算+, 減算-, 乗算*, 除算/, 切り捨て除算//, 余り%, べき乗**
# 型の宣言はしない
x=10
print(x/3) #除算
print(x//3) #切り捨て除算
print(x%3) # 余り
print(x**2) #べき乗
x+=3
print(x)


# # 文字列
# シングルクォート
print('シングルクォートで囲むと"ダブルクォートを"使用できる')
# ダブルクォート
print("ダブルクォートで囲むと'シングルクォート'を使用できる")
# 三重引用符
string = """3つ重ねると
改行を保持できる"""
print(string)
print("\n")

# 連結
print("Hello "+"world")
# 繰り返し
print("Hello "*3)
print("\n")

# ＃#書式化
print ('Hello, %s!' % 'World')
print ('Hi, %s. You are %d years old' % ('John', 25))

# format()を使った書式化
# {}内の値をformatメソッドで指定することができる
name="murbook"
print("Hello "+name+"!")
print("Hello {}!".format(name))

num=150
# print("合計は"+num+"円です") # TypeError
print("合計は{}円です。".format(num))
print("\n")

# 文字列の有無を調べる
print("th" in "python")
# 文字列の分割
print('pain-au-chocolat'.split('-'))
# 文字列の結合
print('-'.join(['pain', 'de', 'campagne']))
print("\n")

# ## エスケープ
print('I\'m murs')
print("Hello\nWorld")
print("Hello\tWorld")
print("\n")


# # 論理値
# True, False (**頭は大文字**)
t=True
f=False
print(not t)
print(f is True)
print(t and f)
print(t or f)
print("\n")

# # 比較
# < より小さい
# <= 以下
# > より大きい
# >= 以上
# == 等しい
# != 等しくない
# is 同一のオブジェクトである
# is not 同一のオブジェクトでない
print(int(100) == float(100.0))
print(int(100) is float(100.0))
print("\n")


# # コメント
# Jupyterだからあんまつかわんけど
# 行コメント
'''
ブロックコメント(テキスト扱い、注意が必要らしい)
'''
