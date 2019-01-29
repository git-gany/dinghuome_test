
"""添加门店接口( “餐厅”页创建 )"""

import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import requests
import time
import login
import CONFIG
import view_shop
import information

def Add_shop_direct(): # 创建直营店
    if information.Information()[0] == '1': # 判断是否存在企业，没有企业的话无法创建直营店;1存在，0不存在
        login.Login() # 初始化登陆
        url = CONFIG.Url()+'/api/small/shop/add.jhtml'
        params = {
                'unionId': CONFIG.Unionid(),  # unionid
                'shopType': 'direct',   # 门店类型 affiliate，加盟；direct 直营
                'name': '直营店'+time.strftime('%Y%m%d-%H%M%S'),
                'userName': '木易',
                'areaId': '800',
                'address': 'address',
                'ids': '',
                'receiverTel': '13800000000',
                'businessCategoryId': '42',
                'startManageTime': '12:00',
                'endManageTime': '12:01',
                'longitude': '121',
                'latitude': '31'}
        request_add_shop_direct = requests.post(url, params)
        if request_add_shop_direct.status_code != 200:
            return '[×] 创建直营门店接口异常-->%s'% request_add_shop_direct.status_code
        else :
            if request_add_shop_direct.json()['code'] != '0': # 根据code确认是否创建成功，0成功，其他则失败
                return '[×] %s_直营门店创建失败，创建的名称:%s'%(request_add_shop_direct.json(), params['name'])
            else:
                # 获取门店接口，判断门店是否存在于门店列表
                shop_list = view_shop.View_shop_name()[1]
                # params = {'name': '又乐'} # 测试数据，写死的不存在的门店名称
                if params['name'] in shop_list:
                    return '直营门店创建成功', params
                else:
                    return '[×] 直营门店创建失败,创建的门店在列表中不存在_创建的名称:%s_门店列表:%s'%(params['name'], shop_list)
              # return request_add_shop.json()
    elif information.Information()[0] == '0':
        return '账号不存在企业，跳过创建直营门店', '账号未创建企业'
    else:
        return '[×] 获取企业信息异常，无法创建门店'

def Add_shop_affiliate(): # 创建加盟店
    login.Login() # 初始化登陆
    url = CONFIG.Url()+'/api/small/shop/add.jhtml'
    params = {
            'unionId': CONFIG.Unionid(),  # unionid
            'shopType': 'affiliate',      # 门店类型 affiliate，加盟；direct 直营
            'name': '加盟店'+time.strftime('%Y%m%d-%H%M%S'),
            'userName': '木易',
            'areaId': '800',
            'address': 'address',
            'ids': '',
            'receiverTel': '13800000000',
            'businessCategoryId': '42',
            'startManageTime': '12:00',
            'endManageTime': '12:01',
            'longitude': '121',
            'latitude': '31'}
    request_add_shop_affiliate = requests.post(url, params)
    if request_add_shop_affiliate.status_code != 200:
        return '[×] 创建加盟门店接口异常-->%s' % request_add_shop_affiliate.status_code
    else :
        if request_add_shop_affiliate.json()['code'] != '0': # 根据code确认是否创建成功，0成功，其他则失败
            return '[×] %s_加盟门店创建失败，创建的门店名称:%s'%(request_add_shop_affiliate.json(), params['name'])
        else:
            shop_list = view_shop.View_shop_name()[1] # 获取门店接口，判断门店是否存在于门店列表
              # params = {'name': '又乐'} # 测试数据，写死的不存在的门店名称
            if params['name'] in shop_list:
                return '加盟门店创建成功', params['name']
            else:
                return '[×] 加盟门店创建失败,创建的加盟门店在列表中不存在_创建的加盟店名称:%s_门店列表:%s'% (params['name'],shop_list)

if __name__ == '__main__':
    print(Add_shop_direct(), '\n')
    # print(Add_shop_affiliate(), '\n')

