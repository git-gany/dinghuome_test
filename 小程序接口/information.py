
"""获取小程序企业信息"""

import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import requests
import CONFIG
import login

# 其它接口调用, 获取“我的”中企业信息
def Information(unionid = CONFIG.Unionid()):
    login.Login()
    url = CONFIG.Url() + '/api/small/member/get.jhtml'
    params = {'unionId': unionid}
    request = requests.get(url, params)
    if request.status_code != 200:
        return '[×] %s, 企业信息获取异常' % request.status_code
    else:
        if request.json()['data']['flag'] is True:
            return '1',  request.json()# 账号已创建企业
        elif request.json()['data']['flag'] is False:
            return '0', request.json() # 账号未创建企业
        else:
            return '[×] %s, 企业信息获取异常' % request.json()

if __name__ == '__main__':
    print(Information())

