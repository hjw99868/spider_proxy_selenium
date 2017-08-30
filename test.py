### phone ###
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import dictory

#fun：查找公司
def find_com(driver, company):
    driver.find_element_by_xpath(dictory.dictory['input_divn']).send_keys(Keys.TAB)
    driver.find_element_by_xpath(dictory.dictory['input_divn']).clear()
    driver.find_element_by_xpath(dictory.dictory['input_divn']).send_keys(company)
    driver.find_element_by_xpath(dictory.dictory['search_btnn']).click()
    time.sleep(3)
    try:
        driver.find_element_by_xpath(dictory.dictory['first_line1']).click()
    except:
        try:
            driver.find_element_by_xpath(dictory.dictory['first_line2']).click()  # 点击第一条
        except:
            driver.find_element_by_xpath(dictory.dictory['first_line3']).click()
    time.sleep(4)
    try:
        driver.find_element_by_xpath(dictory.dictory['unfold_btn']).click()  # 展开经营范围详细信息
    except:
        pass

#fun：第一次搜索
def first_com(driver, company):
    driver.get(dictory.dictory['web'])
    driver.find_element_by_xpath(dictory.dictory['input_div1']).send_keys(Keys.TAB)
    driver.find_element_by_xpath(dictory.dictory['input_div1']).send_keys(company)
    driver.find_element_by_xpath(dictory.dictory['search_btn1']).click()  # 点击搜索
    time.sleep(3)
    driver.find_element_by_xpath(dictory.dictory['first_line1']).click()  # 点击第一条
    time.sleep(2)
    # with open("result.csv", 'a', newline="", encoding='utf-8') as datacsv:
    #     csvwriter = csv.writer(datacsv)
    #     csvwriter.writerow(['公司名称', '组织机构代码 ', '工商注册号 ', '法定代表人 ', '注册资本 ', '注册地址 ', '注册时间 ', '登记机关 ', '企业类型 ', '核准日期 ', '状态', '营业期限 ', '行业 ', '经营范围'])

#fun：后退
def back(driver):
    driver.back()
    time.sleep(3)

def info_find(driver, string):
    try:
        info_re = driver.find_element_by_xpath(dictory.dictory[string]).text
    except:
        info_re = "未公开"
    return info_re

#fun：公司页面检索信息
def cp_info(driver):
    com_name = info_find(driver, 'com_name')
    org_id = info_find(driver, 'org_id')
    reg_id = info_find(driver, 'reg_id')
    legal_person = info_find(driver, 'legal_person')
    reg_capital = info_find(driver, 'reg_capital')
    reg_address = info_find(driver, 'reg_address')
    reg_time = info_find(driver, 'reg_time')
    reg_institution = info_find(driver, 'reg_institution')
    enterprise_type = info_find(driver, 'enterprise_type')
    issue_time = info_find(driver, 'issue_time')
    business_status = info_find(driver, 'business_status')
    business_term = info_find(driver, 'business_term')
    business_type = info_find(driver, 'business_type')
    business_scope = info_find(driver, 'business_scope')
    # credit_id = driver.find_element_by_xpath("").text      #统一信用代码
    with open("result.csv", 'a', newline="", encoding='utf-8') as datacsv:                 #记录到csv文件
        csvwriter = csv.writer(datacsv)
        csvwriter.writerow([com_name, org_id, reg_id, legal_person, reg_capital, reg_address, reg_time, reg_institution, enterprise_type, issue_time, business_status, business_term, business_type, business_scope])

def main():
    dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置userAgent
    #使用移动端浏览器ua
    dcap["phantomjs.page.settings.userAgent"] = (dictory.dictory['phantomjs_ag'])
    #调用phantomjs
    obj = webdriver.PhantomJS(executable_path=r"C:\Users\hjw99868\Desktop\phantomjs-1.9.7-windows\phantomjs.exe", desired_capabilities=dcap)
    obj.maximize_window()
    #初始化搜索
    first_com(obj, "初始化")
    company = open("web_ch.txt", 'r', encoding='utf-8')
    line = company.readline()
    i=0
    while line:
        try:
            i=i+1
            flag = str(i)
            print("searching "+flag+" ...................")
            re_com = line.strip('\n')
            line = company.readline()
            back(obj)         #后退
            find_com(obj, re_com)       #查找
            cp_info(obj)         #记录
        except Exception as err:
            print(err)

if __name__ == '__main__':
    main()










###########################################
### pc端代码（反爬） ###
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# dcap = dictory(DesiredCapabilities.PHANTOMJS)  # 设置userAgent
# dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")
#
# obj = webdriver.PhantomJS(executable_path=r"C:\Users\hjw99868\Desktop\phantomjs-1.9.7-windows\phantomjs.exe", desired_capabilities=dcap)
# obj.maximize_window()
# obj.get('http://www.tianyancha.com/')
#
# obj.find_element_by_id('live-search').send_keys(Keys.TAB)
# obj.find_element_by_id('live-search').send_keys('百度')
# obj.find_element_by_css_selector('div.input-group-addon.search_button > span').click()
# time.sleep(2)
# #标签页切换
# handle = obj.current_window_handle
# obj.find_element_by_xpath("//*[@id='ng-view']/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/a/span").click()
# handles = obj.window_handles
# for newhandle in handles:
#     if newhandle != handle:
#         obj.switch_to_window(newhandle)
# print(obj.page_source)
# obj.get_screenshot_as_file('bai.png')
###############################################

###############################################
### 测试是否有验证码 ###
# for i in range(150041670,150041700):
#     ip = str(i)
#     url = 'http://www.tianyancha.com/company/' + ip
#     obj.get(url)
#     test = obj.find_element_by_xpath("//*[@id='ng-view']/div[2]/div[1]/div[1]/div[1]").text
#     if test == '很抱歉，您要访问的页面不存在':
#         print(ip)
#     else:
#         print(test)
# obj.get_screenshot_as_file("123.png")
###############################################



