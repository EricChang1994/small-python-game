import os
print("----------歡迎光臨證券公司交易系統--------")
ans=("Taiwan0522")
i=3
while i!=0:
    bingo=input("輸入密碼:")
    
    while '*'  in bingo:
        print('密碼不得含有*字')
        i=i+1
        break
    
    if bingo==ans:
        print("成功登入 進入交易系統中----（>∀<）")
        i=3
        break
    else:
        i=i-1
    if i!=0:
        print('提示:文旦國籍生日')
        print('你還有',i,'次機會\n')
    else:
        print("----------登入失敗 (ò皿ó)--------\n")
print("----------文旦製作--------")
os.system("pause")
