
"""BD工具"""

import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import requests
import time
import CONFIG
import view_shop
import DATA_BASE
import login

# BD时获取门店列表
def Bd_shop_list():
    url = CONFIG.Url() + '/api/small/shop/getShopList.jhtml'
    login.Login()
    try:
        params = {'unionId': CONFIG.Unionid(),
                  'memberId': DATA_BASE.Member_id()[0],
                  'channelId': '1'  # 暂定渠道ID
                  }
    except Exception as error:
        return '[×] [BD时获取门店列表失败]-->前置参数获取异常-->unionId/memberid 获取异常-->%s'% error
    request = requests.get(url, params)
    # print(request.url)
    if request.status_code != 200:
        return '[×] BD门店列表获取失败 %s' % request.status_code
    else:
        if request.json()['msg'] == '成功':
            view_list = view_shop.View_shop_affiliate_1()[1] # 获取门店列表加盟店数量
            if len(request.json()['data']) != len(view_list): # 判断BD门店列表的数量与加盟店数量是否一致
                return '[×] BD门店列表获取成功(BD数量与门店列表数量不匹配正确)', {'门店列表加盟店数量': len(view_list)}, {'BD门店列表数量': len(request.json()['data'])}, {'BD门店列表': request.json()['data']}
            else:
                return 'BD门店列表获取成功', {'门店列表加盟店(不含托管)数量': len(view_list)}, {'BD门店列表数量': len(request.json()['data'])}, {'BD门店列表': request.json()['data']}
        else:
            return '[×] BD门店列表获取失败 %s' % request.json()

# 查看BD门店信息
def Bd_shop_view():
    url = CONFIG.Url() + '/api/small/shop/getShop.jhtml'
    params = {'id': '3314'}  # 加盟店(BD专用)_加盟门店id，暂定写死
    request = requests.get(url, params)
    # print(request.url)
    if request.status_code != 200:
        return '[×] 查看BD门店信息失败 %s' % request.status_code
    else:
        if request.json()['msg'] == '成功':
            return 'BD门店查看成功', request.json()
        else:
            return '[×] 查看BD门店信息异常 %s' % request.json()

# BD门店(添加)
def Bd_shop_add():
    try:
        shop_list = view_shop.View_shop_name()
    except Exception as error:
        return '门店列表获取失败'
    if len(shop_list) > 0:
        return '账号下已存在门店, BD时无法创建门店, 跳过'
    else:
        url = CONFIG.Url() + '/api/small/shop/channelSave.jhtml'
        params = {'name': '加盟店(BD/添加)'+time.strftime('%Y%m%d-%H%M%S'),
                  'businessCategoryId': '2',
                  'userName': '木易',
                  'receiverTel': '13800000000',
                  'areaId': '800',
                  'address': '上海市杨浦区海上海',
                  'latitude': '31.266908',
                  'longitude': '121.508925',
                  'startManageTime': '00:00',
                  'endManageTime': '23:59',
                  'introduction': '这是采购说明',  # 采购说明
                  'doorPhoto': 'http://test.dinghuo.me/upload/image/201901/cc4dc70a-5f2d-47db-b8e5-0855f9a3cfb5.jpg',
                  'inStorePhoto': 'http://test.dinghuo.me/upload/image/201901/75dd76c2-91a6-4fdd-add8-f3f57430a973.jpg',
                  'type': 'general',  # general 普通 #dedicated 隐藏门店
                  'memberId': DATA_BASE.Member_id()[0]
                  }
        request = requests.post(url, params)
        # print(request.url)
        if request.status_code != 200:
            return '[×] 状态: %s_BD门店添加失败' % request.status_code
        else:
            shop_list = view_shop.View_shop_name()
            print(params['name'])
            if params['name'] in shop_list:
                return 'BD时门店添加成功', request.json()
            else:
                return 'BD时门店创建失败'






if __name__ == '__main__':
    print(Bd_shop_list()) # BD时获取门店列表
    # print(Bd_shop_view())
    # print(Bd_shop_add())
