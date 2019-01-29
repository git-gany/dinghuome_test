
"""运行业务流程"""

import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import login
import login_exit
import add_shop
import seckill
import goods
import supplier
import view_shop
import information

# 登陆
print('[1.1]', login.Login()) # 登陆

# 创建门店
print('[2.1]', add_shop.Add_shop_affiliate()) # 创建加盟门店
print('[2.2]', add_shop.Add_shop_direct()) # 创建直营门店

# 门店列表
print('[3.1]', view_shop.View_shop_name()) # 获取门店列表

# 秒杀列表
print('[4.1]', seckill.Seckill_list()) # 获取秒杀列表

# 获取企业信息
print('[5.1]', information.Information()) # 获取‘我的’企业信息,1存在企业，0不存在企业

# 企业列表
print('[6.1]', supplier.Supplier_list().Supplier_platform_zhiying()) # 获取平台直营门店企业列表
print('[6.2]', supplier.Supplier_list().Supplier_platform_jiameng()) # 获取平台加盟门店企业列表
print('[6.3]', supplier.Supplier_list().Supplier_local_zhiying()) # 获取本地直营门店企业列表
print('[6.4]', supplier.Supplier_list().Supplier_local_jiameng()) # 获取本地加盟门店企业列表

# 商品列表
print('[7.1]', goods.Goods_platform_zhiying_shop_ziyouzhiying()) # 平台-直营门店-自有直营企业 货品列表
print('[7.2]', goods.Goods_platform_zhiying_shop_zhiyin()) # 平台-直营门店-直营企业 货品列表
print('[7.3]', goods.Goods_platform_jiameng_shop_sanfang()) # 平台-加盟门店-三方企业 货品列表
print('[7.4]', goods.Goods_local_zhiying_shop_ziyouzhiying()) # 本地-直营门店-自有直营企业 货品列表
print('[7.5]', goods.Goods_local_zhiying_shop_zhiying()) # 本地-直营门店-直营企业 货品列表
print('[7.6]', goods.Goods_local_jiameng_shop_sanfang()) # 本地-加盟门店-三方企业 货品列表
print('[7.7]', goods.Goods_local_zhiying_shop()) # 本地-直营门店-本地供应商 货品列表
print('[7.8]', goods.Goods_local_jiameng_shop()) # 本地-加盟门店-本地供应商 货品列表

# print('[0]', login_exit.Login_exit()) # 解除绑定



