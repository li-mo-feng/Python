from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.support.wait import  WebDriverWait
brownser=webdriver.Chrome()
try:
    brownser.get('http://www.baidu.com')
    # get方法访问页面地址
    input=brownser.find_element_by_id('kw')
    input.send_keys('python')
    # 发送搜索结果
    input.send_keys(Keys.ENTER)
    # 按键（enter）开始搜索
    wait=WebDriverWait(brownser,10)
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(brownser.current_url)
    print(brownser.get_cookies())
    print(brownser.page_source)
finally:
    brownser.close()