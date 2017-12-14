
import time

import pymysql
from config import db_config as df
def updata(p):
    try:
        conn = pymysql.connect(host=df['host'],port=df['port'],
                               user=df['user'],password=df['password'],
                               database=df['database'],charset=df['charset'])
    except:
        print("连接出错")
    cur=conn.cursor( )
    sta = cur.execute("UPDATE positions SET sp=1 where position='{}'".format(p))
    if sta == 1:
        print('更新成功--------------------------------------------------------------------------------')
    else:
        print('更新失败--------------------------------------------------------------------------------')

    conn.commit()
    cur.close()
    conn.close()