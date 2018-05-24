# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


class Setup(object):

    def __init__(self, url):
        self.url = url

        # 连接浏览器驱动
    def setup_driver(self, username, password, first_menu, second_menu):
        chrome_option = Options()
        # chrome_option.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=(r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'), chrome_options=chrome_option)
        driver.maximize_window()
        self.driver = driver
        self.driver.get(self.url)
        self.driver.find_element_by_id("j_username").send_keys("%s" % username)
        self.driver.find_element_by_id("j_password").send_keys("%s" % password)
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@id='form-ok']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[@class='applyText'][contains(text(),'%s')]" % first_menu).click()
        if second_menu == '行政执法' or second_menu == '投诉举报' or second_menu == '风险预警' or second_menu == '分析标准' or second_menu == '移动服务' or second_menu == '考试信息':
            second_menu_class = 'extApply'
        else:
            second_menu_class = 'pic-font'
        self.driver.find_element_by_xpath("//span[@class='%s'][contains(text(),'%s')]" % (second_menu_class, second_menu)).click()
        return driver

        # 选择左侧菜单
    def choose_menu(self, first_menu, second_menu, third_menu):
        self.driver.find_element_by_id("menu-toggler").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[@class='menu-text'][contains(text(),'%s')]" % first_menu).click()
        self.driver.find_element_by_xpath("//span[@class='menu-text'][contains(text(),'%s')]" % second_menu).click()
        self.driver.find_element_by_xpath("//span[@class='menu-text context-menu'][contains(text(),'%s')]" % third_menu).click()


class SwitchToFrame(object):

    def __init__(self, driver):
        self.driver = driver

    def switch_to_main_frame(self):
        time.sleep(2)
        self.driver.switch_to.frame("mainFrame")
        time.sleep(1)

    def switch_to_default_content(self):
        time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(1)


class Time(object):

    def get_current_date(self):
        return time.strftime('%Y%m%d', time.localtime(time.time()))

    def get_current_week(self):
        return time.strftime('%w', time.localtime(time.time()))

    def get_log_time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
