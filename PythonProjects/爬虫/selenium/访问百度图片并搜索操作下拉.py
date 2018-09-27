from selenium import webdriver
import time
url='https://image.baidu.com/'
browser=webdriver.Chrome()
browser.get(url)
input=browser.find_element_by_xpath('//*[@id="kw"]')
input.send_keys('T-ara')
time.sleep(2)
button=browser.find_element_by_xpath('//*[@id="homeSearchForm"]/span[2]')
button.click()
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     操作将进度条拉到最底部?
# browser.execute_script('alert("To Bottom")')?