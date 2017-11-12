import os
import random
print('--------猜數字遊戲---------')
secret = random.randint(1,10)
temp = input("猜猜電腦君最喜歡的數字:")
guess=int(temp)

if guess < secret:
    print("小了小了，在猜看看吧")
elif guess>secret:
    print("大了大了，在猜看看吧")
else:
    print("恭喜你答對了~~")

while guess!=secret:

    temp = input("哎呀錯了，重新輸入吧:")
    guess=int(temp)
    
    if guess==secret:
        print("恭喜你答對了~~")
        
    else:
        if guess < secret:
            print("小了小了，在猜看看吧")
        else:
            print("大了大了，在猜看看吧")

print("遊戲結束 下次再玩吧^____^")

print('--------文旦製作---------')


os.system("pause") 
