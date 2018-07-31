#coding=utf-8
from splinter import Browser
import time


global browser
browser = Browser()
browser.visit('http://i.ameco.com.cn/login.jsp')

username = browser.find_by_id('input1')
browser.fill('userName','#####')
browser.fill('pwd','#####')
browser.find_by_name('submit').click()
time.sleep(3)
browser.find_by_id('menu-lv1-095').mouse_over()
time.sleep(2)
browser.find_by_id('095002').click()
time.sleep(2)
browser.find_by_id('nav_width_a').mouse_over()
time.sleep(2)


#browser.quit()tee_tab
    