# coding=utf-8
import re
import time
import sys
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\common_modules')
import time
import re
import random
import common_modules.globalvar as globalvar
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common_modules.common_action import Setup, SwitchToFrame, Time, Button, CommonAction


def qqq():
    # 删除草稿
    food_new_template_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = food_new_template_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
    url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/publicRecord/my_record_list.jsp?parentId=food')
    driver.get(url)
    driver.find_element_by_id("grid_length").click()
    driver.find_element_by_xpath("//option[@value='100']").click()
    i = 5
    while 1:
        driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[12]/button[2]' % i).click()
        driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        try:
            time.sleep(1)
            driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        except:
            pass
        #i += 1
qqq()
