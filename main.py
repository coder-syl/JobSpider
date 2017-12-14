from multiprocessing import Pool
from channel_extact  import GetLinks
from pages_parsing   import get_links_from
from gevent import monkey
monkey.patch_socket()
from multiprocessing.dummy import Pool as ThreadPool
import time
import gevent.pool
import gevent



if __name__ == "__main__":
    link_list = GetLinks()
    pool = ThreadPool(2)  # 4核
    #results =
    #pool.map(get_links_from, link_list)  # 需要执行的方法和地址列表
    pool=gevent.pool.Pool(4)
    for i in link_list:
        # print(i['sp'],i['link'],i['tag'],i['position'])
        # get_links_from(i)
        pool.add(gevent.spawn(get_links_from,i))
    pool.join()
    pool.close()
    pool.join()  # 等待线程都结束后再执行主模块
