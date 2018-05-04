#coding utf-8
#chorme headless Demo

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from time import sleep

chrome_options1=Options()
chrome_options1.add_argument("--headless")

base_url="http://www.baidu.com"
driver=webdriver.Chrome(executable_path=(r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'),chrome_options=chrome_options1)
driver.get(base_url + "/")

start_time=time.time()
print('this is start_time ',start_time)
driver.find_element_by_id("kw").send_keys("selenium webdriver")
driver.find_element_by_id("su").click()
sleep(3)
driver.save_screenshot('screen.png')

driver.close()

end_time=time.time()
print('this is end_time ',end_time)
