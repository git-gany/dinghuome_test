
"""获取餐厅列表接口"""

import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import requests
import login
import CONFIG

# 获取直营门店id
def View_shop_direct():
    login.Login()
    url = CONFIG.Url() + '/api/small/shop/list.jhtml'
    params = {'unionId': CONFIG.Unionid(),
              'pageSize': '1000',
              'pageNumber': '1'}
    request_view_shop_id = requests.get(url, params)
    if request_view_shop_id.status_code != 200:
        return '%s门店信息获取失败'%request_view_shop_id.status_code
    else:
        if request_view_shop_id.json()['msg'] != '成功':
            return '%s门店信息获取失败' % request_view_shop_id.json()
        else:
            shop = []
            for s in request_view_shop_id.json()['data']['list']:
                if s['shopType'] == 'direct':
                    shop.append((s['id'], s['name']))
                else:
                    continue
            return '门店列表直营门店获取成功', shop

# 获取加盟店id
def View_shop_affiliate():
    login.Login()
    url = CONFIG.Url() + '/api/small/shop/list.jhtml'
    params = {'unionId': CONFIG.Unionid(),
              'pageSize': '1000',
              'pageNumber': '1'}
    request_view_shop_id = requests.get(url, params)
    if request_view_shop_id.status_code != 200:
        return '[×] %s门店信息获取失败'%request_view_shop_id.status_code
    else:
        if request_view_shop_id.json()['msg'] != '成功':
            return '[×] %s门店信息获取失败'%request_view_shop_id.json()
        else:
            shop = []
            for s in request_view_shop_id.json()['data']['list']:
                if s['shopType'] == 'affiliate':
                    shop.append((s['id'], s['name']))
                else:
                    continue
    return '门店列表加盟门店获取成功', shop

# 获取门店列表所有门店名称(包括托管)
def View_shop_name():
    login.Login()
    url = CONFIG.Url() + '/api/small/shop/list.jhtml'
    params = {'unionId': CONFIG.Unionid(),
              'pageSize': '1000',
              'pageNumber': '1'}
    request_view_shop_name = requests.get(url, params)
    if request_view_shop_name.status_code != 200:
        return '[×] %s,你懂的' % request_view_shop_name.status_code
    else:
        list = request_view_shop_name.json()
        shop_list = []
        for list in list['data']['list']:
            shop_list.append(list['name'])
        return '门店列表所有门店获取成功', shop_list



# 获取加盟店id(去除托管店)
# 使用处：获取bd门店列表
def View_shop_affiliate_1():
    login.Login()
    url = CONFIG.Url() + '/api/small/shop/list.jhtml'
    params = {'unionId': CONFIG.Unionid(),
              'pageSize': '1000',
              'pageNumber': '1'}
    request_view_shop_id = requests.get(url, params)
    if request_view_shop_id.status_code != 200:
        return '[×] %s门店信息获取失败'%request_view_shop_id.status_code
    else:
        if request_view_shop_id.json()['msg'] != '成功':
            return '[×] %s门店信息获取失败'%request_view_shop_id.json()
        else:
            shop = []
            for s in request_view_shop_id.json()['data']['list']:
                if s['shopType'] == 'affiliate' and s['myself'] is True:
                    shop.append((s['id'], s['name']))
                else:
                    continue
    return '门店列表加盟门店获取成功(不包托管店)', shop


if __name__ == '__main__':
    print(View_shop_name())
#     print(View_shop_direct())
#     print(View_shop_affiliate())

