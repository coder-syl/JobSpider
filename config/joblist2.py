'''
joblist2 爬取http://www.chinahr.com/jobs/ 本地实例为 1.html
主要是爬取里面的职业分类，最终存储到腾讯云服务器上。
数据库为 position
'''
# coding=utf-8;
from bs4 import BeautifulSoup
import requests
import pymysql
from db.dbConfig import db_config as df

try:
    conn = pymysql.connect(host=df['host'], port=df['port'],
                           user=df['user'], password=df['password'],
                           database=df['database'], charset=df['charset'])
except:
    print("连接出错")
cur = conn.cursor()

try:
    # 执行SQL语句
    cur.execute("delete  from positions")
    print("删除数据成功")
    conn.commit()
except Exception as e:
    # 发生错误时回滚
    print(e)
    conn.rollback()

html = requests.get('http://www.chinahr.com/jobs/')
soup = BeautifulSoup(html.text, 'lxml')
positionss = soup.find_all('div', class_="item-class")
i = 1
for p in positionss:
    print("第{}种职业".format(i) + '--------')
    positions = p.find_all('a')
    tag = p.find('div', class_='til-class').find('a').text
    k = 1
    while (k < len(positions)):
        link = positions[k]['href']
        pos = positions[k].text
        hasSpider=0
        print('链接：' + link + '职位：' + pos + '标签：' + tag)
        sql = 'insert ignore into positions(position,link,tag,hasSpider) values (%s,%s,%s,%s)'
        try:
            cur.execute(sql, (pos, link, tag,hasSpider))
            print("插入成功")
            k = k + 1
        except Exception as e:
            print("插入失败")
            print(e)
            k = k + 1
        k = k + 1
    i = i + 1
conn.commit()
conn.close()
print("程序运行结束")
