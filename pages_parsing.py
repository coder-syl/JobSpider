from insertdata import inquery
from selenium import webdriver
from updatedata import updata

import time
def get_links_from(url_list):
    f = open('log.txt', 'a')
    f.write('__职位：' + url_list['position'] + '__标签: ' + url_list['tag'] + 'statue： ' + str(1) + '\n')
    print('写入文件成功')
    f.close()
    try:
        print(url_list['sp'])
        chrome = webdriver.PhantomJS()
        if url_list['sp']==0:
            print('正在爬取')
            chrome.get(url_list['link'])
            print('链接：'+url_list['link']+'  _--职位：'+url_list['position']+'--标签'+url_list['tag'])
            print("正在爬取第一页------------------------------------------------------------")
            elem=chrome.find_elements_by_class_name("jobList")
            j=1
            for i in elem :
                print("这是第{}个职位信息------------------".format(j)+'  _--职位：'+url_list['position']+'--标签'+url_list['tag'])
                i1=i.find_element_by_class_name('l1')
                i2=i.find_element_by_class_name('l2')
                position = i1.find_element_by_class_name('e1').text#.replace(" ", '')
                company = i1.find_element_by_class_name('e3').text#.replace("\n", '').replace(" ", '')
                adrexp =i2.find_element_by_class_name('e1')
                money =i2.find_element_by_class_name('e2')  # 薪资
                adr = adrexp.text.split("[")[1].split("]")[0].split("/")[0].replace(" ", '')  # 工作地址
                try:
                    exp = adrexp.text.split("[")[1].split("]")[1].replace("\r\n\t\t\t\t\t\t\t", '').split("/")[0].replace(" ",
                                                                                                                          '').replace(
                        "年", '').replace("应届生", '0')  # 经验
                    edu = adrexp.text.split("[")[1].split("]")[1].replace("\r\n\t\t\t\t\t\t\t", '').split("/")[1].replace(" ",'')  # 学历
                    if edu=='其他':
                        edu='不限'
                except:
                    exp = '0'
                    edu = adrexp.text.split("[")[1].split("]")[1]
                    if edu=='其他':
                        edu='不限'
                if money.text=='面议':
                    lowmoney=higmony='0';

                else:
                    lowmoney = money.text.split("-")[0]
                    higmony = money.text.split("-")[1]
                avermoney = (int(lowmoney) + int(higmony)) / 2
                print("公司:  " + company+ '  _--职位：' + url_list['position'] + '--标签' +
                          url_list['tag'])#成功
                print("职位:  " + position)#成功
                # print("工作地点:  " + adr)#成功
                # print("学历:  " + edu)
                # print("经验:  " + exp)
                # print("工资下限:  " + higmony)#成功
                # print("工资上限:  " + money.text)#成功
                # print("平均工资： " + str(int(avermoney)))#成功
                inquery(company, position, adr, edu, exp, lowmoney, higmony, avermoney, 2017,7, url_list['position'],url_list['tag'])
                j=j+1
            curpage=2
            while True:
                time.sleep(6)
                try:
                    chrome.find_element_by_link_text('下一页').click()
                    print('正在爬取下一页======================================================')
                except:
                    print("已经到达最后一页----------------------------------------------------------------------------------------------------------------")
                    updata(url_list['position'])
                    break;
                print('正在爬取第{}页******************************************************'.format(curpage))
                elem=chrome.find_elements_by_class_name("jobList")
                j=1
                for i in elem :
                    print("这是第{}个职位信息------------------".format(j) + '  _--职位：' + url_list['position'] + '--标签' +
                          url_list['tag'])
                    i1 = i.find_element_by_class_name('l1')
                    i2 = i.find_element_by_class_name('l2')
                    position = i1.find_element_by_class_name('e1').text  # .replace(" ", '')
                    company = i1.find_element_by_class_name('e3').text  # .replace("\n", '').replace(" ", '')
                    adrexp = i2.find_element_by_class_name('e1')
                    money = i2.find_element_by_class_name('e2')  # 薪资
                    adr = adrexp.text.split("[")[1].split("]")[0].split("/")[0].replace(" ", '')  # 工作地址
                    try:
                        exp = adrexp.text.split("[")[1].split("]")[1].replace("\r\n\t\t\t\t\t\t\t", '').split("/")[0].replace(
                            " ",
                            '').replace(
                            "年", '').replace("应届生", '0')  # 经验
                        edu = adrexp.text.split("[")[1].split("]")[1].replace("\r\n\t\t\t\t\t\t\t", '').split("/")[1].replace(
                            " ", '')  # 学历
                        if edu == '其他':
                            edu = '不限'
                    except:
                        exp = '0'
                        edu = adrexp.text.split("[")[1].split("]")[1]
                        if edu == '其他':
                            edu = '不限'
                    if money.text == '面议':
                        lowmoney = higmony = '0';

                    else:
                        lowmoney = money.text.split("-")[0]
                        higmony = money.text.split("-")[1]
                    avermoney = (int(lowmoney) + int(higmony)) / 2
                    print("公司:  " + company+ '  _--职位：' + url_list['position'] + '--标签' +
                          url_list['tag'])  # 成功
                    print("职位:  " + position)  # 成功
                    # print("工作地点:  " + adr)  # 成功
                    # print("学历:  " + edu)
                    # print("经验:  " + exp)
                    # print("工资下限:  " + higmony)  # 成功
                    # print("工资上限:  " + money.text)  # 成功
                    # print("平均工资： " + str(int(avermoney)))  # 成功
                    inquery(company, position, adr, edu, exp, lowmoney, higmony, avermoney, 2017,7,url_list['position'],url_list['tag'])
                    j=j+1
                curpage=curpage+1
            chrome.close()
    except Exception  as e:
        print(e)
        time.sleep(10)




