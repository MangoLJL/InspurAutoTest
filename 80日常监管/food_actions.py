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
    def setup_driver(self):
        chrome_option = Options()
        # chrome_option.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=(r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'), chrome_options=chrome_option)
        driver.maximize_window()
        self.driver = driver
        self.driver.get(self.url)
        self.driver.find_element_by_id("j_username").send_keys("wangweixuan")
        self.driver.find_element_by_id("j_password").send_keys("1")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@id='form-ok']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[@class='applyText'][contains(text(),'智慧监管')]").click()
        self.driver.find_element_by_id("000000000000000000000000019445").click()
        return driver


class LoginAndClick(object):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def login_and_click(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id("j_username").send_keys("wangweixuan")
        self.driver.find_element_by_id("j_password").send_keys("1")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@id='form-ok']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[@class='applyText'][contains(text(),'智慧监管')]").click()
        self.driver.find_element_by_id("000000000000000000000000019445").click()


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


class NewCheck(object):

    def __init__(self, driver):
        self.driver = driver

    def click_food_new_check(self):
        self.driver.find_element_by_id("menu-toggler").click()
        time.sleep(2)

        self.driver.find_element_by_id("000000000000000000000000019446").click()
        self.driver.find_element_by_id("000000000000000000000000019454").click()
        self.driver.find_element_by_id("check0101010001").click()

    def first_step(self):
        radio3 = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "radio3")))
        radio3.click()
        self.driver.find_element_by_id("firstBtn").click()

    def second_step(self):
        enterprise_selector = self.driver.find_element_by_id("enterpriseName")
        ActionChains(self.driver).double_click(enterprise_selector).perform()
        self.driver.switch_to.default_content()
        time.sleep(1)
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        enterprise_radio_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//html//tr[1]/td[2]/input[1]")))
        enterprise_radio_button.click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_id("secondBtn").click()

    def third_step(self):
        check_type_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "checkTypeCode0")))
        check_type_button.click()
        self.driver.find_element_by_xpath(
            "//tr[@id='nametr2']//td[@class='fieldInput']//div[@class='input-group']//span[@class='input-group-addon']//i[@class='fa fa-search']").click()
        self.driver.switch_to.default_content()
        time.sleep(1)
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        collect_tab = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#collection']")))
        collect_tab.click()
        self.driver.find_element_by_xpath("//html//tr[1]/td[2]/input[1]").click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.find_element_by_xpath("//table[@id='queryTable1']//tbody//tr//td[@class='queryTable-btn-td']//button[@id='save']").click()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_id("thirdhBtn").click()

    def fourth_step(self):
        question_sheet = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "card1")))
        question_sheet.click()
        self.driver.find_element_by_id("basicSituation").send_keys("sunhr测试用文字")
        self.driver.find_element_by_id("fourBtn").click()

    def fifth_step(self):
        checkResult0 = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "checkResult0")))
        checkResult0.click()
        self.driver.find_element_by_id("dealMethod0").click()
        self.driver.find_element_by_id("isShowInfo1").click()
        self.driver.find_element_by_id("fithBtn").click()

    def final_step(self):
        self.driver.find_element_by_xpath("//div[@class='common-btn']//button[@class='btn btn-success btn-sm']").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()

'''
class NewRandomDouble(object):
'''
