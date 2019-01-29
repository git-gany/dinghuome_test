

"""运行业务流程"""

import sys
import pytest
import login
import login_exit
import add_shop
import seckill
import goods
import supplier
import view_shop
import information
import bd
import shoppingCart
import order


# 登陆-id: 1
# @pytest.mark.skip(reason='跳过，没理由')
@pytest.mark.skipif(sys.version_info < (3, 0), reason="python版本低于3.0, 用例无法运行")
class Test_login:
    def test_1_1(self):
        print('接口：登陆    预期：登陆成功')
        assert login.Login()[0] == '登陆成功'

# 门店-id：2
class Test_shop:

    # 门店列表
    def test_2_1(self):
        print('接口：获取门店列表    预期：获取成功')
        assert view_shop.View_shop_name()[0] == '门店列表所有门店获取成功' # 正确获取门店列表

    @pytest.mark.skip(reason='加盟门店已经够多了，跳过创建')
    def test_2_2(self):
        print('接口：添加加盟门店    预期：添加成功')
        assert add_shop.Add_shop_affiliate()[0] == '加盟门店创建成功' # 正确创建加盟门店

    @pytest.mark.skip(reason='直营门店已经够多了，跳过创建')
    def test_2_3(self):
        print('接口：创建直营门店    预期：创建成功')
        assert add_shop.Add_shop_direct()[0] == '直营门店创建成功' or '账号不存在企业，跳过创建直营门店' # 创建直营门店

# 秒杀列表-id: 4
class Test_seckill:
    def test_4_1(self):
        print('接口：获取秒杀列表    预期：获取成功')
        assert seckill.Seckill_list()[0] == '秒杀货品列表获取成功' # 正确获取秒杀列表

# 我的-id:5
class Test_my:
    def test_5_1(self): # 获取企业我的企业信息
        print('接口：“我的”中企业信息     预期：存在企业/不存在企业')
        assert information.Information()[0] == '0' or information.Information()[0] == '1'  # 获取‘我的’企业信息,1存在企业，0不存在企业

# 企业列表-id: 6
class Test_supplier:
    def test_6_1(self):
        print('接口：获取平台直营门店列表    预期：获取成功')
        assert supplier.Supplier_list().Supplier_platform_zhiying()[0] == '平台直营门店企业列表获取成功' # 获取平台直营门店企业列表

    def test_6_2(self):
        print('接口：获取平台加盟门店企业列表  预期：获取成功')
        assert supplier.Supplier_list().Supplier_platform_jiameng()[0] == '平台加盟门店企业列表获取成功' # 获取平台加盟门店企业列表

    def test_6_3(self):
        print('接口：获取本地直营门店企业列表    预期：获取成功')
        assert supplier.Supplier_list().Supplier_local_zhiying()[0] == '本地直营门店企业列表获取成功' # 获取本地直营门店企业列表

    def test_6_4(self):
        print('接口：本地加盟门店企业列表获取成功    预期：获取成功')
        assert supplier.Supplier_list().Supplier_local_jiameng()[0] == '本地加盟门店企业列表获取成功' # 获取本地加盟门店企业列表

# 货品列表-id: 7
class Test_goods:
    def test_7_1(self):
        print('接口：获取自有直营型货品列表   预期：成功')
        assert goods.Goods_platform_zhiying_shop_ziyouzhiying()[0] == '自有直营型货品列表获取成功' # 平台-直营门店-自有直营企业 货品列表

    def test_7_2(self):
        print('接口：获取直营型货品列表     预期：成功')
        assert goods.Goods_platform_zhiying_shop_zhiyin()[0] == '直营型货品列表获取成功' # 平台-直营门店-直营企业 货品列表

    def test_7_3(self):
        print('接口：获取平台-加盟门店-三方企业 货品列表   预期：成功')
        assert goods.Goods_platform_jiameng_shop_sanfang()[0] == '平台-加盟门店-三方企业 货品列表获取成功' # 平台-加盟门店-三方企业 货品列表

    def test_7_4(self):
        print('接口：获取本地-直营门店-自有直营企业 货品列表     预期：成功')
        assert goods.Goods_local_zhiying_shop_ziyouzhiying()[0] == '本地-直营门店-自有直营企业 货品列表获取成功' # 本地-直营门店-自有直营企业 货品列表

    def test_7_5(self):
        print('接口：获取本地-直营门店-直营企业 货品列表   预期：成功')
        assert goods.Goods_local_zhiying_shop_zhiying()[0] == '本地-直营门店-直营企业 货品列表获取成功' # 本地-直营门店-直营企业 货品列表

    def test_7_6(self):
        print('接口：获取本地-加盟门店-三方企业 货品列表   预期：成功')
        assert goods.Goods_local_jiameng_shop_sanfang()[0] == '本地-加盟门店-三方企业 货品列表获取成功' # 本地-加盟门店-三方企业 货品列表

    def test_7_7(self):
        print('接口：获取本地-直营门店-本地供应商 货品列表  预期：成功')
        assert goods.Goods_local_zhiying_shop()[0] == '本地-直营门店-本地供应商 货品列表获取成功' # 本地-直营门店-本地供应商 货品列表

    def test_7_8(self):
        print('接口：获取本地-加盟门店-本地供应商 货品列表      预期：成功')
        assert goods.Goods_local_jiameng_shop()[0] == '本地-加盟门店-本地供应商 货品列表获取成功' # 本地-加盟门店-本地供应商 货品列表

#  购物车-id: 8
class Test_shoppingCart:

    # 8_1 添加购物车
    def test_8_1_1(self):
        print('接口：添加购物车(平台自有直营)     预期：成功')
        assert shoppingCart.Add_shoppingCart().Add_shoppingCart_1() == '平台自有直营购物车货品添加成功'

    def test_8_1_2(self):
        print('接口：添加购物车(平台直营)     预期：成功')
        assert shoppingCart.Add_shoppingCart().Add_shoppingCart_2() == '平台直营购物车货品添加成功'

    def test_8_1_3(self):
        print('接口：添加购物车(平台加盟)     预期：成功')
        assert shoppingCart.Add_shoppingCart().Add_shoppingCart_3() == '平台加盟购物车货品添加成功'

    def test_8_1_4(self):
        print('接口：添加购物车(本地自有直营)     预期：成功')
        assert shoppingCart.Add_shoppingCart().Add_shoppingCart_4() == '本地自有直营购物车货品添加成功'

    def test_8_1_5(self):
        print('接口：添加购物车(本地直营)     预期：成功')
        assert shoppingCart.Add_shoppingCart().Add_shoppingCart_5() == '本地直营购物车货品添加成功'

    def test_8_1_6(self):
        print('接口：添加购物车(本地加盟)     预期：成功')
        assert shoppingCart.Add_shoppingCart().Add_shoppingCart_6() == '本地加盟购物车货品添加成功'

    def test_8_1_7(self):
        print('接口：添加购物车(本地直营店)     预期：成功')
        assert shoppingCart.Add_shoppingCart().Add_shoppingCart_7() == '本地直营店购物车货品添加成功'

    def test_8_1_8(self):
        print('接口：添加购物车(本地加盟店)     预期：成功')
        assert shoppingCart.Add_shoppingCart().Add_shoppingCart_8() == '本地加盟店购物车货品添加成功'

    # 8_2 查看购物车
    def test_8_2_1(self):
        print('接口：查看购物车(直营店-平台-自有直营型订单)     预期：成功')
        assert shoppingCart.See_shoppingCart().See_shoppingCart_1()[0] == '直营店-平台-自有直营型订单购物车获取成功'

    def test_8_2_2(self):
        print('接口：查看购物车(直营店-平台-直营型订单)     预期：成功')
        assert shoppingCart.See_shoppingCart().See_shoppingCart_2()[0] == '直营店-平台-直营型订单购物车获取成功'

    def test_8_2_3(self):
        print('接口：查看购物车(加盟店-平台-三方型订单)     预期：成功')
        assert shoppingCart.See_shoppingCart().See_shoppingCart_3()[0] == '加盟店-平台-三方型订单购物车获取成功'

    def test_8_2_4(self):
        print('接口：查看购物车(直营店-本地-自有直营型订单)     预期：成功')
        assert shoppingCart.See_shoppingCart().See_shoppingCart_4()[0] == '直营店-本地-自有直营型订单购物车获取成功'

    def test_8_2_5(self):
        print('接口：查看购物车(直营店-本地-直营型订单)     预期：成功')
        assert shoppingCart.See_shoppingCart().See_shoppingCart_5()[0] == '直营店-本地-直营型订单购物车获取成功'

    def test_8_2_6(self):
        print('接口：查看购物车(加盟店-本地-三方型订单)     预期：成功')
        assert shoppingCart.See_shoppingCart().See_shoppingCart_6()[0] == '加盟店-本地-三方型订单购物车获取成功'

    def test_8_2_7(self):
        print('接口：查看购物车(直营店-本地-本地供应商订单)     预期：成功')
        assert shoppingCart.See_shoppingCart().See_shoppingCart_7()[0] == '直营店-本地-本地供应商订单购物车获取成功'

    def test_8_2_8(self):
        print('接口：查看购物车(加盟店-本地-本地供应商订单)     预期：成功')
        assert shoppingCart.See_shoppingCart().See_shoppingCart_8()[0] == '加盟店-本地-本地供应商订单购物车获取成功'

    # 8_3 清空购物车
    def test_8_3_1(self):
        print('接口：清空购物车(直营店-平台-自有直营型订单)     预期：成功')
        assert shoppingCart.Delete_shoppingcartgoods().Delete_shoppingcartgoods_1() == '直营店-平台-自有直营型订单购物车清空成功'

    def test_8_3_2(self):
        print('接口：清空购物车(直营店-平台-直营型订单)     预期：成功')
        assert shoppingCart.Delete_shoppingcartgoods().Delete_shoppingcartgoods_2() == '直营店-平台-直营型订单购物车清空成功'

    def test_8_3_3(self):
        print('接口：清空购物车(加盟店-平台-三方型订单)     预期：成功')
        assert shoppingCart.Delete_shoppingcartgoods().Delete_shoppingcartgoods_3() == '加盟店-平台-三方型订单购物车清空成功'

    def test_8_3_4(self):
        print('接口：清空购物车(直营店-本地-自有直营型订单)     预期：成功')
        assert shoppingCart.Delete_shoppingcartgoods().Delete_shoppingcartgoods_4() == '直营店-本地-自有直营型订单购物车清空成功'

    def test_8_3_5(self):
        print('接口：清空购物车(本地-直营型订单)     预期：成功')
        assert shoppingCart.Delete_shoppingcartgoods().Delete_shoppingcartgoods_5() == '查看直营店-本地-直营型订单购物车清空成功'

    def test_8_3_6(self):
        print('接口：清空购物车(本地-三方型订单)     预期：成功')
        assert shoppingCart.Delete_shoppingcartgoods().Delete_shoppingcartgoods_6() == '加盟店-本地-三方型订单购物车清空成功'

    def test_8_3_7(self):
        print('接口：清空购物车(直营店-本地-本地供应商订单)     预期：成功')
        assert shoppingCart.Delete_shoppingcartgoods().Delete_shoppingcartgoods_7() == '直营店-本地-本地供应商订单购物车清空成功'

    def test_8_3_8(self):
        print('接口：清空购物车(加盟店-本地-本地供应商订单)     预期：成功')
        assert shoppingCart.Delete_shoppingcartgoods().Delete_shoppingcartgoods_8() == '加盟店-本地-本地供应商订单购物车清空成功'

# 订单-id: 9
class Test_order:
    def test_9_1(self):
        print('接口：结算(直营店-平台-自有直营型订单)  预期：成功')
        assert order.Submit().Order_1()[0] == '直营店-平台-自有直营型订单下单成功'

    def test_9_2(self):
        print('接口：直营店-平台-直营型订单  预期：成功')
        assert order.Submit().Order_2()[0] == '直营店-平台-直营型订单下单成功'

    def test_9_3(self):
        print('接口：盟店-平台-三方型订单  预期：成功')
        assert order.Submit().Order_3()[0] == '加盟店-平台-三方型订单下单成功'

    def test_9_4(self):
        print('接口：直营店-本地-自有直营型订单  预期：成功')
        assert order.Submit().Order_4()[0] == '直营店-本地-自有直营型订单下单成功'

    def test_9_5(self):
        print('接口：直营店-本地-直营型订单  预期：成功')
        assert order.Submit().Order_5()[0] == '直营店-本地-直营型订单下单成功'

    def test_9_6(self):
        print('接口：加盟店-本地-三方型订单  预期：成功')
        assert order.Submit().Order_6()[0] == '加盟店-本地-三方型订单下单成功'

    def test_9_7(self):
        print('接口：直营店-本地-本地供应商订单  预期：成功')
        assert order.Submit().Order_7()[0] == '直营店-本地-本地供应商订单下单成功'

    def test_9_8(self):
        print('接口：加盟店-本地-本地供应商订单  预期：成功')
        assert order.Submit().Order_8()[0] == '加盟店-本地-本地供应商订单下单成功'



# BD
class Test_bd:
    def test_null_1(self):
        assert bd.Bd_shop_list()[0] == 'BD门店列表获取成功'  # BD时获取门店列表

    def test_null_2(self):
        assert bd.Bd_shop_view()[0] == 'BD门店查看成功' # 查看BD门店的信息

    def test_null_3(self):
        assert bd.Bd_shop_add() == 'BD时门店添加成功' or bd.Bd_shop_add() == '账号下已存在门店, BD时无法创建门店, 跳过'

@pytest.mark.skip(reason='跳过解除绑定')
class Test_quit:
    def test_0_0(self):
        print('接口：小程序解除绑定   ')
        assert login_exit.Login_exit()[0] == '账号成功解除绑定'  # 解除绑定
