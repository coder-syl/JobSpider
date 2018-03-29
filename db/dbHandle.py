# coding:utf-8

import pymysql
from db.dbConfig import db_config as df


class dbHandle():
    def __init__(self):
        # self.host = host
        # self.port = port
        # self.user = user
        # self.password = password
        # self.database = database
        # self.charset = charset
        try:
            self.conn = pymysql.connect(host=df['host'], port=df['port'], user=df['user'], password=df['password'],
                                        database=df['database'], charset=df['charset'])
        except:
            print("连接数据库失败")
        self.cur = self.conn.cursor()

    def dbClose(self):
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()

    def dbQueryLinks(self,sql):
        link_list = []
        self.cur.execute(sql)
        links = self.cur.fetchall()
        for link in links:
            link_list.append({
                'position': link[0],
                'link': link[1],
                'tag': link[2],
                'hasSpider': link[3]
            })
        return link_list

    def dbInsert(self, sql):
        try:
            self.cur.execute(sql)
            print("插入成功！！！")
            self.conn.commit()

        except Exception as e:
            print(e)
            print('插入失败！！！')

    def dbUpdate(self, sql):
        try:
            self.cur.execute(sql)
            print("更新状态成功！！！")
            self.conn.commit()

        except Exception as e:
            print(e)
            print('更新状态失败！！！')
if __name__ == '__main__':
    dbHandle = dbHandle()
    dbHandle.dbQueryLinks()
