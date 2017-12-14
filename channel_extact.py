'''
channel_extact.py 主要任务是从腾讯云服务器的position数据库中获取爬取链接
'''
import pymysql
from config import db_config as df
def GetLinks():
    link_list=[]
    try:
        conn = pymysql.connect(host=df['host'],port=df['port'],
                               user=df['user'],password=df['password'],
                               database=df['database'],charset=df['charset'])
    except:
        print("连接出错")
    cur=conn.cursor()
    cur.execute('select * from positions where sp=0')
    links=cur.fetchall()
    for link in links:
        link_list.append({
            'position':link[0],
            'link':link[1],
            'tag':link[2],
            'sp':link[3]
        })
    return link_list

GetLinks()

