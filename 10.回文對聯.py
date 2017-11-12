import os
def deter(inputStr):
    length=len(inputStr)
    count=int(length/2)

    for each in range(count):
        if inputStr[each] != inputStr[length-each-1]:
            print('不是回文對聯')
            break

    print('是回文對聯')
        
a=input('請輸入字串:')
deter(a)
os.system('pause')
