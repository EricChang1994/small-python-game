#替規函數概念:調用含數自身的行為
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

number = int(input('請輸入一個正整數:'))
result = factorial(number) 
print('%d 的階層是: %d'%(number, result))
