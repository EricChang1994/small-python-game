import os 
import random

command=input("---------------神奇寶貝大師---------------")
command = int(input("是否開始對戰? 0.開始對戰 1.走為上策"))
while command == 0:

    choice=int(input("請問要派出什麼神奇寶貝??0.妙挖種子 1.小火龍 2.傑尼龜"))
    c_choice=random.randint(0,2)



    if choice == 0:
        print("你派出了妙挖種子!")

        if c_choice == 0:
            print("對方派出妙蛙種子，平分秋色!")
        if c_choice == 1:
            print("對方派出小火龍，屬性相剋，你輸了!")
        if c_choice == 2:
            print("對方派出傑尼龜，GOOD，你贏了!")

    elif choice == 1:
        print("你派出了小火龍!")

        if c_choice == 0:
            print("對方派出妙蛙種子，GOOD，你贏了!")
        if c_choice == 1:
            print("對方派出小火龍，平分秋色!")
        if c_choice == 2:
            print("對方派出傑尼龜，屬性相剋，你輸了!")

    elif choice == 2:
        print("你派出了傑尼龜!")

        if c_choice == 0:
            print("對方派出妙蛙種子，屬性相剋，你輸了!")
        if c_choice == 1:
            print("對方派出小火龍，GOOD，你贏了!")
        if c_choice == 2:
            print("對方派出傑尼龜，平分秋色!")
    command = int(input("要繼續玩嗎?  0. 繼續 1. 不了"))


print("----------逃走了!!----------")

os.system("pause") 
    
