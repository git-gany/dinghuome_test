
"""获取秒杀列表"""

import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import requests
import CONFIG
import login
def Seckill_list():
    login.Login()
    url = CONFIG.Url() + '/api/small/messageMemberProduct/findList.jhtml'
    params = {'unionId': CONFIG.Unionid(),
              'shopId':  '3147', # 此处当前写死
              'pageNumber': '1',
              'pageSize': '1000'}
    request = requests.get(url, params)
    if request.status_code != 200:
        return '[×] 获取秒杀列表失败, %s' % request.status_code
    else:
        # return request.json()
        if request.json()['msg'] != '成功':
            return '[×] 秒杀列表获取异常-->%s' % request.json()
        else:
            seckill_list_all = request.json()['data']['result'] # 推荐列表
            seckill_list = [] # 秒杀列表，需从推荐列表作筛选处理
            for list in seckill_list_all:
                if list['products'][0]['activityType'] == 'pike': # 判断货品是否满足秒杀条件
                    # seckill_list.append(list)
                    seckill_list.append({'商品名称': list['name'],
                                         '限购量': list['products'][0]['maxNumber'],
                                         '秒杀价': list['products'][0]['activityPrice'],
                                         '供应价': list['products'][0]['supplyPrice'],
                                         '供应商': list['supplierName']
                                         })
                    # print(seckill_list[-1], '\n\n')
                else:
                    continue
        return '秒杀货品列表获取成功', {'数量': len(seckill_list)}, {'列表': seckill_list}
if __name__ == '__main__':
    print(Seckill_list())
