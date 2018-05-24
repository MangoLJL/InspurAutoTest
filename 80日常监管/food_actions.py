# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from common_action import Time, Button
import time


class NewCheck(object):

    def __init__(self, driver):
        self.driver = driver
        timer = Time()
        self.log_time = timer.get_log_time()
        self.current_week = timer.get_current_week()
        self.current_date = timer.get_current_date()

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
        self.driver.find_element_by_id("basicSituation").send_keys("【%s】sunhr测试用文字" % self.log_time)
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


class NewDoubleRandom(object):

    def __init__(self, driver):
        self.driver = driver
        timer = Time()
        self.log_time = timer.get_log_time()
        self.current_week = timer.get_current_week()
        self.current_date = timer.get_current_date()
        self.button = Button(self.driver)

    def new_random_task(self):
        self.button.click_plus_button()
        time.sleep(10)
        self.driver.find_element_by_id("planName").send_keys("【%s】sunhr测试双随机" % self.current_date)
        self.driver.find_element_by_id("planCode").send_keys(self.current_date)
        self.driver.find_element_by_id("radio0").click()
        self.driver.find_element_by_id("s2id_checkTypeCode").click()
        self.driver.find_element_by_id("select2-results-1").click()
        self.button.click_calendar_start_button()
        self.driver.find_element_by_xpath("//html//div[3]/div[3]/table[1]/tbody[1]/tr[4]/td[5]").click()
        self.button.click_calendar_end_button()
        self.driver.find_element_by_xpath("//html//div[4]/div[3]/table[1]/tbody[1]/tr[4]/td[5]").click()
        self.driver.find_element_by_id("planContent").send_keys("【%s】sunhr测试双随机任务概要" % self.current_date)
        self.driver.find_element_by_xpath("//a[@href='#planEntInfo']").click()
        time.sleep(3)
        listbox = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "select2-chosen-2")))
        listbox.click()
        self.driver.find_element_by_id("select2-result-label-79").click()
        self.driver.find_element_by_id("mainEntAmount").send_keys("10")
        self.driver.find_element_by_id("mainEntRadomButton").click()
        self.driver.find_element_by_xpath("//a[@href='#planPersonInfo']").click()
        self.driver.find_element_by_id("checkPersonAmount").send_keys("300")
        self.driver.find_element_by_id("checkPersonRadomButton").click()
        queryMoreCountMainLi = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "queryMoreCountMainLi")))
        queryMoreCountMainLi.click()
        #//span[@data - toggle = 'tooltip'][contains(text(), '刘宝祥')]
        print(self.driver)
        time.sleep(100)
