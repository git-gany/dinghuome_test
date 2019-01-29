
"""购物车相关"""


import requests
import random
import sys; sys.path.append('../')
import CONFIG
import supplier
import goods
import login

'''
1-平台-A-a
2-平台-A-B-b
3-平台-A-b
4-本地-A-a
5-本地-A-B-b
6-本地-A-b
7-本地-直营门店-本地货品
8-本地-加盟门店-本地货品
'''

# 查看购物车  # 半成品,未做价格相关的校验
class See_shoppingCart:

    # 返回示例-->成功--> ('直营店-平台-自有直营型订单购物车获取成功', {'code': '0', 'msg': '成功', 'requesturl': '', 'data': {'amount': 16.5, 'list': [{'goodsId': 25027, 'valid': True, 'date': '', 'name': '大米', 'saleableInventory': True, 'purchasedQuantity': -1, 'nowActivityNumber': '', 'quantity': 11, 'activityTimeId': '', 'minOrderQuantity': 1, 'isStock': True, 'isMarketable': True, 'image': 'https://www.dinghuo.me/upload/image/201901/e5e97c8a-18d9-42f5-af0e-6ba9cddb7dfa.jpg', 'maxActivityNumber': '', 'activityPrice': '', 'specifications': [], 'productId': 29133, 'unit': '箱', 'cartItemId': 19812, 'now': 1548309022873, 'stockNumber': 9999994, 'supplyPrice': 1.5, 'maxNumber': -1, 'activityType': '', 'activityTime': ''}], 'displayPrice': 'display'}, 'data2': ''})
    #           失败--> [×] 直营店-平台-自有直营型订单购物车时出现异常 404

    # 查看直营店-平台-自有直营型订单购物车
    def See_shoppingCart_1(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/list.jhtml'
        # if len(supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]) == 0:
        #     return '该门店自有直营供应商暂未进行供货'
        # else:
        #     pass
        supplierId = supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['id']
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplierId,
                  'shopId': '3212',
                  'supplierType': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['relationId'],
                  'types': 'platform',
                  'supplyType': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['supplyType']
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                goodsList = xx.json()
                return '直营店-平台-自有直营型订单购物车获取成功', goodsList
            else:
                return '[×] 直营店-平台-自有直营型订单购物车时出现异常 %s' % xx.xx.json()['msg']
        else:
            return '[×] 直营店-平台-自有直营型订单购物车时出现异常 %s' % xx.status_code


    # 查看直营店-平台-直营型订单购物车
    def See_shoppingCart_2(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/list.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_platform_zhiying()[0]['id'],
                  'shopId': '3212',
                  'supplierType': supplier.Supplier_id().Supplier_platform_zhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_platform_zhiying()[0]['relationId'],
                  'types': 'platform',
                  'supplyType': supplier.Supplier_id().Supplier_platform_zhiying()[0]['supplierType']
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                goodsList = xx.json()
                return '直营店-平台-直营型订单购物车获取成功', goodsList
            else:
                return '[×] 直营店-平台-直营型订单购物车出现异常 %s' % xx.xx.json()['msg']
        else:
            return '[×] 直营店-平台-直营型订单购物车出现异常 %s' % xx.status_code


    # 查看加盟店-平台-三方型订单购物车
    def See_shoppingCart_3(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/list.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_platform_sanfang()[0]['id'],
                  'shopId': '3214',
                  'supplierType': supplier.Supplier_id().Supplier_platform_sanfang()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_platform_sanfang()[0]['relationId'],
                  'types': 'platform',
                  'supplyType': supplier.Supplier_id().Supplier_platform_sanfang()[0]['supplierType']
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                goodsList = xx.json()
                return '加盟店-平台-三方型订单购物车获取成功', goodsList
            else:
                return '[×] 加盟店-平台-三方型订单购物车出现异常 %s' % xx.xx.json()['msg']
        else:
            return '[×] 加盟店-平台-三方型订单购物车出现异常 %s' % xx.status_code


    # 查看直营店-本地-自有直营型订单购物车
    def See_shoppingCart_4(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/list.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['id'],
                  'shopId': '3212',
                  'supplierType': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['relationId'],
                  'types': 'local',
                  'supplyType': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['supplierType']
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                goodsList = xx.json()
                return '直营店-本地-自有直营型订单购物车获取成功', goodsList
            else:
                return '[×] 直营店-本地-自有直营型订单购物车出现异常 %s' % xx.xx.json()['msg']
        else:
            return '[×] 直营店-本地-自有直营型订单购物车出现异常 %s' % xx.status_code


    # 查看直营店-本地-直营型订单购物车
    def See_shoppingCart_5(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/list.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_local_zhiying()[0]['id'],
                  'shopId': '3212',
                  'supplierType': supplier.Supplier_id().Supplier_local_zhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_zhiying()[0]['relationId'],
                  'types': 'local',
                  'supplyType': supplier.Supplier_id().Supplier_local_zhiying()[0]['supplierType']
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                goodsList = xx.json()
                return '直营店-本地-直营型订单购物车获取成功', goodsList
            else:
                return '[×] 直营店-本地-直营型订单购物车出现异常 %s' % xx.xx.json()['msg']
        else:
            return '[×] 直营店-本地-直营型订单购物车出现异常 %s' % xx.status_code


    # 查看加盟店-本地-三方型订单购物车
    def See_shoppingCart_6(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/list.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_local_sanfang()[0]['id'],
                  'shopId': '3214',
                  'supplierType': supplier.Supplier_id().Supplier_local_sanfang()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_sanfang()[0]['relationId'],
                  'types': 'local',
                  'supplyType': supplier.Supplier_id().Supplier_local_sanfang()[0]['supplierType']
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                goodsList = xx.json()
                return '加盟店-本地-三方型订单购物车获取成功', goodsList
            else:
                return '[×] 加盟店-本地-三方型订单购物车出现异常 %s' % xx.xx.json()['msg']
        else:
            return '[×] 加盟店-本地-三方型订单购物车出现异常 %s' % xx.status_code


    # 查看直营店-本地-本地供应商订单购物车
    def See_shoppingCart_7(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/list.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_local_zhiying_shop()[0]['id'],
                  'shopId': '3212',
                  'supplierType': supplier.Supplier_id().Supplier_local_zhiying_shop()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_zhiying_shop()[0]['relationId'],
                  'types': 'local',
                  'supplyType': supplier.Supplier_id().Supplier_local_zhiying_shop()[0]['supplierType']
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                goodsList = xx.json()
                return '直营店-本地-本地供应商订单购物车获取成功', goodsList
            else:
                return '[×] 直营店-本地-本地供应商订单购物车出现异常 %s' % xx.xx.json()['msg']
        else:
            return '[×] 直营店-本地-本地供应商订单购物车出现异常 %s' % xx.status_code


    # 查看加盟店-本地-本地供应商订单购物车
    def See_shoppingCart_8(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/list.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['id'],
                  'shopId': '3214',
                  'supplierType': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['relationId'],
                  'types': 'local',
                  'supplyType': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['supplierType']
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                goodsList = xx.json()
                return '加盟店-本地-本地供应商订单购物车获取成功', goodsList
            else:
                return '[×] 加盟店-本地-本地供应商订单购物车出现异常 %s' % xx.xx.json()['msg']
        else:
            return '[×] 加盟店-本地-本地供应商订单购物车出现异常 %s' % xx.status_code

# 清空购物车全部货品
class Delete_shoppingcartgoods:
    login.Login()

    # 清空直营店-平台-自有直营型订单购物车
    def Delete_shoppingcartgoods_1(self):
        def Del(cartItemId):
            url = CONFIG.Url() + '/api/small/cart/deleteCartItem.jhtml'
            params = {'unionId': CONFIG.Unionid(),
                      'cartItemId': cartItemId  # 购物车货品id
                      }
            xx = requests.post(url, params)
            if xx.status_code == 200:
                if xx.json()['msg'] == '成功':
                    # print('', end='')
                    return '0', '成功'
                else:
                    return '1', '[×] 直营店-平台-自有直营型订单购物车清空失败_%s' % xx.json()['msg']
            else:
                return '1', '[×] 直营店-平台-自有直营型订单购物车清空失败_%s' % xx.status_code
        try:  # 获取购物车列表及异常处理
            shoppingCart_list = See_shoppingCart().See_shoppingCart_1()[1]['data']['list']  # 获取购物车所有货品
        except Exception as error:
            # logging.exception(error)
            return '[×] 直营店-平台-自有直营型订单购物车清空失败_获取购物车货品失败-->%s' % error
        for cartitemid in shoppingCart_list:
            Del_ = Del(cartitemid['cartItemId'])
            if Del_[0] == '0':
                # print('', end='')
                pass
            else:
                return '[×] 直营店-平台-自有直营型订单购物车清空失败_%s' % Del_[1]
        if len(See_shoppingCart().See_shoppingCart_1()[1]['data']['list']) == 0:
            return '直营店-平台-自有直营型订单购物车清空成功'
        else:
            return '[×] 直营店-平台-自有直营型订单购物车清空失败_%s' % len(See_shoppingCart().See_shoppingCart_1()[1]['data']['list'])

    # 清空直营店-平台-直营型订单购物车
    def Delete_shoppingcartgoods_2(self):
        def Del(cartItemId):
            url = CONFIG.Url() + '/api/small/cart/deleteCartItem.jhtml'
            params = {'unionId': CONFIG.Unionid(),
                      'cartItemId': cartItemId  # 购物车货品id
                      }
            xx = requests.post(url, params)
            if xx.status_code == 200:
                if xx.json()['msg'] == '成功':
                    # print('', end='')
                    return '0', '成功'
                else:
                    return '1', '[×] 直营店-平台-直营型订单购物车清空失败_%s'% xx.json()['msg']
            else:
                return '1', '[×] 直营店-平台-直营型订单购物车清空失败_%s' % xx.status_code

        try:
            shoppingCart_list = See_shoppingCart().See_shoppingCart_2()[1]['data']['list']
        except Exception as error:
            # logging.exception(error)
            return '[×] 直营店-平台-直营型订单购物车清空失败_查看购物车失败-->%s' % error
        for cartitemid in shoppingCart_list:
            Del_ = Del(cartitemid['cartItemId'])
            if Del_[0] == '0':
                # print('', end='')
                pass
            else:
                return '[×] 直营店-平台-直营型订单购物车清空失败_%s' % Del_[1]
        if len(See_shoppingCart().See_shoppingCart_2()[1]['data']['list']) == 0:
            return '直营店-平台-直营型订单购物车清空成功'
        else:
            return '[×] 直营店-平台-直营型订单购物车清空失败5_%s' % len(See_shoppingCart().See_shoppingCart_2()[1]['data']['list'])

    # 清空加盟店-平台-三方型订单购物车
    def Delete_shoppingcartgoods_3(self):
        def Del(cartItemId):
            url = CONFIG.Url() + '/api/small/cart/deleteCartItem.jhtml'
            params = {'unionId': CONFIG.Unionid(),
                      'cartItemId': cartItemId  # 购物车货品id
                      }
            xx = requests.post(url, params)
            if xx.status_code == 200:
                if xx.json()['msg'] == '成功':
                    # print('', end='')
                    return '0', '成功'
                else:
                    return '1', '[×] 加盟店-平台-三方型订单购物车清空失败_%s' % xx.json()['msg']
            else:
                return '1', '[×] 加盟店-平台-三方型订单购物车清空失败_%s' % xx.status_code

        try:
            shoppingCart_list = See_shoppingCart().See_shoppingCart_3()[1]['data']['list']
        except Exception as error:
            # logging.exception(error)
            return '[×] 加盟店-平台-三方型订单购物车清空失败_查看购物车失败-->%s' % error
        for cartitemid in shoppingCart_list:
            Del_ = Del(cartitemid['cartItemId'])
            if Del_[0] == '0':
                # print('', end='')
                pass
            else:
                return '[×] 加盟店-平台-三方型订单购物车清空失败_%s' % Del_[1]
        if len(See_shoppingCart().See_shoppingCart_3()[1]['data']['list']) == 0:
            return '加盟店-平台-三方型订单购物车清空成功'
        else:
            return '[×] 加盟店-平台-三方型订单购物车清空失败_%s' % len(See_shoppingCart().See_shoppingCart_3()['data']['list'])

    # 清空直营店-本地-自有直营型订单购物车
    def Delete_shoppingcartgoods_4(self):
        def Del(cartItemId):
            url = CONFIG.Url() + '/api/small/cart/deleteCartItem.jhtml'
            params = {'unionId': CONFIG.Unionid(),
                      'cartItemId': cartItemId  # 购物车货品id
                      }
            xx = requests.post(url, params)
            if xx.status_code == 200:
                if xx.json()['msg'] == '成功':
                    # print('', end='')
                    return '0', '成功'
                else:
                    return '1', '[×] 直营店-本地-自有直营型订单购物车清空失败_%s'% xx.json()['msg']
            else:
                return '1', '[×] 直营店-本地-自有直营型订单购物车清空失败_%s' % xx.status_code

        try:
            shoppingCart_list = See_shoppingCart().See_shoppingCart_4()[1]['data']['list']
        except Exception as error:
            # logging.exception(error)
            return '[×] 直营店-本地-自有直营型订单购物车清空失败_查看购物车失败-->%s' % error
        for cartitemid in shoppingCart_list:
            Del_ = Del(cartitemid['cartItemId'])
            if Del_[0] == '0':
                pass
            else:
                return '[×] 直营店-本地-自有直营型订单购物车清空失败_%s' % Del_[1]
        if len(See_shoppingCart().See_shoppingCart_4()[1]['data']['list']) == 0:
            return '直营店-本地-自有直营型订单购物车清空成功'
        else:
            return '[×] 直营店-本地-自有直营型订单购物车清空失败_%s' % len(See_shoppingCart().See_shoppingCart_4()[1]['data']['list'])

    # 清空直营店-本地-直营型订单购物车
    def Delete_shoppingcartgoods_5(self):
        def Del(cartItemId):
            url = CONFIG.Url() + '/api/small/cart/deleteCartItem.jhtml'
            params = {'unionId': CONFIG.Unionid(),
                      'cartItemId': cartItemId  # 购物车货品id
                      }
            xx = requests.post(url, params)
            if xx.status_code == 200:
                if xx.json()['msg'] == '成功':
                    # print('', end='')
                    return '0', '成功'
                else:
                    return '1', '[×] 查看直营店-本地-直营型订单购物车清空失败_%s'% xx.json()['msg']
            else:
                return '1', '[×] 查看直营店-本地-直营型订单购物车清空失败_%s' % xx.status_code

        try:
            shoppingCart_list = See_shoppingCart().See_shoppingCart_5()[1]['data']['list']
        except Exception as error:
            # logging.exception(error)
            return '[×] 查看直营店-本地-直营型订单购物车清空失败_查看购物车失败-->%s' % error
        for cartitemid in shoppingCart_list:
            Del_ = Del(cartitemid['cartItemId'])
            if Del_[0] == '0':
                pass
            else:
                return '[×] 查看直营店-本地-直营型订单购物车清空失败_%s' % Del_[1]
        if len(See_shoppingCart().See_shoppingCart_5()[1]['data']['list']) == 0:
            return '查看直营店-本地-直营型订单购物车清空成功'
        else:
            return '[×] 查看直营店-本地-直营型订单购物车清空失败_%s' % len(See_shoppingCart().See_shoppingCart_5()[1]['data']['list'])

    # 清空加盟店-本地-三方型订单购物车
    def Delete_shoppingcartgoods_6(self):
        def Del(cartItemId):
            url = CONFIG.Url() + '/api/small/cart/deleteCartItem.jhtml'
            params = {'unionId': CONFIG.Unionid(),
                      'cartItemId': cartItemId  # 购物车货品id
                      }
            xx = requests.post(url, params)
            if xx.status_code == 200:
                if xx.json()['msg'] == '成功':
                    # print('', end='')
                    return '0', '成功'
                else:
                    return '1', '[×] 加盟店-本地-三方型订单购物车清空失败_%s'% xx.json()['msg']
            else:
                return '1', '[×] 加盟店-本地-三方型订单购物车清空失败_%s' % xx.status_code

        try:
            shoppingCart_list = See_shoppingCart().See_shoppingCart_6()[1]['data']['list']
        except Exception as error:
            # logging.exception(error)
            return '[×] 加盟店-本地-三方型订单购物车清空失败_查看购物车失败-->%s' % error
        for cartitemid in shoppingCart_list:
            Del_ = Del(cartitemid['cartItemId'])
            if Del_[0] == '0':
                pass
            else:
                return '[×] 加盟店-本地-三方型订单购物车清空失败_%s' % Del_[1]
        if len(See_shoppingCart().See_shoppingCart_6()[1]['data']['list']) == 0:
            return '加盟店-本地-三方型订单购物车清空成功'
        else:
            return '[×] 加盟店-本地-三方型订单购物车清空失败_%s' % len(See_shoppingCart().See_shoppingCart_6()[1]['data']['list'])

    # 清空直营店-本地-本地供应商订单购物车
    def Delete_shoppingcartgoods_7(self):
        def Del(cartItemId):
            url = CONFIG.Url() + '/api/small/cart/deleteCartItem.jhtml'
            params = {'unionId': CONFIG.Unionid(),
                      'cartItemId': cartItemId  # 购物车货品id
                      }
            xx = requests.post(url, params)
            if xx.status_code == 200:
                if xx.json()['msg'] == '成功':
                    # print('', end='')
                    return '0', '成功'
                else:
                    return '1', '[×] 直营店-本地-本地供应商订单购物车清空失败_%s'% xx.json()['msg']
            else:
                return '1', '[×] 直营店-本地-本地供应商订单购物车清空失败_%s' % xx.status_code

        try:
            shoppingCart_list = See_shoppingCart().See_shoppingCart_7()[1]['data']['list']
        except Exception as error:
            # logging.exception(error)
            return '[×] 直营店-本地-本地供应商订单购物车清空失败_查看购物车失败-->%s' % error
        for cartitemid in shoppingCart_list:
            Del_ = Del(cartitemid['cartItemId'])
            if Del_[0] == '0':
                pass
            else:
                return '[×] 直营店-本地-本地供应商订单购物车清空失败_%s' % Del_[1]
        if len(See_shoppingCart().See_shoppingCart_7()[1]['data']['list']) == 0:
            return '直营店-本地-本地供应商订单购物车清空成功'
        else:
            return '[×] 直营店-本地-本地供应商订单购物车清空失败_%s' % len(See_shoppingCart().See_shoppingCart_7()[1]['data']['list'])

    # 清空加盟店-本地-本地供应商订单购物车
    def Delete_shoppingcartgoods_8(self):
        def Del(cartItemId):
            url = CONFIG.Url() + '/api/small/cart/deleteCartItem.jhtml'
            params = {'unionId': CONFIG.Unionid(),
                      'cartItemId': cartItemId  # 购物车货品id
                      }
            xx = requests.post(url, params)
            if xx.status_code == 200:
                if xx.json()['msg'] == '成功':
                    # print('', end='')
                    return '0', '成功'
                else:
                    return '1', '[×] 加盟店-本地-本地供应商订单购物车清空失败_%s'% xx.json()['msg']
            else:
                return '1', '[×] 加盟店-本地-本地供应商订单购物车清空失败_%s' % xx.status_code

        try:
            shoppingCart_list = See_shoppingCart().See_shoppingCart_8()[1]['data']['list']
        except Exception as error:
            # logging.exception(error)
            return '[×] 加盟店-本地-本地供应商订单购物车清空失败_查看购物车失败-->%s' % error
        for cartitemid in shoppingCart_list:
            Del_ = Del(cartitemid['cartItemId'])
            if Del_[0] == '0':
                pass
            else:
                return '[×] 加盟店-本地-本地供应商订单购物车清空失败_%s' % Del_[1]
        if len(See_shoppingCart().See_shoppingCart_8()[1]['data']['list']) == 0:
            return '加盟店-本地-本地供应商订单购物车清空成功'
        else:
            return '[×] 加盟店-本地-本地供应商订单购物车清空失败_%s' % len(See_shoppingCart().See_shoppingCart_8()[1]['data']['list'])

# 购物车添加货品   # 待完善，增加校验，货品是否在购物车
class Add_shoppingCart:
    # 购物车添加货品(平台_自有直营_A-a)
    def Add_shoppingCart_1(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/add.jhtml'

        try:  # 异常处理，添加购物车时获取供应商参数时出现异常
            params = {'unionId': CONFIG.Unionid(),
                      'supplierId': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['id'],
                      'shopId': '3212',
                      'supplierType': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['supplierType'],
                      'relationId': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['relationId'],
                      'types': 'platform',
                      'supplyType': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['supplyType'],
                      'quantity': random.randint(1, 30),  # 在购物车中的数量
                      'productId': '29133',
                      }
        except Exception as error:
            # logging.exception(error)
            return '[×] 平台自有直营购物车添加货品失败_供应商参数获取异常-->%s' % error
        xx = requests.post(url, params)

        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                return '平台自有直营购物车货品添加成功'
            else:
                return '[×] 平台自有直营购物车货品添加失败-->msg: %s' % xx.json['msg']
        else:
            return '[×] 平台自有直营购物车货品添加失败-->状态码: %s' % xx.status_code

    # 购物车添加货品(平台_直营_A-B-b)
    def Add_shoppingCart_2(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/add.jhtml'

        try:  # 异常处理，添加购物车时获取供应商参数时出现异常
            params = {'unionId': CONFIG.Unionid(),
                      'supplierId': supplier.Supplier_id().Supplier_platform_zhiying()[0]['id'],
                      'shopId': '3212',
                      'supplierType': supplier.Supplier_id().Supplier_platform_zhiying()[0]['supplierType'],
                      'relationId': supplier.Supplier_id().Supplier_platform_zhiying()[0]['relationId'],
                      'types': 'platform',
                      'supplyType': supplier.Supplier_id().Supplier_platform_zhiying()[0]['supplyType'],
                      'quantity': random.randint(1, 30),  # 在购物车中的数量
                      'productId': '29134',
                      }
        except Exception as error:
            # logging.exception(error)
            return '[×] 平台直营购物车添加货品失败_供应商参数获取异常-->%s' % error
        xx = requests.post(url, params)

        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                return '平台直营购物车货品添加成功'
            else:
                return '[×] 平台直营购物车货品添加失败-->msg: %s' % xx.json['msg']
        else:
            return '[×] 平台直营购物车货品添加失败-->状态码: %s' % xx.status_code


    # 购物车添加货品(平台_加盟_A-b)
    def Add_shoppingCart_3(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/add.jhtml'

        try:  # 异常处理，添加购物车时获取供应商参数时出现异常
            params = {'unionId': CONFIG.Unionid(),
                      'supplierId': supplier.Supplier_id().Supplier_platform_sanfang()[0]['id'],
                      'shopId': '3214',  # 固定值,加盟店id
                      'supplierType': supplier.Supplier_id().Supplier_platform_sanfang()[0]['supplierType'],
                      'relationId': supplier.Supplier_id().Supplier_platform_sanfang()[0]['relationId'],
                      'types': 'platform',
                      'supplyType': supplier.Supplier_id().Supplier_platform_sanfang()[0]['supplyType'],
                      'quantity': random.randint(1, 30),  # 在购物车中的数量
                      'productId': '29140',
                      }
        except Exception as error:
            # logging.exception(error)
            return '[×] 平台加盟购物车添加货品失败_供应商参数获取异常-->%s' % error
        xx = requests.post(url, params)

        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                return '平台加盟购物车货品添加成功'
            else:
                return '[×] 平台加盟购物车货品添加失败-->msg: %s' % xx.json['msg']
        else:
            return '[×] 平台加盟购物车货品添加失败-->状态码: %s' % xx.status_code


    # 购物车添加货品(本地_自有直营_A-a)
    def Add_shoppingCart_4(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/add.jhtml'

        try:  # 异常处理，添加购物车时获取供应商参数时出现异常
            params = {'unionId': CONFIG.Unionid(),
                      'supplierId': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['id'],
                      'shopId': '3212',
                      'supplierType': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['supplierType'],
                      'relationId': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['relationId'],
                      'types': 'local',
                      'supplyType': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['supplyType'],
                      'quantity': random.randint(1, 30),  # 在购物车中的数量
                      'productId': '29133',
                      }
        except Exception as error:
            # logging.exception(error)
            return '[×] 本地自有直营购物车添加货品失败_供应商参数获取异常-->%s' % error
        xx = requests.post(url, params)

        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                return '本地自有直营购物车货品添加成功'
            else:
                return '[×] 本地自有直营购物车货品添加失败-->msg: %s' % xx.json['msg']
        else:
            return '[×] 本地自有直营购物车货品添加失败-->状态码: %s' % xx.status_code


    # 购物车添加货品(本地_直营_A-B-b)
    def Add_shoppingCart_5(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/add.jhtml'

        try:  # 异常处理，添加购物车时获取供应商参数时出现异常
            params = {'unionId': CONFIG.Unionid(),
                      'supplierId': supplier.Supplier_id().Supplier_local_zhiying()[0]['id'],
                      'shopId': '3212',
                      'supplierType': supplier.Supplier_id().Supplier_local_zhiying()[0]['supplierType'],
                      'relationId': supplier.Supplier_id().Supplier_local_zhiying()[0]['relationId'],
                      'types': 'local',
                      'supplyType': supplier.Supplier_id().Supplier_local_zhiying()[0]['supplyType'],
                      'quantity': random.randint(1, 30),  # 在购物车中的数量
                      'productId': '29134',
                      }
        except Exception as error:
            # logging.exception(error)
            return '[×] 本地直营购物车添加货品失败_供应商参数获取异常-->%s' % error
        xx = requests.post(url, params)

        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                return '本地直营购物车货品添加成功'
            else:
                return '[×] 本地直营购物车货品添加失败-->msg: %s' % xx.json['msg']
        else:
            return '[×] 本地直营购物车货品添加失败-->状态码: %s' % xx.status_code


    # 购物车添加货品(本地_加盟_A-b)
    def Add_shoppingCart_6(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/add.jhtml'

        try:  # 异常处理，添加购物车时获取供应商参数时出现异常
            params = {'unionId': CONFIG.Unionid(),
                      'supplierId': supplier.Supplier_id().Supplier_local_sanfang()[0]['id'],
                      'shopId': '3214',
                      'supplierType': supplier.Supplier_id().Supplier_local_sanfang()[0]['supplierType'],
                      'relationId': supplier.Supplier_id().Supplier_local_sanfang()[0]['relationId'],
                      'types': 'local',
                      'supplyType': supplier.Supplier_id().Supplier_local_sanfang()[0]['supplyType'],
                      'quantity': random.randint(1, 30),  # 在购物车中的数量
                      'productId': '29140',
                      }
        except Exception as error:
            # logging.exception(error)
            return '[×] 本地加盟购物车添加货品失败_供应商参数获取异常-->%s' % error
        xx = requests.post(url, params)

        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                return '本地加盟购物车货品添加成功'
            else:
                return '[×] 本地加盟购物车货品添加失败-->msg: %s' % xx.json['msg']
        else:
            return '[×] 本地加盟购物车货品添加失败-->状态码: %s' % xx.status_code


    # 购物车添加货品(本地_本地供应商_直营店)
    def Add_shoppingCart_7(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/add.jhtml'

        try:  # 异常处理，添加购物车时获取供应商参数时出现异常
            params = {'unionId': CONFIG.Unionid(),
                      'supplierId': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['id'],
                      'shopId': '3212',
                      'supplierType': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['supplierType'],
                      'relationId': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['relationId'],
                      'types': 'local',
                      'supplyType': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['supplyType'],
                      'quantity': random.randint(1, 30),  # 在购物车中的数量
                      'productId': '29225',
                      }
        except Exception as error:
            # logging.exception(error)
            return '[×] 本地直营店购物车添加货品失败_供应商参数获取异常-->%s' % error
        xx = requests.post(url, params)

        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                return '本地直营店购物车货品添加成功'
            else:
                return '[×] 本地直营店购物车货品添加失败-->msg: %s' % xx.json['msg']
        else:
            return '[×] 本地直营店购物车货品添加失败-->状态码: %s' % xx.status_code


    # 购物车添加货品(本地_本地供应商_加盟店)
    def Add_shoppingCart_8(self):
        login.Login()
        url = CONFIG.Url() + '/api/small/cart/add.jhtml'

        try:  # 异常处理，添加购物车时获取供应商参数时出现异常
            params = {'unionId': CONFIG.Unionid(),
                      'supplierId': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['id'],
                      'shopId': '3214',
                      'supplierType': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['supplierType'],
                      'relationId': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['relationId'],
                      'types': 'local',
                      'supplyType': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['supplyType'],
                      'quantity': random.randint(1, 30),  # 在购物车中的数量
                      'productId': '29225',
                      }
        except Exception as error:
            # logging.exception(error)
            return '[×] 本地加盟店购物车添加货品失败_供应商参数获取异常-->%s' % error
        xx = requests.post(url, params)

        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':
                return '本地加盟店购物车货品添加成功'
            else:
                return '[×] 本地加盟店购物车货品添加失败-->msg: %s' % xx.json['msg']
        else:
            return '[×] 本地加盟店购物车货品添加失败-->状态码: %s' % xx.status_code

# class Balance_shoppingCart:
#     login.Login()




if __name__ == '__main__':
        # pass
    print('\n**购物车添加**')

    print(Add_shoppingCart().Add_shoppingCart_1())
    print(Add_shoppingCart().Add_shoppingCart_2())
    print(Add_shoppingCart().Add_shoppingCart_3())
    print(Add_shoppingCart().Add_shoppingCart_4())
    print(Add_shoppingCart().Add_shoppingCart_5())
    print(Add_shoppingCart().Add_shoppingCart_6())
    print(Add_shoppingCart().Add_shoppingCart_7())
    print(Add_shoppingCart().Add_shoppingCart_8())
    #
    # print('\n**购物车查看**')
    #
    # print(See_shoppingCart().See_shoppingCart_1())
    # print(See_shoppingCart().See_shoppingCart_2())
    # print(See_shoppingCart().See_shoppingCart_3())
    # print(See_shoppingCart().See_shoppingCart_4())
    # print(See_shoppingCart().See_shoppingCart_5())
    # print(See_shoppingCart().See_shoppingCart_6())
    # print(See_shoppingCart().See_shoppingCart_7())
    # print(See_shoppingCart().See_shoppingCart_8())

    print('\n**购物车清空**')

    print(Delete_shoppingcartgoods().Delete_shoppingcartgoods_1())
    print(Delete_shoppingcartgoods().Delete_shoppingcartgoods_2())
    print(Delete_shoppingcartgoods().Delete_shoppingcartgoods_3())
    print(Delete_shoppingcartgoods().Delete_shoppingcartgoods_4())
    print(Delete_shoppingcartgoods().Delete_shoppingcartgoods_5())
    print(Delete_shoppingcartgoods().Delete_shoppingcartgoods_6())
    print(Delete_shoppingcartgoods().Delete_shoppingcartgoods_7())
    print(Delete_shoppingcartgoods().Delete_shoppingcartgoods_8())
