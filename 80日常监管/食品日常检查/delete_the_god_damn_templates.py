# coding=utf-8
import re
import time
import globalvar
from functools import reduce
from food_actions import NewCheck, NewDoubleRandom, NewNormalTask, NewTemplate
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from common_action import Setup, SwitchToFrame, Button, CommonAction


def qqq():
    food_new_template_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = food_new_template_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
    url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkTemplate/dtdcheckftemplate_list.jsp?entParentId=food&cancelUser=null')
    driver.get(url)
    self.driver.find_element_by_id("grid_length").click()
    self.driver.find_element_by_xpath("//option[@value='100']").click()
    i = 1
    while 1:
        driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[i]/td[8]/button[4]')
        driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        i += 1
