#関数を定義
def fizzbuzz(n):
    if n%15==0:
        return "FizzBuzz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return str(n)

#実行
for i in range(1,101):
    print(fizzbuzz(i))
