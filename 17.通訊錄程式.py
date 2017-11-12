print('---- 歡迎使用通訊錄 BY文旦製作 ----')
print('----1.查詢聯絡人資料----')
print('----2.新增新的聯絡人----')
print('----3.刪除已有聯絡人----')
print('----4.退出通訊錄程式---- \n')

contact = {'文睿':'0908809522'}

while True:
    fun=int(input('請輸入你要使用的功能:'))
    
    if fun == 1:
        
        search = input('請輸入您要查詢的人名:')

        if contact.get(search) == None:
            print('查無此人，請重新輸入。')
        else:
            print('%s 的電話:' %search , contact[search])
        print('\n')

    if fun == 2:
        
        new = input('請輸入您要新增的聯絡人:')

        if contact.get(new) == None:

            number = input('請輸入聯絡人的電話號碼: \n')
            contact.update({new : number})

        else:

            deter = int(input('此聯絡人已經存在，是否更改資料? 0.Yes 1.No '))

            if deter == 0:
                number = input('請輸入聯絡人的電話號碼: ')
                contact.update({new : number})

            else:
                continue
        print('\n')
            
        
    if fun == 3:
        
        delet=input('請輸入您要刪除的聯絡人姓名:')
        contact.pop(delet)
        print('\n')

    if fun == 4:
        print('----- 感謝使用旦哥通訊錄 ----')
        print('\n')
        break    
