from selenium import webdriver
import time
while True:
    option=webdriver.ChromeOptions()
    option.add_argument("headless")
    browser=webdriver.Chrome(chrome_options=option)
    # browser=webdriver.Chrome()
    url1='http://192.168.1.1'
    # 路由器地址
    browser.get(url1)
    input1=browser.find_element_by_id('user_name')
    input2=browser.find_element_by_id('password')
    input1.send_keys('user')
    input2.send_keys('knc9a')
    button=browser.find_element_by_id('login_btn')
    button.click()
    # 模拟登陆
    time.sleep(3)
    sreach_window=browser.current_window_handle
    # 页面原地跳转重新定位
    man_button=browser.find_element_by_id("Menu1_Management")
    man_button.click()
    time.sleep(3)
    # 进入路由器管理界面
    sreach_window2=browser.current_window_handle
    man_button2=browser.find_element_by_id("Menu2_Mng_Device")
    man_button2.click()
    time.sleep(3)
    sreach_window3=browser.current_window_handle
    man_button3=browser.find_element_by_id("Restart_button")
    man_button3.click()
    time.sleep(3)
    # 进入硬件管理
    al = browser.switch_to_alert()
    al.accept()
    time.sleep(3)
    browser.close()
    # 确定弹窗
    time.sleep(120)
#     三分钟断一次网！+_+






