# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

# 建立驱动，选择系统，选择菜单


class Setup(object):

    def __init__(self, url):
        self.url = url

        # 连接浏览器驱动并选择所需要测试的系统
    def setup_driver(self, username, password, first_menu, second_menu):
        chrome_option = Options()
        # 是否选择以无头模式运行：可能使用不太正常
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
        try:
            self.driver.find_element_by_xpath("//span[@class='applyText'][contains(text(),'%s')]" % first_menu).click()
            if second_menu == '行政执法' or second_menu == '投诉举报' or second_menu == '风险预警' or second_menu == '分析标准' or second_menu == '移动服务' or second_menu == '考试信息':
                second_menu_class = 'extApply'
            else:
                second_menu_class = 'pic-font'
            self.driver.find_element_by_xpath("//span[@class='%s'][contains(text(),'%s')]" % (second_menu_class, second_menu)).click()
        except Exception as e:
            print('点击首页功能菜单失败，可能系统首页有报错，导致不能进行流程：', e)
        return driver

        # 选择左侧菜单
    def choose_menu(self, first_menu, second_menu, third_menu):
        button = Button(self.driver)
        time.sleep(10)
        try:
            button.click_confirm_button()
            print('系统首页测试到有错误弹窗')
        except:
            pass
        finally:
            self.driver.find_element_by_id("menu-toggler").click()
            time.sleep(1)

            self.driver.find_element_by_xpath("//span[@class='menu-text'][contains(text(),'%s')]" % first_menu).click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//span[@class='menu-text'][contains(text(),'%s')]" % second_menu).click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//span[@class='menu-text context-menu'][contains(text(),'%s')]" % third_menu).click()

# 切换Frame：MainFrame/default_content


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

# 获取当前日期，获取当前星期，获取当前日期和详细时间


class Time(object):

    def get_current_date(self):
        return time.strftime('%Y%m%d', time.localtime(time.time()))

    def get_current_week(self):
        return time.strftime('%w', time.localtime(time.time()))

    def get_log_time(self):
        return time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


class Button(object):

    def __init__(self, driver):
        self.driver = driver

    def click_plus_button(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='fa fa-plus']").click()
        time.sleep(5)

    def click_calendar_start_button(self):
        self.driver.find_element_by_id("checkStartDate").click()

    def click_calendar_end_button(self):
        self.driver.find_element_by_id("checkEndDate").click()

    def click_save_button(self):
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

    def click_confirm_button(self):
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
