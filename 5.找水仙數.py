import os
print("求100到999的水仙花數")

for i in range(100,1000):
    temp=i
    a=temp%10
    b=((temp-a)%100)/10
    c=((temp-(b*10)-a))/100
    det=a*a*a+b*b*b+c*c*c
    if det==i:
        print(i)

print("--------文旦製作--------")
os.system('pause')
