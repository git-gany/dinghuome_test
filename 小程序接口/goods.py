
"""获取货品列表"""

import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import requests
import supplier
import CONFIG

# 平台-直营门店-自有直营企业 货品列表
def Goods_platform_zhiying_shop_ziyouzhiying():
    url = CONFIG.Url()+'/api/small/supplier/getAssignGoods.jhtml'
    try:
        params = {'supplierId': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['id'],
                  'shopId': '3212',# 直营店(接口)，写死项
                  'supplierType': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_platform_ziyouzhiying()[0]['relationId'], # 门店与自有直营企业的供应id
                  'goodsName': '', # 货品名称，空则为所有
                  'productCategoryId': '', # 分类id，空则为所有
                  'pageSize': '1000',
                  'pageNumber': '1',
                  'unionId': CONFIG.Unionid()
                  }
    except Exception as error:
        return '[×] [平台-直营门店-自有直营企业 货品列表获取异常]-->前置参数获取异常-->门店及企业id获取异常-->%s'% error
    request = requests.get(url, params)
    if request.status_code != 200:
        return '[×] %s 平台-直营门店-自有直营企业 货品列表获取异常' % request.status_code
    else:
        if request.json()['msg'] != '成功':
            return '[×] %s 平台-直营门店-自有直营企业 货品列表获取异常' % request.json()
        else:
            goods_list = []
            for goods in request.json()['data']['data']:
                goods_list.append(goods)
            return '自有直营型货品列表获取成功', len(goods_list), goods_list

# 平台-直营门店-直营企业 货品列表
def Goods_platform_zhiying_shop_zhiyin():
    url = CONFIG.Url()+'/api/small/supplier/getAssignGoods.jhtml'
    try:
        params = {'supplierId': supplier.Supplier_id().Supplier_platform_zhiying()[0]['id'],# 注意，此处的0只是暂时，若有多个直营关系，此处需处理
                  'shopId': '3212',# 直营店(接口)，写死项
                  'supplierType': supplier.Supplier_id().Supplier_platform_zhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_platform_zhiying()[0]['relationId'],
                  'goodsName': '', # 货品名称，空则为所有
                  'productCategoryId': '', # 分类id，空则为所有
                  'pageSize': '1000',
                  'pageNumber': '1',
                  'unionId': CONFIG.Unionid()
                  }
    except Exception as error:
        return '[×] [平台-直营门店-直营企业 货品列表获取异常]-->前置参数获取异常-->门店及企业id获取异常-->%s'% error
    request = requests.get(url, params)
    if request.status_code != 200:
        return '[×] %s 平台-直营门店-直营企业 货品列表获取异常'%request.status_code
    else:
        if request.json()['msg'] != '成功':
            return '[×] %s 平台-直营门店-直营企业 货品列表获取异常'%request.json()
        else:
            goods_list = []
            for goods in request.json()['data']['data']:
                goods_list.append(goods)
            return '直营型货品列表获取成功', len(goods_list), goods_list

# 平台-加盟门店-三方企业 货品列表
def Goods_platform_jiameng_shop_sanfang():
    url = CONFIG.Url()+'/api/small/supplier/getAssignGoods.jhtml'
    try:
        params = {'supplierId': supplier.Supplier_id().Supplier_platform_sanfang()[0]['id'],# 注意，此处的0只是暂时，若有多个直营关系，此处需处理
              'shopId': '3214',# 加盟(接口)，写死项
              'supplierType': supplier.Supplier_id().Supplier_platform_sanfang()[0]['supplierType'],
              'relationId': supplier.Supplier_id().Supplier_platform_sanfang()[0]['relationId'],
              'goodsName': '', # 货品名称，空则为所有
              'productCategoryId': '', # 分类id，空则为所有
              'pageSize': '1000',
              'pageNumber': '1',
              'unionId': CONFIG.Unionid()
              }
    except Exception as error:
        return '[×] [平台-加盟门店-三方企业 货品列表]-->前置参数获取异常-->门店及企业id获取异常-->%s'% error
    request = requests.get(url, params)
    if request.status_code != 200:
        return '[×] %s 平台-加盟门店-三方企业 货品列表获取异常'%request.status_code
    else:
        if request.json()['msg'] != '成功':
            return '[×] %s 平台-加盟门店-三方企业 货品列表获取异常'%request.json()
        else:
            goods_list = []
            for goods in request.json()['data']['data']:
                goods_list.append(goods)
            return '平台-加盟门店-三方企业 货品列表获取成功', len(goods_list), goods_list

# 本地-直营门店-自有直营企业 货品列表
def Goods_local_zhiying_shop_ziyouzhiying():
    url = CONFIG.Url()+'/api/small/supplier/getAssignGoods.jhtml'
    try:
        params = {'supplierId': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['id'],# 注意，此处的0只是暂时，若有多个直营关系，此处需处理
                  'shopId': '3212',# 直营店(接口)，写死项
                  'supplierType': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_ziyouzhiying()[0]['relationId'],
                  'goodsName': '', # 货品名称，空则为所有
                  'productCategoryId': '', # 分类id，空则为所有
                  'pageSize': '1000',
                  'pageNumber': '1',
                  'unionId': CONFIG.Unionid()
                  }
    except Exception as error:
        return '[×] [本地-直营门店-自有直营企业 货品列表]-->前置参数获取异常-->门店及企业id获取异常-->%s'% error
    request = requests.get(url, params)
    if request.status_code != 200:
        return '[×] %s 本地-直营门店-自有直营企业 货品列表获取异常'%request.status_code
    else:
        if request.json()['msg'] != '成功':
            return '[×] %s 本地-直营门店-自有直营企业 货品列表获取异常'%request.json()
        else:
            goods_list = []
            for goods in request.json()['data']['data']:
                goods_list.append(goods)
            return '本地-直营门店-自有直营企业 货品列表获取成功', {'数量': len(goods_list)}, {'货品列表': goods_list}

# 本地-直营门店-直营企业 货品列表
def Goods_local_zhiying_shop_zhiying():
    url = CONFIG.Url()+'/api/small/supplier/getAssignGoods.jhtml'
    try:
        params = {'supplierId': supplier.Supplier_id().Supplier_local_zhiying()[0]['id'],# 注意，此处的0只是暂时，若有多个直营关系，此处需处理
                  'shopId': '3212',# 直营店(接口)，写死项
                  'supplierType': supplier.Supplier_id().Supplier_local_zhiying()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_zhiying()[0]['relationId'],
                  'goodsName': '', # 货品名称，空则为所有
                  'productCategoryId': '', # 分类id，空则为所有
                  'pageSize': '1000',
                  'pageNumber': '1',
                  'unionId': CONFIG.Unionid()
                  }
    except Exception as error:
        return '[×] [本地-直营门店-直营企业 货品列表]-->前置参数获取异常-->门店及企业id获取异常_errorlog-->%s' % error
    request = requests.get(url, params)
    if request.status_code != 200:
        return '[×] %s 本地-直营门店-直营企业 货品列表获取异常'%request.status_code
    else:
        if request.json()['msg'] != '成功':
            return '[×] %s 本地-直营门店-直营企业 货品列表获取异常'%request.json()
        else:
            goods_list = []
            for goods in request.json()['data']['data']:
                goods_list.append(goods)
            return '本地-直营门店-直营企业 货品列表获取成功', {'数量': len(goods_list)}, {'货品列表': goods_list}

# 本地-加盟门店-三方企业 货品列表
def Goods_local_jiameng_shop_sanfang():
    url = CONFIG.Url()+'/api/small/supplier/getAssignGoods.jhtml'
    try:
        params = {'supplierId': supplier.Supplier_id().Supplier_local_sanfang()[0]['id'],# 注意，此处的0只是暂时，若有多个直营关系，此处需处理
                  'shopId': '3214',# 加盟(接口)，写死项
                  'supplierType': supplier.Supplier_id().Supplier_local_sanfang()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_sanfang()[0]['relationId'],
                  'goodsName': '', # 货品名称，空则为所有
                  'productCategoryId': '', # 分类id，空则为所有
                  'pageSize': '1000',
                  'pageNumber': '1',
                  'unionId': CONFIG.Unionid()
                  }
    except Exception as error:
        return '[×] [本地-加盟门店-三方企业 货品列表]-->前置参数获取异常-->门店及企业id获取异常-->%s'% error
    request = requests.get(url, params)
    if request.status_code != 200:
        return '[×] %s 本地-加盟门店-三方企业 货品列表获取异常'%request.status_code
    else:
        if request.json()['msg'] != '成功':
            return '[×] %s 本地-加盟门店-三方企业 货品列表获取异常'%request.json()
        else:
            goods_list = []
            for goods in request.json()['data']['data']:
                goods_list.append(goods)
            return '本地-加盟门店-三方企业 货品列表获取成功', {'数量': len(goods_list)}, {'货品列表': goods_list}

# 本地-直营门店-本地供应商 货品列表
def Goods_local_zhiying_shop():
    url = CONFIG.Url()+'/api/small/supplier/getAssignGoods.jhtml'
    try:
        params = {'supplierId': supplier.Supplier_id().Supplier_local_zhiying_shop()[0]['id'],# 注意，此处的0只是暂时，若有多个直营关系，此处需处理
                  'shopId': '3212',# 直营店(接口)，写死项
                  'supplierType': supplier.Supplier_id().Supplier_local_zhiying_shop()[0]['supplierType'],
                  'relationId': supplier.Supplier_id().Supplier_local_zhiying_shop()[0]['relationId'],
                  'goodsName': '', # 货品名称，空则为所有
                  'productCategoryId': '', # 分类id，空则为所有
                  'pageSize': '1000',
                  'pageNumber': '1',
                  'unionId': CONFIG.Unionid()
                  }
    except Exception as error:
        return '[×] [本地-直营门店-本地供应商 货品列表]-->前置参数获取异常-->门店及企业id获取异常-->%s'% error
    request = requests.get(url, params)
    if request.status_code != 200:
        return '[×] %s 本地-直营门店-本地供应商 货品列表获取异常'%request.status_code
    else:
        if request.json()['msg'] != '成功':
            return '[×] %s 本地-直营门店-本地供应商 货品列表获取异常'%request.json()
        else:
            goods_list = []
            for goods in request.json()['data']['data']:
                goods_list.append(goods)
            return '本地-直营门店-本地供应商 货品列表获取成功', {'数量': len(goods_list)}, {'货品列表': goods_list}

# 本地-加盟门店-本地供应商 货品列表
def Goods_local_jiameng_shop():
    url = CONFIG.Url()+'/api/small/supplier/getAssignGoods.jhtml'
    try:
        params = {'supplierId': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['id'],# 注意，此处的0只是暂时，若有多个直营关系，此处需处理
              'shopId': '3214',# 加盟(接口)，写死项
              'supplierType': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['supplierType'],
              'relationId': supplier.Supplier_id().Supplier_local_jiameng_shop()[0]['relationId'],
              'goodsName': '', # 货品名称，空则为所有
              'productCategoryId': '', # 分类id，空则为所有
              'pageSize': '1000',
              'pageNumber': '1',
              'unionId': CONFIG.Unionid()
              }
    except Exception as error:
        return '[×] [本地-加盟门店-本地供应商 货品列表]-->前置参数获取异常-->门店及企业id获取异常-->%s'% error
    request = requests.get(url, params)
    if request.status_code != 200:
        return '[×] %s 本地-加盟门店-本地供应商获取异常'%request.status_code
    else:
        if request.json()['msg'] != '成功':
            return '[×] %s 本地-加盟门店-本地供应商获取异常'%request.json()
        else:
            goods_list = []
            for goods in request.json()['data']['data']:
                goods_list.append(goods)
            return '本地-加盟门店-本地供应商 货品列表获取成功', {'数量': len(goods_list)}, {'货品列表': goods_list}

if __name__ == '__main__':
    print('平台-直营门店-自有直营企业 货品列表', Goods_platform_zhiying_shop_ziyouzhiying())
    # print('平台-直营门店-直营企业 货品列表', Goods_platform_zhiying_shop_zhiyin())
    # print('平台-加盟门店-三方企业 货品列表', Goods_platform_jiameng_shop_sanfang())
    # print('本地-直营门店-自有直营企业 货品列表', Goods_local_zhiying_shop_ziyouzhiying())
    # print('本地-直营门店-直营企业 货品列表', Goods_local_zhiying_shop_zhiying())
    # print('本地-加盟门店-三方企业 货品列表', Goods_local_jiameng_shop_sanfang())
    # print('本地-直营门店-本地供应商 货品列表', Goods_local_zhiying_shop())
    # print('本地-加盟门店-本地供应商 货品列表', Goods_local_jiameng_shop())

