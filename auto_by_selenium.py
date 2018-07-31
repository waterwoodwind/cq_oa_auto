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

browser.switch_to.frame(4)
browser.find_element_by_id('ztree_7_ico').click()
time.sleep(2)
browser.switch_to.frame('frame')
#以上已经进入到重庆分公司的操作界面

#创建项目按钮
browser.find_element_by_css_selector("button.btn.btn-info").click()

browser.switch_to.default_content()
#browser.fill('userName','00371747')
#browser.fill('pwd','WATER13a')
#browser.find_by_name('submit').click()