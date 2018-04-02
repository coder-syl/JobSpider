from selenium import webdriver
def detailParse(detaillink):
    chrome = webdriver.Chrome('/Users/syl/node_modules/chromedriver/lib/chromedriver/chromedriver')
    if detaillink!='':
        chrome.get(detaillink)
        elem = chrome.find_element_by_class_name("job_intro_info")
        position_intro=str(elem.text)
        return position_intro
