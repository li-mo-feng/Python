from selenium import webdriver
import time
url='https://www.bilibili.com/'

browser=webdriver.Chrome()
browser.get(url)
input=browser.find_element_by_css_selector('#banner_link > div > div > form > input')
# id选择器
# input_second=browser.find_element_by_css_selector('#q')
# css选择器
# input_third=browser.find_element_by_xpath('//*[@id="q"]')
# xpath选择器
input.send_keys('凹凸曼')
time.sleep(1)
input.clear()
input.send_keys('T-ara')
button=browser.find_element_by_xpath('//*[@id="banner_link"]/div/div/form/button')
button.click()
browser.close()