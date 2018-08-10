# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:29:13 2018

@author: 46979
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from learn_csv import get_config_list
from learn_csv import get_loc_options_list
import time

#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Firefox()

def login_in_oa():
    #2.通过浏览器向服务器发送URL请求
    browser.get("http://i.ameco.com.cn/login.jsp")
    browser.implicitly_wait(15)
    with open('user_pwd.txt') as f:
        user_str = f.readline()
        password_str = f.readline()
    username = browser.find_element_by_name('userName')
    username.send_keys(user_str)
    pwd = browser.find_element_by_name('pwd')
    pwd.send_keys(password_str)
    submit = browser.find_element_by_name('submit')
    submit.click()
    browser.implicitly_wait(15)
    
def into_tree(sub_name):
    cms = browser.find_element_by_id('menu-lv1-095')
    ActionChains(browser).move_to_element(cms).perform()
    time.sleep(2)
    browser.find_element_by_id('095002').click()
    time.sleep(2)
    nav = browser.find_element_by_id('nav_width_a')
    ActionChains(browser).move_to_element(nav).perform()
    time.sleep(1)
    #进入左侧组织树的frame
    browser.switch_to.frame(4)
    xpath_sub = "//span[contains(text(),'" + sub_name + "')]"
    browser.find_element_by_xpath(xpath_sub).click()
    time.sleep(2)
    
def switch_tree(loc_list):
    for loc in loc_list:
        xpath_str = "//span[contains(text(),'" + loc +"')]"
        browser.find_element_by_xpath(xpath_str).click()
        time.sleep(2)

def creat_item(options_list):
    #从上一层frame进入到操作界面
    browser.switch_to.frame('frame')
    #创建项目按钮
    browser.find_element_by_css_selector("button.btn.btn-info").click()
    #暂停时间=5时，太长会出现已有一个主机连接的错误《ConnectionAbortedError:[WinError 10053] 你的主机中的软件中止了一个已建立的连接。》
    time.sleep(3)
    
    #填写项目信息
    #进入到项目窗的frame
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'jsp?siteId=')]"))
    time.sleep(1)
    browser.find_element_by_id("chnlIdentity").clear()
    browser.find_element_by_id("chnlIdentity").send_keys(options_list[0])
    time.sleep(1)
    browser.find_element_by_id("chnlName").clear()
    browser.find_element_by_id("chnlName").send_keys(options_list[1])
    time.sleep(1)
    browser.find_element_by_id("sortNo").clear()
    browser.find_element_by_id("sortNo").send_keys(options_list[2])
    time.sleep(1)
    browser.find_element_by_id("folder").clear()
    browser.find_element_by_id("folder").send_keys(options_list[3])
    time.sleep(1)
    browser.find_element_by_id("pageSize").clear()
    browser.find_element_by_id("pageSize").send_keys(options_list[4])
    time.sleep(1)
    browser.find_element_by_id("topChnlName").clear()
    browser.find_element_by_id("topChnlName").send_keys(options_list[5])
    time.sleep(1)
    
    #选择框
    Select(browser.find_element_by_id("indexTpl")).select_by_visible_text(options_list[6])
    time.sleep(1)
    Select(browser.find_element_by_id("detailTpl")).select_by_visible_text(options_list[7])
    time.sleep(1)
    #退回到操作界面的frame
    browser.switch_to.parent_frame()
    #点击确定
    browser.find_element_by_xpath("html/body/div[3]/div/div/div[3]/button[2]").click()
    time.sleep(3)
    
if __name__ == "__main__":
    login_in_oa()
    config_list = get_config_list()
    for config_item in config_list:
        loc_list,options_list = get_loc_options_list(config_item)
        into_tree("呼和浩特分公司")
        switch_tree(loc_list)
        creat_item(options_list)
        browser.switch_to.default_content()
        browser.refresh()
        browser.implicitly_wait(15)
    into_tree("呼和浩特分公司")

#回到顶层frame
#browser.switch_to.default_content()
#browser.find_by_name('submit').click()