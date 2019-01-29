
"""获取supplier信息(门店id为固定值)"""

import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import requests
import CONFIG

class Supplier_list():

    # 返回示例-->成功：{'supplierType': 'ONE', 'id': 1888, 'name': '_自动化接口测试企业_', 'supplyType': 'temporary', 'relationId': 15110}, {'supplierType': 'TWO', 'id': 1898, 'name': '_自动化接口测试企业1_', 'supplyType': 'formal', 'relationId': 759}
    #           失败：[×] 404 平台直营门店企业获取异常

    # 获取平台直营门店企业列表
    def Supplier_platform_zhiying(self):
        url = CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3212',  # 直营店(接口用)
                  'types': 'platform'
                  }
        request = requests.get(url, params)
        # return request.json()
        if request.status_code != 200:
            return '[×] %s 平台直营门店企业获取异常'%request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '[×] %s 平台直营门店企业获取异常'%request.json()
            else:
                supplier = []
                for s in request.json()['data']:
                    supplier.append(s)
        return '平台直营门店企业列表获取成功', supplier

    # 获取平台加盟门店企业列表
    def Supplier_platform_jiameng(self):
        url =  CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3214', # 直营店(接口用)
                  'types': 'platform'
                  }
        request = requests.get(url, params)
        # return request.json()
        if request.status_code != 200:
            return '[×] %s 平台加盟门店企业获取异常'%request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '[×] %s 平台加盟门店企业获取异常'%request.json()
            else:
                supplier = []
                for s in request.json()['data']:
                    supplier.append(s)
        return '平台加盟门店企业列表获取成功', supplier

    # 获取本地直营门店企业列表
    def Supplier_local_zhiying(self):
        url =  CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3212', # 直营店(接口用)
                  'types': 'local'
                  }
        request = requests.get(url, params)
        # return request.json()
        if request.status_code != 200:
            return '[×] 本地直营门店企业列表获取失败, %s' % request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '[×] 本地直营门店企业列表获取失败, %s' % request.json()
            else:
                supplier = []
                for s in request.json()['data']:
                    supplier.append(s)
        return '本地直营门店企业列表获取成功', supplier

    # 获取本地加盟门店企业列表
    def Supplier_local_jiameng(self):
        url =  CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3214', # 直营店(接口用)
                  'types': 'local'
                  }
        request = requests.get(url, params)
        # return request.json()
        if request.status_code != 200:
            return '[×] 本地加盟门店企业列表获取失败, %s' % request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '[×] 本地加盟门店企业列表获取失败, %s' % request.json()
            else:
                supplier = []
                for s in request.json()['data']:
                    supplier.append(s)
        return '本地加盟门店企业列表获取成功', supplier

# 获取商品列表处，返回相应供应商id，
class Supplier_id():
    # ONE 自有直营
    # TWO 直营
    # THREE 三方
    # 返回示例-->成功：{'supplierType': 'ONE', 'id': 1888, 'name': '_自动化接口测试企业_', 'supplyType': 'temporary', 'relationId': 15110}
    #           失败：404 企业信息获取失败

    # 获取平台自有直营供应商id
    def Supplier_platform_ziyouzhiying(self):
        url = CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3212',  # 直营店(接口用)
                  'types': 'platform'
                  }
        request = requests.get(url, params)
        if request.status_code != 200:
            return '%s 企业信息获取失败'%request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '%s 企业信息获取失败'%request.json()
            else:
                supplier = [] # 自有直营供应商列表
                for s in request.json()['data']:
                    if s['supplierType'] == 'ONE': # 自有直营
                        supplier.append(s)
                    else:
                        continue
        return supplier

    # 获取平台直营供应商id
    def Supplier_platform_zhiying(self):
        url = CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3212', # 直营店(接口用)
                  'types': 'platform'
                  }
        request = requests.get(url, params)
        if request.status_code != 200:
            return '%s 企业信息获取失败'%request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '%s 企业信息获取失败'%request.json()
            else:
                supplier = [] # 自有直营供应商列表
                for s in request.json()['data']:
                    if s['supplierType'] == 'TWO': # 自有直营
                        supplier.append(s)
                    else:
                        continue
        return supplier

    # 获取平台三方供应商id
    def Supplier_platform_sanfang(self):
        url = CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3214', # 加盟店(接口用)
                  'types': 'platform'
                  }
        request = requests.get(url, params)
        if request.status_code != 200:
            return '%s 企业信息获取失败'%request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '%s 企业信息获取失败'%request.json()
            else:
                supplier = [] # 自有直营供应商列表
                for s in request.json()['data']:
                    if s['supplierType'] == 'THREE': # 自有直营
                        supplier.append(s)
                    else:
                        continue
        return supplier

    # 获取本地自有直营供应商id
    def Supplier_local_ziyouzhiying(self):
        url = CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3212', # 直营店(接口用)
                  'types': 'local'
                  }
        request = requests.get(url, params)
        if request.status_code != 200:
            return '%s 企业信息获取失败'%request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '%s 企业信息获取失败'%request.json()
            else:
                supplier = [] # 自有直营供应商列表
                for s in request.json()['data']:
                    if s['supplierType'] == 'ONE': # 自有直营
                        supplier.append(s)
                    else:
                        continue
        return supplier

    # 获取本地直营供应商id
    def Supplier_local_zhiying(self):
        url = CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3212', # 直营店(接口用)
                  'types': 'local'
                  }
        request = requests.get(url, params)
        if request.status_code != 200:
            return '%s 企业信息获取失败'%request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '%s 企业信息获取失败'%request.json()
            else:
                supplier = [] # 自有直营供应商列表
                for s in request.json()['data']:
                    if s['supplierType'] == 'TWO': # 自有直营
                        supplier.append(s)
                    else:
                        continue
        return supplier

    # 获取本地三方供应商id
    def Supplier_local_sanfang(self):
        url = CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3214', # 加盟店(接口用)
                  'types': 'local'
                  }
        request = requests.get(url, params)
        if request.status_code != 200:
            return '%s 企业信息获取失败'%request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '%s 企业信息获取失败'%request.json()
            else:
                supplier = [] # 自有直营供应商列表
                for s in request.json()['data']:
                    if s['supplierType'] == 'THREE': # 自有直营
                        supplier.append(s)
                    else:
                        continue
        return supplier

    # 获取直营店本地供应商id
    def Supplier_local_zhiying_shop(self):
        url = CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3212', # 直营店(接口用)
                  'types': 'local'
                  }
        request = requests.get(url, params)
        if request.status_code != 200:
            return '%s 企业信息获取失败'%request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '%s 企业信息获取失败'%request.json()
            else:
                supplier = [] # 自有直营供应商列表
                for s in request.json()['data']:
                    if s['supplierType'] == 'FOUR': # 自有直营
                        supplier.append(s)
                    else:
                        continue
        return supplier

    # 获取加盟店本地供应商id
    def Supplier_local_jiameng_shop(self):
        url = CONFIG.Url() + '/api/small/supplier/getAssignSupplier.jhtml'
        params = {'shopId': '3214', # 加盟店(接口用)
                  'types': 'local'
                  }
        request = requests.get(url, params)
        if request.status_code != 200:
            return '%s 企业信息获取失败'%request.status_code
        else:
            if request.json()['msg'] != '成功':
                return '%s 企业信息获取失败'%request.json()
            else:
                supplier = [] # 自有直营供应商列表
                for s in request.json()['data']:
                    if s['supplierType'] == 'FOUR': # 自有直营
                        supplier.append(s)
                    else:
                        continue
        return supplier

if __name__ == '__main__':
    print(Supplier_list().Supplier_platform_zhiying())
    print(Supplier_list().Supplier_platform_jiameng())
    print(Supplier_list().Supplier_local_zhiying())
    print(Supplier_list().Supplier_local_jiameng())

# if __name__ == '__main__':
#     print('平台自有直营供应商', Supplier_id().Supplier_platform_ziyouzhiying())
    # print('平台直营供应商', Supplier_id().Supplier_platform_zhiying())
    # print('平台三方供应商', Supplier_id().Supplier_platform_sanfang())
    # print('本地自有直营供应商', Supplier_id().Supplier_local_ziyouzhiying())
    # print('本地直营供应商', Supplier_id().Supplier_local_zhiying())
    # print('本地三方供应商', Supplier_id().Supplier_local_sanfang())
    # print('直营店本地供应商', Supplier_id().Supplier_local_zhiying_shop())
    # print('加盟店本地供应商', Supplier_id().Supplier_local_jiameng_shop())
