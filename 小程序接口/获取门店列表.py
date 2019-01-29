
"""eg"""
import sys; sys.path.append('../')
import requests
import CONFIG
import login

login.Login('17602120657') # 门店信息对应的账号

url = CONFIG.Url() +'/api/small/shop/list.jhtml'
params ={'unionId': CONFIG.Unionid(),
          'pageSize': '20',
          'pageNumber': '1'}
a = requests.get(url, params=params)
if a.status_code == 200:
    b = a.json()['data']['list']
    for c in b:
        if c['myself'] == True:
            if c['shopType'] == 'direct':
                print('[直营店]%s' % c['name'])
            elif c['shopType'] == 'affiliate':
                print('[加盟店]%s' % c['name'])
        else:
            if c['shopType'] == 'direct':
                print('[托管店][直营店]%s' % c['name'])
            elif c['shopType'] == 'affiliate':
                print('[托管店][加盟店]%s' % c['name'])
else:
    print(a.status_code, '门店列表获取失败')
