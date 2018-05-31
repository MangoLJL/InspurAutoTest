# coding=utf-8
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from common_action import Setup, SwitchToFrame, Button, CommonAction
import time
from common_action import Setup, SwitchToFrame, CommonAction
from food_actions import NewCheck, NewDoubleRandom, NewNormalTask


class NewDoubleRandom(object):

    def __init__(self, driver):
        self.driver = driver
        self.button = Button(self.driver)
        self.common_action = CommonAction(self.driver)

    def check_new_random_test(self, task_name):
        # 以下步骤为根据创建的双随机计划建立检查

        url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/basic/publicRecord/my_record_task_list.jsp?parentId=food')
        self.driver.get(url)
        self.common_action.find(task_name)
        finaltarget = target.parent
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.get_text()
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[8]/button' % finaltarget).click()
food_new_random_task_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
driver = food_new_random_task_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
nd = NewDoubleRandom(driver)
nd.check_new_random_test("20180530111854sunhr测试双随机")
