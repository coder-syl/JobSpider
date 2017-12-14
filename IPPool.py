'''
IPPool 主要是从腾讯云服务器的IP代理池中回去每日更新的IP
'''
import pymysql
from config import db_config as df
def GetIp():
    url=[]
    try:
        conn = pymysql.connect(host=df['host'],port=df['port'],
                               user=df['user'],password=df['password'],
                               database=df['database'],charset=df['charset'])
    except:
        print("连接出错")
    cur=conn.cursor()
    cur.execute('select * from IP')
    ips=cur.fetchall()
    for ip in ips:
        url.append(ip)
    return url
GetIp()