# coding=utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from common_action import Setup, SwitchToFrame
from common_action import Time, Button
import time
import re


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
        collect_tab = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#collection']")))
        collect_tab.click()
        self.driver.find_element_by_xpath("//html//tr[1]/td[2]/input[1]").click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.find_element_by_xpath("//table[@id='queryTable1']//tbody//tr//td[@class='queryTable-btn-td']//button[@id='save']").click()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_id("thirdhBtn").click()

    def fourth_step(self):

        question_sheet = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "card1")))
        question_sheet.click()
        check_situation = ("【" + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "】sunhr测试用文字")
        self.driver.find_element_by_id("basicSituation").send_keys(check_situation)
        self.driver.find_element_by_id("fourBtn").click()
        return check_situation

    def fifth_step(self):
        checkResult0 = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "checkResult0")))
        checkResult0.click()
        self.driver.find_element_by_id("dealMethod0").click()
        self.driver.find_element_by_id("isShowInfo1").click()
        self.driver.find_element_by_id("fithBtn").click()

    def final_step(self):
        self.driver.find_element_by_xpath("//div[@class='common-btn']//button[@class='btn btn-success btn-sm']").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()

    def confirm_new_check(self, check_situation):
        url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/publicRecord/my_record_list.jsp?parentId=food')
        self.driver.get(url)
        self.driver.find_element_by_id("grid_length").click()
        self.driver.find_element_by_xpath("//option[@value='100']").click()
        current_html = self.driver.page_source
        soup = BeautifulSoup(current_html, 'lxml')
        target = soup.find('span', string=re.compile('提交'))
        finaltarget = target.parent
        for i in range(0, 10):
            finaltarget = finaltarget.previous_sibling
        self.driver.find_element_by_xpath("//html//tr[%s]/td[3]/a[1]" % finaltarget.get_text()).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.switch_to.default_content()
        time.sleep(5)
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        current_situation = self.driver.find_element_by_id("basicSituation").text
        if current_situation == check_situation:
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '食品新建日常检查流程测试成功，测试通过')
            return True
        else:
            return False


class NewDoubleRandom(object):

    def __init__(self, driver):
        self.driver = driver
        timer = Time()
        self.log_time = timer.get_log_time()
        self.current_week = timer.get_current_week()
        self.current_date = timer.get_current_date()
        self.button = Button(self.driver)

    def create_new_random_task(self):
        self.button.click_plus_button()
        task_name = ("%ssunhr测试双随机" % self.log_time)
        self.driver.find_element_by_id("planName").send_keys(task_name)
        self.driver.find_element_by_id("planCode").send_keys(self.current_date)
        self.driver.find_element_by_id("radio0").click()
        self.driver.find_element_by_id("s2id_checkTypeCode").click()
        self.driver.find_element_by_id("select2-results-1").click()
        self.button.click_calendar_start_button()
        self.driver.find_element_by_xpath("//html//div[3]/div[3]/table[1]/tbody[1]/tr[4]/td[5]").click()
        self.button.click_calendar_end_button()
        self.driver.find_element_by_xpath("//html//div[4]/div[3]/table[1]/tbody[1]/tr[4]/td[5]").click()
        self.driver.find_element_by_id("planContent").send_keys("【%s】sunhr测试双随机任务概要" % self.log_time)
        self.driver.find_element_by_xpath("//a[@href='#planEntInfo']").click()
        time.sleep(3)
        self.driver.find_element_by_id("mainEntAmount").send_keys("10")
        self.driver.find_element_by_id("mainEntRadomButton").click()
        try:
            self.driver.find_element_by_xpath("//a[@href='#planPersonInfo']").click()
        except Exception as e:
            print('企业列表未正确加载或有报错', e)
        time.sleep(3)
        self.driver.find_element_by_id("checkPersonAmount").send_keys("387")
        self.driver.find_element_by_id("groupingNum").send_keys("1")
        self.driver.find_element_by_id("checkPersonRadomButton").click()
        queryMoreCountMainLi = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "queryMoreCountMainLi")))
        queryMoreCountMainLi.click()
        current_html = self.driver.page_source
        soup = BeautifulSoup(current_html, 'lxml')
        try:
            target = soup.find('span', string=re.compile('刘宝祥'))  # 查找到员工01的位置，获取编号
            targetparent = target.parent
            targetparentbrother = targetparent.previous_sibling
            finaltarget = targetparentbrother.previous_sibling
            employee_number = finaltarget.get_text()
            self.driver.find_element_by_xpath("//html//tr[%s]/td[8]/button[1]" % employee_number).click()  # 根据获取到编号的XPATH点击设为组长按钮
        except Exception as e:
            print('员工列表可能加载有误', e)
        time.sleep(1)
        self.button.click_save_button()
        time.sleep(5)
        self.button.click_confirm_button()
        driver.quit()
        return task_name

    def receive_new_random_test(self, task_name):
        # 以下步骤为登陆账号查看是否可以接收
        url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkPlan/dtdcheckplan_receive_list.jsp?entParentId=food')
        self.driver.get(url)
        time.sleep(2)
        current_html = self.driver.page_source
        soup = BeautifulSoup(current_html, 'lxml')
        target = soup.find('a', string=re.compile(task_name))
        if target == None:
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "获取双随机任务失败，任务可能没有创建成功")
            return False
        else:
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "双随机计划创建成功,开始签收")
            finaltarget = target.parent
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.get_text()
            self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[7]/button' % finaltarget).click()
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            self.driver.switch_to.default_content()
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
            self.driver.switch_to.frame(iframe)
            self.driver.find_element_by_id("checkNumber").send_keys("1")
            self.driver.find_element_by_xpath("//button[@class='btn btn-success btn-xs']").click()
            self.button.click_confirm_button()
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "双随机任务接收成功")

    def check_new_random_test(self, task_name):
        # 以下步骤为根据创建的双随机计划建立检查
        url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/basic/publicRecord/my_record_task_list.jsp?parentId=food')
        self.driver.get(url)
        time.sleep(2)

        def find_task(task_name):
            current_html = self.driver.page_source
            soup = BeautifulSoup(current_html, 'lxml')
            target = soup.find('a', string=re.compile(task_name))
            return target
        while 1:
            target = find_task(task_name)
            if target == None:
                try:
                    self.driver.find_element_by_id('grid_next').click()
                except Exception as e:
                    print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '根据双随机任务%s录入检查失败' % task_name)
            else:
                finaltarget = target.parent
                finaltarget = finaltarget.previous_sibling
                finaltarget = finaltarget.previous_sibling
                finaltarget = finaltarget.get_text()
                break
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[8]/button' % finaltarget).click()


class NewNormalTask(object):

    def __init__(self, driver):
        self.driver = driver
        self.button = Button(self.driver)

    def create_task(self):
        self.button.click_plus_button()
        plan_name = (time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "sunhr测试计划")
        self.driver.find_element_by_id("planName").send_keys(plan_name)
        self.driver.find_element_by_id("select2-chosen-1").click()
        self.driver.find_element_by_id("select2-results-1").click()
        self.driver.find_element_by_id("radio3").click()
        self.button.click_calendar_start_button()
        self.driver.find_element_by_xpath("//html//div[3]/div[3]/table[1]/tbody[1]/tr[1]/td[1]").click()
        self.button.click_calendar_end_button()
        self.driver.find_element_by_xpath("//html//div[4]/div[3]/table[1]/tbody[1]/tr[6]/td[7]").click()
        self.driver.find_element_by_id("DeptName").click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.switch_to.default_content()
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        self.button.click_plus_button()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        iframe2 = self.driver.find_element_by_xpath("(//iframe[contains(@id,'layui-layer-iframe')])[last()]")
        self.driver.switch_to.frame(iframe2)
        self.driver.find_element_by_id("organTree_1_check").click()
        self.driver.find_element_by_id("save").click()  # 选择部门之后点击保存
        self.driver.switch_to.default_content()
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        self.button.click_edit_button()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_id("planContent").send_keys("【" + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "】sunhr测试普通任务概要")
        self.driver.switch_to.frame("frameName")
        self.driver.find_element_by_xpath("(//i[@class='fa fa-save fa-fw'])[last()]").click()
        self.button.click_confirm_button()
        return plan_name

    def confirm_new_normal_task(self, plan_name):
        url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkPlan/dtdcheckplansd_list.jsp?entParentId=food')
        self.driver.get(url)
        time.sleep(2)
        current_html = self.driver.page_source
        soup = BeautifulSoup(current_html, 'lxml')
        target = soup.find('a', string=re.compile(plan_name))
        if target == None:
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "获取普通任务失败，任务可能没有创建成功,当前页面截图已保存至confirm_new_normal_task.png")
            self.driver.get_screenshot_as_file("C:\\Users\\sunhaoran\\Desktop\\%sconfirm_new_normal_task.png" % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
            return False
        else:
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "普通任务创建成功,测试通过")
            return True
