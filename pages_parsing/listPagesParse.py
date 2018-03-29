# encoding: utf-8


from selenium import webdriver
import time
from pages_parsing.emailSend import sendEmail

def listParse(url_list, dbHandle):
    try:
        year=time.strftime("%Y",time.localtime())
        month=time.strftime("%Y",time.localtime())
        print(url_list['hasSpider'])  ## 打印当前连接是否爬取过
        chrome = webdriver.Chrome('/Users/syl/node_modules/chromedriver/lib/chromedriver/chromedriver')
        if url_list['hasSpider'] == 0:
            spiderNum=0
            print('正在爬取' + '链接：' + url_list['link'])
            chrome.get(url_list['link'])
            print("正在爬取第一页------------------------------------------------------------")
            elem = chrome.find_elements_by_class_name("jobList")
            j = 1
            for i in elem:
                spiderNum=spiderNum+1
                print("这是第{}个职位信息".format(j))
                i1 = i.find_element_by_class_name('l1')
                i2 = i.find_element_by_class_name('l2')
                position = i1.find_element_by_class_name('e1').text
                company = i1.find_element_by_class_name('e3').text
                adrexp = i2.find_element_by_class_name('e1')
                money = i2.find_element_by_class_name('e2')
                adr = adrexp.text.split("[")[1].split("]")[0].split("/")[0].replace(" ", '')
                exp = adrexp.text.split("[")[1].split("]")[1].replace("\r\n\t\t\t\t\t\t\t", '').split("/")[0]\
                    .replace(
                    " ", '')
                edu = adrexp.text.split("[")[1].split("]")[1].replace("\r\n\t\t\t\t\t\t\t", '').split("/")[1]\
                    .replace(
                    " ", '')
                if money.text == '面议':
                    continue;
                else:
                    lowmoney = money.text.split("-")[0]
                    highmoney = money.text.split("-")[1]
                avermoney = (int(lowmoney) + int(highmoney)) / 2
                sql = "INSERT INTO joblist(company ,position ,adr ,edu ,exp ,lowmoney,highmoney ,avermoney,year,curmon,ta,tag)" \
                      "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                      %(company, position, adr, edu, exp,int(lowmoney),int(highmoney),avermoney, year, month,url_list['position'],url_list['tag'])
                dbHandle.dbInsert(sql)
                j = j + 1
                curpage = 2
            while True:
                time.sleep(6)
                try:
                    chrome.find_element_by_link_text('下一页').click()
                    print('正在爬取下一页======================================================')
                except:
                    print(
                        "已经到达最后一页----------------------------------------------------------------------------------------------------------------")
                    dbHandle.dbUpdate("UPDATE positions SET hasSpider=1 where position='{}'".format(url_list['position']))
                    sendEmail(url_list['link'] + ":{}".format(spiderNum))
                    break;
                print('正在爬取第{}页******************************************************'.format(curpage))
                elem = chrome.find_elements_by_class_name("jobList")
                j = 1
                for i in elem:
                    spiderNum = spiderNum + 1
                    print("这是第{}个职位信息------------------".format(j) + '  _--职位：' + url_list['position'] + '--标签' +
                          url_list['tag'])
                    i1 = i.find_element_by_class_name('l1')
                    i2 = i.find_element_by_class_name('l2')
                    position = i1.find_element_by_class_name('e1').text  # .replace(" ", '')
                    company = i1.find_element_by_class_name('e3').text  # .replace("\n", '').replace(" ", '')
                    adrexp = i2.find_element_by_class_name('e1')
                    money = i2.find_element_by_class_name('e2')  # 薪资
                    adr = adrexp.text.split("[")[1].split("]")[0].split("/")[0].replace(" ", '')  # 工作地址

                    exp = adrexp.text.split("[")[1].split("]")[1].replace("\r\n\t\t\t\t\t\t\t", '').split("/")[
                        0].replace(" ", '')
                    edu = adrexp.text.split("[")[1].split("]")[1].replace("\r\n\t\t\t\t\t\t\t", '').split("/")[
                        1].replace(" ", '')  # 学历
                    if money.text == '面议':
                        lowmoney = highmoney = '0';

                    else:
                        lowmoney = money.text.split("-")[0]
                        highmoney = money.text.split("-")[1]
                    avermoney = (int(lowmoney) + int(highmoney)) / 2
                    sql = "INSERT INTO joblist(company ,position ,adr ,edu ,exp ,lowmoney,highmoney ,avermoney,year,curmon,ta,tag)" \
                          "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                          % (company, position, adr, edu, exp, int(lowmoney), int(highmoney), avermoney, year, month,
                    url_list['position'], url_list['tag'])
                    dbHandle.dbInsert(sql)
                    j = j + 1
                curpage = curpage + 1
            chrome.close()
    except:
        dbHandle.dbUpdate("UPDATE positions SET hasSpider=1 where position='{}'".format(url_list['position']))
        sendEmail(url_list['link'] + ":{}".format(spiderNum))
