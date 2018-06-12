import time
import re
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common_action import Setup, SwitchToFrame, Button, CommonAction, SendKeys


class SampleActions(object):

    def __init__(self, driver):
        self.driver = driver
        self.button = Button(self.driver)
        self.common_action = CommonAction(self.driver)
        self.send = SendKeys(self.driver)
        self.time = Time()

    def new_sample(self):
        self.button.click('shipinDiv')
        self.send('sampleBaseNo', time.get_log_time())
        self.button.click('//*[@id="selectPlansTr"]/td[2]/div[2]/div[1]/input')
        self.send('sourceDetail', time.get_log_time() + 'sunhr测试任务来源')
        self.button.click('sampleQDept')
        self.common_action.scroll_and_switch_to_iframe()
        self.button.click('//*[@id="grid"]/tbody/tr/td[2]/input')
        self.button.click_save_button()
        self.send('sampleQNum', '1')
        self.button.click('treeDemo_38_check')
