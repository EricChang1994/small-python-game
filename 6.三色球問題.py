import os
print('三色球問題')
print('red   yellow   blue')
for red in range(0,4):
    for yellow in range(0,4):
        for blue in range(0,7):
            if red+blue+yellow==8:
                print (red,'\t',yellow, '\t',blue,'\t')
print('------文旦製作-----')
os.system('pause')
