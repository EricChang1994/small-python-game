def findStr(desStr,subStr):
    count=0
    length=len(desStr)
    if subStr not in desStr:
        print('沒有搜尋結果')
    else:
        for each in range(length-1):
            if desStr[each] == subStr[0]:
                if desStr[each+1] == subStr[1]:
                    count += 1

    print('字串中共出現%d次' %count)

desStr = input('請輸入段落字串:')
subStr = input('請輸入子字符串(兩個字符):')
findStr(desStr,subStr)
