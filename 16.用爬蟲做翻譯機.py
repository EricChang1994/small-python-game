input('------歡迎使用爬蟲翻譯機  By文旦------')
import urllib.request
import urllib.parse
import json
import os

command = int(1)
while command == 1:
    content = input('請輸入翻譯內容:\n')
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='



    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['typoResult']='true'
    data=urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    print('翻譯結果:%s \n'%(target['translateResult'][0][0]['tgt']))

    command = int(input('是否繼續翻譯? 0.結束 1.繼續翻譯'))

    

