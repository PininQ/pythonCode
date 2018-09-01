# -*- coding: utf-8 -*-
__author__ = 'QB'
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://qzone.qq.com/')

username = 'username'
password = 'password'

frame = driver.find_element_by_id('login_frame')
driver.switch_to.frame(frame)
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()  # 选择账号密码登录
driver.find_element_by_xpath('//*[@id="u"]').clear()
driver.find_element_by_xpath('//*[@id="u"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="p"]').clear()
driver.find_element_by_xpath('//*[@id="p"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="login_button"]').click()
