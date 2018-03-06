#type関数を使って変数の型を確認する
myvar = 1234
print(type(myvar))

mystr = "Hello"
print(type(mystr))

mylist = [1,2,3,4]
mydict = {"one":1, "two":2, "three":3}
print(type(mylist))
print(type(mydict))

def myfunc():
    return(0)
print(type(myfunc))
print()

#isinstance関数を使って変数が指定した型であるか確認する
myvar = 1234
print(isinstance(myvar, int))
print()

#isinstance関数は、スーパークラスでもTrueを返す
class mysuperclass(object):
    pass
class myclass(mysuperclass):
    pass
myinstance = myclass()

print(type(myinstance))
print(type(myinstance)==myclass)
print(type(myinstance)==mysuperclass)
print(isinstance(myinstance, myclass))
print(isinstance(myinstance, mysuperclass))
