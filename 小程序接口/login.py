
"""小程序登陆接口"""

import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import CONFIG
import requests
import time
import login_exit

# 登陆接口,其他模块调用
def Login(tel=CONFIG.Mobile()):
    login_exit.Login_exit() # 初始化操作，解除绑定
    url = CONFIG.Url() + '/api/small/login/checkSms.jhtml'

    # 判断是1还是2开头的手机号码并生成相应的验证码
    # tel = CONFIG.Mobile()
    if str(tel[:2]) == '23' and len(str(tel)) == 11:
        code = str((int(tel[:1]) + int(tel[-5:])) * 201812306 )[:6]
    elif str(tel[0]) == '1' and len(tel) == 11:
        code = tel[-4:]+time.strftime('%m%d')
    else:
        return '[×] 异常记录-->登陆账号错误'

    params = {'tel': tel,
              'code': code,
              'unionId': CONFIG.Unionid()}
    # print(params['tel'])
    request_login = requests.get(url, params)
    if request_login.status_code == 200:
        if request_login.json()['msg'] == '成功':
            return '登陆成功', request_login.json()
        else:
            return '[×] 异常记录-->%s'%request_login.json()
    else:
        return '[×] %s登录失败' % request_login.status_code

# 登陆接口用例
def Login_edit(tel, code):
    login_exit.Login_exit()
    url = CONFIG.Url() + '/api/small/login/checkSms.jhtml'
    params = {'tel': tel,
              'code': code,
              'unionId': CONFIG.Unionid()}
    request_login = requests.get(url, params)
    if request_login.status_code == 200:
        if request_login.json()['msg'] == '成功':
            return '登陆成功'
        else:
            return request_login.json()
    else:
        return '[×] %s登录失败' % request_login.status_code

Login()
