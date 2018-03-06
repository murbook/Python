# リスト、タプル、辞書型、集合

# ## リスト
l = ['A','B','C','D','E']
print(l)
print(l[0]) #A
print(len(l)) #5
print(l[-1]) #E
print("\n")

# ### スライス
# インデックス
# |  A |  B |  C |  D |  E |    |
# |  0 |  1 |  2 |  3 |  4 |  5 |
# | -5 | -4 | -3 | -2 | -1 |    |
# l[a:b]は、a<=x<b のような感じ
print(l[1:3]) #BC
print(l[2:]) #CDE
print(l[:5]) #ABCDE
print(l[:-1]) #ABCD
print("\n")

l.append('F')
print(l)
#ひとつ飛ばし
print(l[0::2])
# リスト内包表記
print([x for x in range(0, 10)])
print(2 in [1, 2, 3])
print("\n")

# ## ディクショナリ
d = {'a': 1, 'b': 2}
print(d)
print(d['a'])
d['c'] = 100
print(d)
print('a' in d)
print(2 in d.values())
