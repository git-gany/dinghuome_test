import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import pymysql
import CONFIG

# 获取MemberID
def Member_id():
    connect = pymysql.connect(CONFIG.Data_base_config()['address'], CONFIG.Data_base_config()['user'],CONFIG.Data_base_config()['pwd'],CONFIG.Data_base_config()['base_name'])
    try:
        cursor = connect.cursor()  # 游标
        cursor.execute('select id, mobile \
                        from xx_member \
                        where mobile = \'%s\'' % CONFIG.Mobile())  #执行sql
        member_id = cursor.fetchall()[0]  # 返回执行结果
        connect.close() # 断开数据库连接
        return member_id
    except Exception as error:
        connect.close()
        return '数据库操作失败-->%s' % error



# 获取商品列表最终价格
def ProductPrice():
    pass

# 查询订单编号
def OrderCode(id):
    connect = pymysql.connect(CONFIG.Data_base_config()['address'], CONFIG.Data_base_config()['user'],CONFIG.Data_base_config()['pwd'],CONFIG.Data_base_config()['base_name'])
    try:
        cursor = connect.cursor() # 游标
        cursor.execute('select id, sn \
                        from xx_order \
                        where id = \'%s\'' % id)  # 执行sql
        sn = cursor.fetchall()[0]  # 返回执行结果
        connect.close()  # 断开数据库连接
        return sn[1]
    except Exception as error:
        connect.close()
        return '数据库操作失败, 订单id: %s没找到-->异常记录: %s' % (id,error)




if __name__ == '__main__':
    print(OrderCode('8415'))
    # print(Member_id())
