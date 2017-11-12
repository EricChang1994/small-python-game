import os
def count(inputStr):
    length = len(inputStr)
    count = 0
    alpha = 0
    number = 0
    space = 0
    others = 0
    while count != length:

        if inputStr[count].isdigit():
            number += 1
        elif inputStr[count].isalpha():
            alpha += 1
        elif inputStr[count] == ' ':
            space += 1
        else:
            others+=1

        
        count += 1
    print('本字串共有 %d 個數字， %d 個字符 %d 個空格 和 %d 個其他字元' %(number,alpha,space,others))
a=input('請輸入字串:')
count(a)

os.system('pause')
