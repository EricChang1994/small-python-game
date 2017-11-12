import os 
print('------------判斷分數--------------')

det=0
while det==0:
    score = int(input('輸入您的分數:'))
    if 100 > score >= 80:
        print('您的分數是等級A\n')
    elif 80 > score >= 70:
        print('您的分數是等級B\n')
    elif 70 > score >= 60:
        print('您的分數是等級C\n')
    elif 60 > score >=0:
        print('您的分數是等級D\n')
    else:
        print('輸入錯誤')
        
    det=int(input("是否繼續判斷:0.繼續1.退出程式\n"))

print('------------文旦製作--------------')

os.system("pause") 
