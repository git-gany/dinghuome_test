
"""解除绑定接口"""

import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import CONFIG
import requests

# 解除小程序绑定接口
def Login_exit(unionid=CONFIG.Unionid()):
    url = CONFIG.Url()+'/api/small/member/unBind.jhtml'
    params = {'unionId': unionid}
    request_login_exit = requests.get(url, params)
    if request_login_exit.status_code == 200:
        if request_login_exit.json()['msg'] == '成功':
            return '账号成功解除绑定', request_login_exit.json()
        elif request_login_exit.json()['msg']=='您已经解除了绑定':
            return '账号未登陆，无需解除绑定'
        else:
            return '[×] 异常记录-->%s', request_login_exit.json()
    else:
        return '[×] %s 你懂的' % request_login_exit.status_code
if __name__ == '__main__':
    print(Login_exit())
