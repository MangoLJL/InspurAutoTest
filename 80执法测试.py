#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
base_url=("http://10.12.1.80/portal/jsp/public/login.jsp")
driver=webdriver.Chrome(executable_path=(r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'))		
driver.get(base_url)
driver.find_element_by_id("j_username").send_keys("YUANGONG01")
driver.find_element_by_id("j_password").send_keys("1")
time.sleep(3)
driver.find_element_by_xpath("//button[@id='form-ok']").click()
time.sleep(3)
driver.find_element_by_xpath("//span[@class='applyText'][contains(text(),'政务办公')]").click()
driver.find_element_by_xpath("//a[@id='000000000000000000000000018266']//i[@class='fa fa-file-text-o circle fa-2x fa-blue']").click()
driver.get("http://10.12.1.80/el/jsp/enforcelaw_bs/caseDeal/cform/tasklist/newTask/newTask_index.jsp")
driver.find_element_by_xpath("//li[@biztype='01']").click()