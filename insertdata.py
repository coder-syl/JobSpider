# coding:utf-8

import pymysql
from config import db_config as df
def inquery(comp ,pos ,ad,ed ,ex ,l,h ,av,year,cm,ta,tag):
      try:
          conn = pymysql.connect(host=df['host'],port=df['port'],
                               user=df['user'],password=df['password'],
                               database=df['database'],charset=df['charset'])
      except:
        print("连接出错")
      cur=conn.cursor()
      try:
          cur.execute("INSERT INTO joblist(company ,position ,adr ,edu ,exp ,lowmoney,highmoney ,avermoney,year,curmon,ta,tag) \
                                           values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",\
                                           (comp ,pos ,ad,ed ,int(ex) ,int(l),int(h) ,int(av),int(year),int(cm),ta,tag))

      except Exception as e:
          print(e)
          print('插入失败。。。')
      conn.commit()
      cur.close()
      conn.close()