def gcd(x,y):
	if y:
		return gcd(y,x%y)
	else:
		return x
a=int(input('請輸入X:'))
b=int(input('請輸入Y:'))
print('他們的最大公因數是: %d'%(gcd(a,b)))
