# -*- coding: utf-8 -*-
__author__ = 'QB'
from selenium import webdriver

driver = webdriver.Chrome()  # 谷歌浏览器
# driver = webdriver.Firefox() # 火狐浏览器

driver.implicitly_wait(3)  # 设置隐式等待时间
driver.get('https://mail.qq.com/')

username = 'username'  # QQ账号
password = 'password'  # QQ密码

# 选择基本版
driver.find_element_by_xpath('/html/body/div/div[1]/div/a[1]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("//*[@id='u']").clear()  # 清空输入框
driver.find_element_by_xpath("//*[@id='u']").send_keys(username)  # 输入账号
driver.find_element_by_xpath("//*[@id='p']").clear()  # 清空输入框
driver.find_element_by_xpath("//*[@id='p']").send_keys(username)  # 输入密码
driver.find_element_by_xpath("//*[@id='go']").click()  # 登录
