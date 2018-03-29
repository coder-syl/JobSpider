# encoding: utf-8
from db.dbHandle import dbHandle
from pages_parsing.listPagesParse   import listParse
from gevent import monkey
monkey.patch_socket()
# from multiprocessing.dummy import Pool as ThreadPool
import gevent.pool
import gevent



if __name__ == "__main__":
    dbHandle=dbHandle()
    sql='select * from positions where hasSpider=0'
    link_list = dbHandle.dbQueryLinks(sql)
    # pool = ThreadPool(4)  # 4核
    pool=gevent.pool.Pool(2)
    for i in link_list:
        pool.add(gevent.spawn(listParse,i,dbHandle))
    pool.join()
    pool.close()
    pool.join()  # 等待线程都结束后再执行主模块
