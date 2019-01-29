

"""接口测试用例"""

import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import pytest
import sys
import time
import login
import login_exit
import add_shop
import seckill
import goods
import supplier
import view_shop
import information
import bd
import order

# 登录相关
# @pytest.mark.skip(reason='跳过，没理由')
@pytest.mark.skipif(sys.version_info < (3, 0), reason="python版本低于3.0, 用例无法运行")
class Test_login:
    def test_1_1_1(self):  # 账号&验证码为空
        assert login.Login_edit('', '') != '登陆成功'

    def test_1_1_2(self):  # 账号为空
        assert login.Login_edit('', '123456') != '登陆成功'

    def test_1_1_3(self):  # 验证码为空
        assert login.Login_edit('17602120657', '') != '登陆成功'

    def test_1_1_4(self):  # 手机号格式错误
        assert login.Login_edit('21321', '123456') != '登陆成功'

    def test_1_1_5(self):  # 验证码错误
        assert login.Login_edit('17602120657', '123123') != '登陆成功'

    def test_1_1_6(self):  # 账号及验证码正确
        assert login.Login_edit('17602120657', '0657'+time.strftime('%m%d')) == '登陆成功'
