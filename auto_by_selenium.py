# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:29:13 2018

@author: 46979
"""
from selenium import webdriver
import time

with open('user_pwd.txt') as f:
    user_str = f.readline()
    password_str = f.readline()

  
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Firefox(executable_path ="C:\Python37\geckodriver")
from selenium.webdriver.common.action_chains import ActionChains
#2.通过浏览器向服务器发送URL请求
browser.get("http://i.ameco.com.cn/login.jsp")

time.sleep(3)
username = browser.find_element_by_name('userName')
username.send_keys(user_str)
pwd = browser.find_element_by_name('pwd')
pwd.send_keys(password_str)
submit = browser.find_element_by_name('submit')
submit.click()

time.sleep(3)
cms = browser.find_element_by_id('menu-lv1-095')
ActionChains(browser).move_to_element(cms).perform()
time.sleep(2)
browser.find_element_by_id('095002').click()
time.sleep(2)
nav = browser.find_element_by_id('nav_width_a')
ActionChains(browser).move_to_element(nav).perform()

#进入左侧组织树的frame
browser.switch_to.frame(4)
browser.find_element_by_xpath("//span[contains(text(),'重庆分公司门户')]").click()
time.sleep(2)
browser.find_element_by_xpath("//span[contains(text(),'组织机构')]").click()
time.sleep(2)
browser.find_element_by_xpath("//span[contains(text(),'生产部门')]").click()
time.sleep(2)
browser.find_element_by_xpath("//span[contains(text(),'航空安全质量分部')]").click()
time.sleep(2)
#进入到操作界面
browser.switch_to.frame('frame')


#创建项目按钮
browser.find_element_by_css_selector("button.btn.btn-info").click()
#暂停时间=5时，太长会出现已有一个主机连接的错误《ConnectionAbortedError:[WinError 10053] 你的主机中的软件中止了一个已建立的连接。》
time.sleep(3)
#填写项目信息

#进入到项目窗的frame
browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'4029')]"))
browser.find_element_by_id("chnlIdentity").clear()
browser.find_element_by_id("chnlIdentity").send_keys("CQHQAQZLFBJS")
browser.find_element_by_id("sortNo").clear()
browser.find_element_by_id("sortNo").send_keys("0")
browser.find_element_by_id("pageSize").clear()
browser.find_element_by_id("pageSize").send_keys("0")
browser.find_element_by_id("chnlName").clear()
browser.find_element_by_id("chnlName").send_keys(u"分部介绍")

#退回到操作界面的frame
#browser.switch_to.parent_frame()
browser.find_element_by_class_name("btn btn-primary").click()


#回到顶层frame
#browser.switch_to.default_content()
#browser.fill('userName','00371747')
#browser.fill('pwd','WATER13a')
#browser.find_by_name('submit').click()