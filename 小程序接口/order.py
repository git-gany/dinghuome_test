
"""提交订单"""

import requests
import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import CONFIG
import supplier
import shoppingCart
import login
import DATA_BASE

class Submit:
    # 返回示例-->成功--> ('直营店-平台-自有直营型订单下单成功', {'code': '0', 'msg': '成功', 'requesturl': '', 'data': {···})
    #           失败--> [x] 直营店-平台-自有直营型订单下单失败_状态码:未知异常

    login.Login()

    # 直营店-平台-自有直营型订单
    def Order_1(self):
        try:
            add_goods = shoppingCart.Add_shoppingCart().Add_shoppingCart_1()
            if add_goods == '平台自有直营购物车货品添加成功':
                see_goods = shoppingCart.See_shoppingCart().See_shoppingCart_1()
                if len(see_goods[1]['data']['list']) > 0:
                    pass
                else:
                    return '[x] 直营店-平台-自有直营型订单下单失败_购物车为空'
            else:
                return '[x] 直营店-平台-自有直营型订单下单失败_购物车添加货品时出现异常_%s' % add_goods
        except Exception as error:
            return '[x] 直营店-平台-自有直营型订单下单失败_购物车添加货品时出现异常_%s' % shoppingCart.Add_shoppingCart().Add_shoppingCart_1()
        url = CONFIG.Url() + '/api/small/order/create.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['id'],
                  'shopId': '3212',
                  'supplierType': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['relationId'],
                  'types': 'platform',
                  'supplyType': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['supplyType'],
                  'reDate': '2019-01-24 00:00',
                  'reEndDate': '2019-01-24 02:00',
                  'memo': '我是备注我是备注，自动下单就是快啊'
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':

                orderid = xx.json()['data']['orderId']
                orderid_list = []
                try:
                    orders = See().PlatfromOrder()
                except Exception as error:
                    return '[x] 直营店-平台-自有直营型订单下单失败_订单列表获取失败-->%s' % error
                for orderid_ in orders:
                    orderid_list.append(orderid_['orderId'])
                if orderid in orderid_list:
                    return '直营店-平台-自有直营型订单下单成功', xx.json()
                else:
                    return '[x] 直营店-平台-自有直营型订单下单失败_订单列表未找到'

            else:
                return '[x] 直营店-平台-自有直营型订单下单失败_msg:%s' % xx.json()
        else:
            return '[x] 直营店-平台-自有直营型订单下单失败_状态码: %s' % xx.status_code

    # 直营店-平台-直营型订单
    def Order_2(self):
        try:
            add_goods = shoppingCart.Add_shoppingCart().Add_shoppingCart_2()
            if add_goods == '平台直营购物车货品添加成功':
                see_goods = shoppingCart.See_shoppingCart().See_shoppingCart_2()
                if len(see_goods[1]['data']['list']) > 0:
                    pass
                else:
                    return '[x] 直营店-平台-直营型订单下单失败_购物车为空'
            else:
                return '[x] 直营店-平台-直营型订单下单失败_购物车添加货品时出现异常_%s' % add_goods
        except Exception as error:
            return '[x] 直营店-平台-直营型订单下单失败_购物车添加货品时出现异常_%s' % shoppingCart.Add_shoppingCart().Add_shoppingCart_1()
        url = CONFIG.Url() + '/api/small/order/create.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_platform_zhiying()[0]['id'],
                  'shopId': '3212',
                  'supplierType': supplier.Supplier_id().Supplier_platform_zhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_platform_zhiying()[0]['relationId'],
                  'types': 'platform',
                  'supplyType': supplier.Supplier_id().Supplier_platform_zhiying()[0]['supplyType'],
                  'reDate': '2019-01-24 00:00',
                  'reEndDate': '2019-01-24 02:00',
                  'memo': '我是备注我是备注，自动下单就是快啊'
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':

                orderid = xx.json()['data']['orderId']
                orderid_list = []
                try:
                    orders = See().PlatfromOrder()
                except Exception as error:
                    return '[x] 直营店-平台-直营型订单下单失败_订单列表获取失败-->%s' % error
                for orderid_ in orders:
                    orderid_list.append(orderid_['orderId'])
                if orderid in orderid_list:
                    return '直营店-平台-直营型订单下单成功', xx.json()
                else:
                    return '[x] 直营店-平台-直营型订单下单失败_订单列表未找到'

            else:
                return '[x] 直营店-平台-直营型订单下单失败_msg:%s' % xx.json()
        else:
            return '[x] 直营店-平台-直营型订单下单失败_状态码异常: %s' % xx.status_code

    # 加盟店-平台-三方型订单
    def Order_3(self):
        try:
            add_goods = shoppingCart.Add_shoppingCart().Add_shoppingCart_3()
            if add_goods == '平台加盟购物车货品添加成功':
                see_goods = shoppingCart.See_shoppingCart().See_shoppingCart_3()
                if len(see_goods[1]['data']['list']) > 0:
                    pass
                else:
                    return '[x] 加盟店-平台-三方型订单下单失败_购物车为空'
            else:
                return '[x] 加盟店-平台-三方型订单下单失败_购物车添加货品时出现异常_%s' % add_goods
        except Exception as error:
            return '[x] 加盟店-平台-三方型订单下单失败_购物车添加货品时出现异常_%s' % shoppingCart.Add_shoppingCart().Add_shoppingCart_1()
        url = CONFIG.Url() + '/api/small/order/create.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_platform_sanfang()[0]['id'],
                  'shopId': '3214',
                  'supplierType': supplier.Supplier_id().Supplier_platform_sanfang()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_platform_sanfang()[0]['relationId'],
                  'types': 'platform',
                  'supplyType': supplier.Supplier_id().Supplier_platform_sanfang()[0]['supplyType'],
                  'reDate': '2019-01-24 00:00',
                  'reEndDate': '2019-01-24 02:00',
                  'memo': '我是备注我是备注，自动下单就是快啊'
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':

                orderid = xx.json()['data']['orderId']
                orderid_list = []
                try:
                    orders = See().PlatfromOrder()
                except Exception as error:
                    return '[x] 加盟店-平台-三方型订单下单失败_订单列表获取失败-->%s' % error
                for orderid_ in orders:
                    orderid_list.append(orderid_['orderId'])
                if orderid in orderid_list:
                    return '加盟店-平台-三方型订单下单成功', xx.json()
                else:
                    return '[x] 加盟店-平台-三方型订单下单失败_订单列表未找到'

            else:
                return '[x] 加盟店-平台-三方型订单下单失败_msg:%s' % xx.json()
        else:
            return '[x] 加盟店-平台-三方型订单下单失败_状态码异常: %s' % xx.status_code

    # 直营店-本地-自有直营型订单
    def Order_4(self):
        try:
            add_goods = shoppingCart.Add_shoppingCart().Add_shoppingCart_4()
            if add_goods == '本地自有直营购物车货品添加成功':
                see_goods = shoppingCart.See_shoppingCart().See_shoppingCart_4()
                if len(see_goods[1]['data']['list']) > 0:
                    pass
                else:
                    return '[x] 直营店-本地-自有直营型订单下单失败_购物车为空'
            else:
                return '[x] 直营店-本地-自有直营型订单下单失败_购物车添加货品时出现异常_%s' % add_goods
        except Exception as error:
            return '[x] 直营店-本地-自有直营型订单下单失败_购物车添加货品时出现异常_%s' % shoppingCart.Add_shoppingCart().Add_shoppingCart_1()
        url = CONFIG.Url() + '/api/small/order/create.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['id'],
                  'shopId': '3212',
                  'supplierType': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['relationId'],
                  'types': 'local',
                  'supplyType': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['supplyType'],
                  'reDate': '2019-01-24 00:00',
                  'reEndDate': '2019-01-24 02:00',
                  'memo': '我是备注我是备注，自动下单就是快啊'
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':

                orderid = xx.json()['data']['orderId']
                orderid_list = []
                try:
                    orders = See().LocalOrder()
                except Exception as error:
                    return '[x] 直营店-本地-自有直营型订单下单失败_订单列表获取失败-->%s' % error
                for orderid_ in orders:
                    orderid_list.append(orderid_['orderId'])
                if orderid in orderid_list:
                    return '直营店-本地-自有直营型订单下单成功', xx.json()
                else:
                    return '[x] 直营店-本地-自有直营型订单下单失败_订单列表未找到'

            else:
                return '[x] 直营店-本地-自有直营型订单下单失败_msg:%s' % xx.json()
        else:
            return '[x] 直营店-本地-自有直营型订单下单失败_状态码异常: %s' % xx.status_code

    # 直营店-本地-直营型订单
    def Order_5(self):
        try:
            add_goods = shoppingCart.Add_shoppingCart().Add_shoppingCart_5()
            if add_goods == '本地直营购物车货品添加成功':
                see_goods = shoppingCart.See_shoppingCart().See_shoppingCart_5()
                if len(see_goods[1]['data']['list']) > 0:
                    pass
                else:
                    return '[x] 直营店-本地-直营型订单下单失败_购物车为空'
            else:
                return '[x] 直营店-本地-直营型订单下单失败_购物车添加货品时出现异常_%s' % add_goods
        except Exception as error:
            return '[x] 直营店-本地-直营型订单下单失败_购物车添加货品时出现异常_%s' % shoppingCart.Add_shoppingCart().Add_shoppingCart_1()
        url = CONFIG.Url() + '/api/small/order/create.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_local_zhiying()[0]['id'],
                  'shopId': '3212',
                  'supplierType': supplier.Supplier_id().Supplier_local_zhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_zhiying()[0]['relationId'],
                  'types': 'local',
                  'supplyType': supplier.Supplier_id().Supplier_local_zhiying()[0]['supplyType'],
                  'reDate': '2019-01-24 00:00',
                  'reEndDate': '2019-01-24 02:00',
                  'memo': '我是备注我是备注，自动下单就是快啊'
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':

                orderid = xx.json()['data']['orderId']
                orderid_list = []
                try:
                    orders = See().LocalOrder()
                except Exception as error:
                    return '[x] 直营店-本地-直营型订单下单失败_订单列表获取失败-->%s' % error
                for orderid_ in orders:
                    orderid_list.append(orderid_['orderId'])
                if orderid in orderid_list:
                    return '直营店-本地-直营型订单下单成功', xx.json()
                else:
                    return '[x] 直营店-本地-直营型订单下单失败_订单列表未找到'

            else:
                return '[x] 直营店-本地-直营型订单下单失败_msg:%s' % xx.json()
        else:
            return '[x] 直营店-本地-直营型订单下单失败_状态码异常: %s' % xx.status_code

    # 加盟店-本地-三方型订单
    def Order_6(self):
        try:
            add_goods = shoppingCart.Add_shoppingCart().Add_shoppingCart_6()
            if add_goods == '本地加盟购物车货品添加成功':
                see_goods = shoppingCart.See_shoppingCart().See_shoppingCart_6()
                if len(see_goods[1]['data']['list']) > 0:
                    pass
                else:
                    return '[x] 加盟店-本地-三方型订单下单失败_购物车为空'
            else:
                return '[x] 加盟店-本地-三方型订单下单失败_购物车添加货品时出现异常_%s' % add_goods
        except Exception as error:
            return '[x] 加盟店-本地-三方型订单下单失败_购物车添加货品时出现异常_%s' % shoppingCart.Add_shoppingCart().Add_shoppingCart_1()
        url = CONFIG.Url() + '/api/small/order/create.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_local_sanfang()[0]['id'],
                  'shopId': '3214',
                  'supplierType': supplier.Supplier_id().Supplier_local_sanfang()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_sanfang()[0]['relationId'],
                  'types': 'local',
                  'supplyType': supplier.Supplier_id().Supplier_local_sanfang()[0]['supplyType'],
                  'reDate': '2019-01-24 00:00',
                  'reEndDate': '2019-01-24 02:00',
                  'memo': '我是备注我是备注，自动下单就是快啊'
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':

                orderid = xx.json()['data']['orderId']
                orderid_list = []
                try:
                    orders = See().LocalOrder()
                except Exception as error:
                    return '[x] 加盟店-本地-三方型订单下单失败_订单列表获取失败-->%s' % error
                for orderid_ in orders:
                    orderid_list.append(orderid_['orderId'])
                if orderid in orderid_list:
                    return '加盟店-本地-三方型订单下单成功', xx.json()
                else:
                    return '[x] 加盟店-本地-三方型订单下单失败_订单列表未找到'

            else:
                return '[x] 加盟店-本地-三方型订单下单失败_msg:%s' % xx.json()
        else:
            return '[x] 加盟店-本地-三方型订单下单失败_状态码异常: %s' % xx.status_code

    # 直营店-本地-本地供应商订单
    def Order_7(self):
        try:
            add_goods = shoppingCart.Add_shoppingCart().Add_shoppingCart_7()
            if add_goods == '本地直营店购物车货品添加成功':
                see_goods = shoppingCart.See_shoppingCart().See_shoppingCart_7()
                if len(see_goods[1]['data']['list']) > 0:
                    pass
                else:
                    return '[x] 直营店-本地-本地供应商订单下单失败_购物车为空'
            else:
                return '[x] 直营店-本地-本地供应商订单下单失败_购物车添加货品时出现异常_%s' % add_goods
        except Exception as error:
            return '[x] 直营店-本地-本地供应商订单下单失败_购物车添加货品时出现异常_%s' % shoppingCart.Add_shoppingCart().Add_shoppingCart_1()
        url = CONFIG.Url() + '/api/small/order/create.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_local_zhiying_shop()[0]['id'],
                  'shopId': '3212',
                  'supplierType': supplier.Supplier_id().Supplier_local_zhiying_shop()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_zhiying_shop()[0]['relationId'],
                  'types': 'local',
                  'supplyType': supplier.Supplier_id().Supplier_local_zhiying_shop()[0]['supplyType'],
                  'reDate': '2019-01-24 00:00',
                  'reEndDate': '2019-01-24 02:00',
                  'memo': '我是备注我是备注，自动下单就是快啊'
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':

                orderid = xx.json()['data']['orderId']
                orderid_list = []
                try:
                    orders = See().LocalOrder()
                except Exception as error:
                    return '[x] 直营店-本地-本地供应商订单下单失败_订单列表获取失败-->%s' % error
                for orderid_ in orders:
                    orderid_list.append(orderid_['orderId'])
                if orderid in orderid_list:
                    return '直营店-本地-本地供应商订单下单成功', xx.json()
                else:
                    return '[x] 直营店-本地-本地供应商订单下单失败_订单列表未找到'

            else:
                return '[x] 直营店-本地-本地供应商订单下单失败_msg:%s' % xx.json()
        else:
            return '[x] 直营店-本地-本地供应商订单下单失败_状态码异常: %s' % xx.status_code

    # 加盟店-本地-本地供应商订单
    def Order_8(self):
        try:
            add_goods = shoppingCart.Add_shoppingCart().Add_shoppingCart_8()
            if add_goods == '本地加盟店购物车货品添加成功':
                see_goods = shoppingCart.See_shoppingCart().See_shoppingCart_8()
                if len(see_goods[1]['data']['list']) > 0:
                    pass
                else:
                    return '[x] 加盟店-本地-本地供应商订单下单失败_购物车为空'
            else:
                return '[x] 加盟店-本地-本地供应商订单下单失败_购物车添加货品时出现异常_%s' % add_goods
        except Exception as error:
            return '[x] 加盟店-本地-本地供应商订单下单失败_购物车添加货品时出现异常_%s' % shoppingCart.Add_shoppingCart().Add_shoppingCart_1()
        url = CONFIG.Url() + '/api/small/order/create.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'supplierId': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['id'],
                  'shopId': '3214',
                  'supplierType': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['relationId'],
                  'types': 'local',
                  'supplyType': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['supplyType'],
                  'reDate': '2019-01-24 00:00',
                  'reEndDate': '2019-01-24 02:00',
                  'memo': '我是备注我是备注，自动下单就是快啊'
                  }
        xx = requests.get(url, params)
        if xx.status_code == 200:
            if xx.json()['msg'] == '成功':

                orderid = xx.json()['data']['orderId']
                orderid_list = []
                try:
                    orders = See().LocalOrder()
                except Exception as error:
                    return '[x] 加盟店-本地-本地供应商订单下单失败_订单列表获取失败-->%s' % error
                for orderid_ in orders:
                    orderid_list.append(orderid_['orderId'])
                if orderid in orderid_list:
                    return '加盟店-本地-本地供应商订单下单成功', xx.json()
                else:
                    return '[x] 加盟店-本地-本地供应商订单下单失败_订单列表未找到'

            else:
                return '[x] 加盟店-本地-本地供应商订单下单失败_msg:%s' % xx.json()
        else:
            return '[x] 加盟店-本地-本地供应商订单下单失败_状态码异常: %s' % xx.status_code

class See:

    login.Login()

    def PlatfromOrder(self):
        url = CONFIG.Url() + '/api/small/order/orderList.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'searchProperty': 'sn',  # ??
                  'searchValue': '',  # 搜索时传入订单号
                  'status': '',  # 订单状态tab
                  'pageNumber': 1,  # 分页，可不填，默认为1
                  'pageSize': 20  # 分页显示的条数，可不填，默认为10
                  }
        xx = requests.get(url, params)
        return xx.json()['data']['orders']


    def LocalOrder(self):
        url = CONFIG.Url() + '/api/small/order/localOrderList.jhtml'
        params = {'unionId': CONFIG.Unionid(),
                  'searchProperty': 'sn',  # ??
                  'searchValue': '',  # 搜索时传入订单号
                  'status': '',  # 订单状态tab
                  'pageNumber': 1,  # 分页，可不填，默认为1
                  'pageSize': 20  # 分页显示的条数，可不填，默认为10
                  }
        xx = requests.get(url, params)
        return xx.json()['data']['orders']


#  测试
if __name__ == '__main__':
    pass
    # print(Submit().Order_1())
    # print(Submit().Order_2())
    # print(Submit().Order_3())
    # print(Submit().Order_4())
    # print(Submit().Order_5())
    # print(Submit().Order_6())
    # print(Submit().Order_7())
    print(Submit().Order_8())

if __name__ == '__main__':
    pass
    print(See().PlatfromOrder())
    print(See().LocalOrder())

