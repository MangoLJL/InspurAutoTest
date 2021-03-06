# coding=utf-8
import sys
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\common_modules')
import time
import re
import random
import traceback
import common_modules.globalvar as globalvar
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common_modules.common_action import Setup, SwitchToFrame, Time, Button, CommonAction

globalvar._init()


class NewCheck(object):
    # 新建检查

    def __init__(self, driver):
        self.driver = driver
        self.button = Button(self.driver)
        self.common_action = CommonAction(self.driver)

    def first_step(self, radio_index):
        radiobuttonindex = 'radio' + str(radio_index)
        radiobutton = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, radiobuttonindex)))
        radiobutton.click()
        self.driver.find_element_by_id("firstBtn").click()

    def second_step(self):
        enterprise_selector = self.driver.find_element_by_id("enterpriseName")
        ActionChains(self.driver).double_click(enterprise_selector).perform()  # 双击
        self.driver.switch_to.default_content()
        time.sleep(1)
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        time.sleep(3)
        data_exsists = self.common_action.data_exsists()
        if data_exsists:
            random_enterprise = random.randint(1, 5)
            enterprise_name = self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[3]/span' % random_enterprise).text
            print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '检查的企业为' + enterprise_name)
            enterprise_radio_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//html//tr[%s]/td[2]/input[1]" % random_enterprise)))
            enterprise_radio_button.click()
            self.button.click_save_button()
            time.sleep(1)
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("mainFrame")
            self.driver.find_element_by_id("secondBtn").click()
            return True
        else:
            return False

    def third_step(self, checktype):
        check_type_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, checktype)))
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
        time.sleep(1)
        self.driver.find_element_by_id("thirdhBtn").click()

    def fourth_step_check_template(self, template_ID):
        # 使用检查模板
        self.driver.find_element_by_id(template_ID).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//input[@class='clauseRes'][2]").click()
        # self.driver.find_element_by_xpath("//input[@class='clauseRes'][last()]").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-default btn-xs']").click()
        time.sleep(1)
        self.common_action.scroll_and_switch_to_iframe()
        check_describe = ("%ssunhr问题描述" % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        self.driver.find_element_by_id("checkDescribe").send_keys('$' + check_describe + '$')
        self.button.click_save_button()
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_xpath("//input[@class='scoreValue']").send_keys('66')
        self.driver.find_element_by_id("fourBtn").click()
        return check_describe

    def fourth_step_check_situation(self):
        # 使用检查情况
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "card2"))).click()
        self.button.click('//*[@id="jcbnr"]/div[1]/label/a')
        question_sheet = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "card1")))
        question_sheet.click()
        self.driver.find_element_by_id("basicSituation").click()
        time.sleep(0.8)
        self.button.click_confirm_button()
        self.driver.switch_to.frame("mainFrame")
        check_situation = ("【" + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "】sunhr测试用文字")
        self.driver.find_element_by_id("basicSituation").send_keys(check_situation)
        self.driver.find_element_by_id("fourBtn").click()
        return check_situation

    def fifth_step(self):
        checkResult0 = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "checkResult1")))
        checkResult0.click()
        self.driver.find_element_by_id("dealMethod5").click()
        self.driver.find_element_by_id("isShowInfo1").click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_id("fithBtn").click()

    def final_step(self):
        self.driver.find_element_by_xpath("//div[@class='common-btn']//button[@class='btn btn-success btn-sm']").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()

    def confirm_new_check_check_situation(self, check_situation):
        # 确认使用检查情况来检查的事项的情况
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
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '测试通过')
            return True
        else:
            return False

    def confirm_new_check_check_template(self, check_describe):
        # 确认使用检查模板进行检查的事项的情况
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
        current_describe = self.driver.find_element_by_id("gridClause").text
        current_describe_suits = current_describe.split('$')
        current_describe = current_describe_suits[1]
        if current_describe == check_describe:
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '测试通过')
            return True
        else:
            return False

    def confirm_save_as_draft(self, check_situation):
        # 确认草稿保存成功
        url = 'http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/publicRecord/my_record_list.jsp?parentId=food'
        self.driver.get(url)
        target = self.common_action.find('span', '草稿')
        finaltarget = target.parent
        for i in range(10):
            finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.get_text()
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[3]/a' % finaltarget).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.switch_to.default_content()
        time.sleep(5)
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        current_situation = self.driver.find_element_by_id("basicSituation").text
        if current_situation == check_situation:
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '测试通过')
            return True
        else:
            return False

    def delete_draft(self):
        # 删除草稿
        url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/publicRecord/my_record_list.jsp?parentId=food')
        self.driver.get(url)
        '''
        driver.find_element_by_id("grid_length").click()
        driver.find_element_by_xpath("//option[@value='100']").click()
        '''
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[1]/td[12]/button[2]').click()
        self.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        except:
            pass


class NewDoubleRandom(object):
    # 双随机任务新建并发起检查

    def __init__(self, driver):
        self.driver = driver
        self.button = Button(self.driver)
        self.common_action = CommonAction(self.driver)

    def create_new_random_task(self):
        # 新建双随机任务
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary btn-sm']").click()
        time.sleep(3)
        task_name = ("%ssunhr测试双随机" % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        self.driver.find_element_by_id("planName").send_keys(task_name)
        self.driver.find_element_by_id("planCode").send_keys(time.strftime('%Y%m%d', time.localtime(time.time())))
        self.driver.find_element_by_id("radio3").click()
        self.driver.find_element_by_id("s2id_checkTypeCode").click()
        self.driver.find_element_by_id("select2-results-1").click()
        self.button.click_calendar_start_button()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//html//div[3]/div[3]/table[1]/tbody[1]/tr[1]/td[1]").click()
        self.button.click_calendar_end_button()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//html//div[4]/div[3]/table[1]/tbody[1]/tr[5]/td[7]").click()
        '''
        self.driver.find_element_by_id("DeptName").click()  # 被检查单位/部门
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        time.sleep(3)
        self.driver.find_element_by_id("organTree_1_check").click()
        self.button.click_save_button()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        self.driver.switch_to.frame("mainFrame")
        '''
        self.driver.find_element_by_id("planTemplateName").click()  # 指定检查表模板
        self.driver.switch_to.default_content()
        time.sleep(1)
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[1]/td[2]/input').click()
        self.button.click_save_button()
        time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame("mainFrame")

        self.driver.find_element_by_id("planContent").send_keys("【%s】sunhr测试双随机任务概要" % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        self.driver.find_element_by_xpath("//a[@href='#planEntInfo']").click()
        time.sleep(3)
        self.button.click('s2id_mainEntCityRegion')
        self.button.click("//li[@class='select2-results-dept-0 select2-result select2-result-selectable'][4]")
        time.sleep(1)
        self.driver.find_element_by_id("mainEntAmount").send_keys("10")
        self.driver.find_element_by_id("mainEntRadomButton").click()
        try:
            self.driver.find_element_by_xpath("//a[@href='#planPersonInfo']").click()
        except Exception as e:
            print('企业列表未正确加载或有报错，错误信息：')
            traceback.print_exc()
        time.sleep(3)
        self.driver.find_element_by_id("checkPersonAmount").send_keys("387")
        self.driver.find_element_by_id("groupingNum").send_keys("1")
        self.driver.find_element_by_id("checkPersonRadomButton").click()
        self.button.click_confirm_button()
        self.driver.switch_to.frame("mainFrame")
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
            print('员工列表可能加载有误，错误信息：')
            traceback.print_exc()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-success'][last()]").click()
        time.sleep(5)
        # 此处应该增加错误判断====================
        self.button.click_confirm_button()
        self.driver.quit()
        print(task_name)
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
        else:
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "双随机计划创建成功,开始签收")
            finaltarget = target.parent
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.get_text()
            self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[13]/button' % finaltarget).click()
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            self.driver.switch_to.default_content()
            self.button.click_confirm_button()
            time.sleep(1)
            print(self.driver.find_element_by_xpath("//div[@class='layui-layer-content layui-layer-padding']").text)
            self.button.click_confirm_button()
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "双随机任务接收成功")

    def check_new_random_test(self, task_name):
        # 以下步骤为根据创建的双随机计划建立检查
        url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/basic/publicRecord/my_record_task_list.jsp?parentId=food')
        self.driver.get(url)
        target = self.common_action.find('a', task_name)
        finaltarget = target.parent
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.get_text()
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[12]/button' % finaltarget).click()
        try:
            enterprise_name = '未选择'
            enterprise_selector = self.driver.find_element_by_id("enterpriseName")
            ActionChains(self.driver).double_click(enterprise_selector).perform()
            self.driver.switch_to.default_content()
            time.sleep(1)
            iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
            self.driver.switch_to.frame(iframe)
            random_enterprise = random.randint(1, 5)
            enterprise_radio_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//html//tr[%s]/td[2]/input[1]" % random_enterprise)))
            enterprise_name = self.driver.find_element_by_xpath("//html//tr[%s]/td[3]" % random_enterprise).text
            enterprise_radio_button.click()
            self.button.click_save_button()
            time.sleep(1)
            self.driver.switch_to.default_content()
            try:
                self.driver.find_element_by_id("radio0").click()  # 选择食品经营企业时会出现两个radio button
            except:
                pass
            self.driver.find_element_by_id("firstBtn").click()
            check_type_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "checkTypeCode0")))
            check_type_button.click()
            self.driver.find_element_by_xpath("//*[@id='nametr1']/td/div[1]/span/i").click()
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
            self.driver.find_element_by_id("secondBtn").click()
            question_sheet = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "card1")))
            question_sheet.click()
            check_situation = ("【" + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "】sunhr测试用文字")
            self.driver.find_element_by_id("basicSituation").send_keys(check_situation)
            self.driver.find_element_by_id("thirdhBtn").click()
            checkResult0 = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "checkResult0")))
            checkResult0.click()
            self.driver.find_element_by_id("dealMethod0").click()
            self.driver.find_element_by_id("fourBtn").click()
            self.driver.find_element_by_xpath("//div[@class='common-btn']//button[@class='btn btn-success btn-sm']").click()
            self.button.click_confirm_button()
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "依据双随机任务新建检查已提交，检查企业为%s" % enterprise_name)
            return enterprise_name
        except Exception as e:
            self.common_action.get_screenshot("check_new_random_test")
            print("根据%s创建针对%s的流程失败" % (task_name, enterprise_name))
            traceback.print_exc()

    def confirm_random_enterprise_check(self, task_name, enterprise_name):
        # 确定根据双随机任务发起的检查建立成功
        try:
            url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkPlan/dtdcheckplansd_list.jsp?entParentId=food')
            self.driver.get(url)
            target = self.common_action.find('a', task_name)
            finaltarget = target.parent
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.get_text()
            self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[9]/a' % finaltarget).click()
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            self.driver.switch_to.default_content()
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
            self.driver.switch_to.frame(iframe)
            target = self.common_action.find('a', enterprise_name)
            if target != None:
                print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "依据双随机任务新建检查成功，检查企业为%s" % enterprise_name)
                return True
            else:
                return False
        except Exception as e:
            traceback.print_exc()
            return False


class NewNormalTask(object):
    # 普通任务发起并新建检查

    def __init__(self, driver):
        self.driver = driver
        self.button = Button(self.driver)
        self.common_action = CommonAction(self.driver)

    def create_task(self):
        # 新建普通任务
        self.button.click_plus_button()
        plan_name = (time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "sunhr测试计划")
        self.driver.find_element_by_id("planName").send_keys(plan_name)
        self.driver.find_element_by_id("select2-chosen-1").click()
        self.driver.find_element_by_id("select2-results-1").click()
        self.driver.find_element_by_id("radio3").click()
        self.driver.find_element_by_id("checkNumber").send_keys('66')
        self.button.click_calendar_start_button()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//html//div[3]/div[3]/table[1]/tbody[1]/tr[1]/td[1]").click()
        self.button.click_calendar_end_button()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//html//div[4]/div[3]/table[1]/tbody[1]/tr[5]/td[7]").click()
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
        # 确定普通任务新建成功
        try:
            url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkPlan/dtdcheckplansd_list.jsp?entParentId=food')
            self.driver.get(url)
            time.sleep(2)
            current_html = self.driver.page_source
            soup = BeautifulSoup(current_html, 'lxml')
            target = soup.find('a', string=re.compile(plan_name))
            if target == None:
                print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "获取普通任务%s失败，任务可能没有创建成功,当前页面截图已保存至confirm_new_normal_task.png" % plan_name)
                self.driver.get_screenshot_as_file("C:\\Users\\sunhaoran\\Desktop\\%sconfirm_new_normal_task.png" % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
                return False
            else:
                print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "普通任务创建成功,测试通过，任务名称为：" + plan_name)
                return True
        except Exception as e:
            traceback.print_exc()

    def receive_new_normal_task(self, plan_name):
        try:
            url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkPlan/dtdcheckplan_receive_list.jsp?entParentId=food')
            self.driver.get(url)
            time.sleep(2)
            target = self.common_action.find('a', plan_name)
            finaltarget = target.parent
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.get_text()
            self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[13]/button' % finaltarget).click()
            self.common_action.scroll_and_switch_to_iframe()
            self.driver.find_element_by_id('checkNumber').send_keys('1')
            self.button.click_save_button()
            self.button.click_confirm_button()
            time.sleep(1)
            self.button.click_confirm_button()
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "签收成功")
            self.driver.quit()
        except Exception as e:
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "签收失败，错误为：")
            traceback.print_exc()
            self.driver.quit()

    def create_normal_task_check(self, plan_name):
        # 针对新建的普通任务发起检查
        url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/basic/publicRecord/my_record_task_list.jsp?parentId=food')
        self.driver.get(url)
        self.button.click_search_button()
        time.sleep(2)
        target = self.common_action.find('a', plan_name)
        finaltarget = target.parent
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.get_text()
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[12]/button' % finaltarget).click()
        try:
            enterprise_name = '未选择'
            enterprise_selector = self.driver.find_element_by_id("enterpriseName")
            ActionChains(self.driver).double_click(enterprise_selector).perform()
            self.driver.switch_to.default_content()
            time.sleep(1)
            iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
            self.driver.switch_to.frame(iframe)
            enterprise_radio_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//html//tr[1]/td[2]/input[1]")))
            enterprise_name = self.driver.find_element_by_xpath("//html//tr[1]/td[3]").text
            enterprise_radio_button.click()
            self.button.click_save_button()
            time.sleep(1)
            self.driver.switch_to.default_content()
            try:
                self.driver.find_element_by_id("radio0").click()  # 选择食品经营企业时会出现两个radio button
            except:
                pass
            self.driver.find_element_by_id("firstBtn").click()
            check_type_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "checkTypeCode0")))
            check_type_button.click()
            self.driver.find_element_by_xpath("//*[@id='nametr2']/td/div[1]/span/i").click()
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
            self.driver.find_element_by_id("secondBtn").click()
            question_sheet = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "card1")))
            question_sheet.click()
            check_situation = ("【" + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "】sunhr测试用文字")
            self.driver.find_element_by_id("basicSituation").send_keys(check_situation)
            self.driver.find_element_by_id("thirdhBtn").click()
            checkResult0 = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "checkResult0")))
            checkResult0.click()
            self.driver.find_element_by_id("dealMethod0").click()
            self.driver.find_element_by_id("fourBtn").click()
            self.driver.find_element_by_xpath("//div[@class='common-btn']//button[@class='btn btn-success btn-sm']").click()
            self.button.click_confirm_button()
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "依据普通任务新建检查已提交，检查企业为【%s】" % enterprise_name)
            return enterprise_name
        except Exception as e:
            self.common_action.get_screenshot("check_new_random_test")
            print("根据普通任务【%s】创建针对【%s】的流程失败" % (plan_name, enterprise_name))
            traceback.print_exc()

    def confirm_normal_task_check(self, task_name, enterprise_name):
        # 确认针对普通任务发起的检查新建成功
        try:
            url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkPlan/dtdcheckplansd_list.jsp?entParentId=food')
            self.driver.get(url)
            target = self.common_action.find('a', task_name)
            finaltarget = target.parent
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.get_text()
            self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[9]/a' % finaltarget).click()
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            self.driver.switch_to.default_content()
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
            self.driver.switch_to.frame(iframe)
            target = self.common_action.find('a', enterprise_name)
            if target != None:
                print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "依据普通任务新建检查成功，检查企业为【%s】" % enterprise_name)
                return True
            else:
                return False
        except Exception as e:
            traceback.print_exc()


class Template(object):

    def __init__(self, driver):
        self.driver = driver
        self.button = Button(self.driver)
        self.common_action = CommonAction(self.driver)

    def create_template(self):
        self.button.click_plus_button()
        template_name = ("%ssunhr测试模板" % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        self.driver.find_element_by_id('templateName').send_keys(template_name)
        self.driver.find_element_by_id('radio1').click()
        self.driver.find_element_by_id('radio3').click()
        self.driver.find_element_by_id('radio4').click()
        self.driver.find_element_by_id('radio5').click()
        self.driver.find_element_by_id('radio6').click()
        self.driver.find_element_by_id('radio7').click()
        # self.driver.find_element_by_id('checkTableType0').click()
        self.driver.find_element_by_id('isPeriod1').click()
        self.driver.find_element_by_id('checkProgramNum').send_keys('1')
        self.driver.find_element_by_id('DeptName').click()
        self.common_action.scroll_and_switch_to_iframe()
        self.button.click_plus_button()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        iframe2 = self.driver.find_element_by_xpath("(//iframe[contains(@id,'layui-layer-iframe')])[last()]")
        self.driver.switch_to.frame(iframe2)
        self.driver.find_element_by_id("organTree_1_check").click()
        self.driver.find_element_by_id("save").click()  # 选择部门之后点击保存\
        self.driver.switch_to.default_content()
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        self.button.click_edit_button()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_id('displayColumn0').click()
        self.driver.find_element_by_id('displayColumn1').click()
        self.driver.find_element_by_id('displayColumn2').click()
        self.driver.find_element_by_id('displayColumn3').click()
        self.driver.find_element_by_id('displayColumn4').click()
        self.driver.find_element_by_id('displayColumn5').click()
        self.driver.find_element_by_id('displayColumn6').click()
        iframe = self.driver.find_element_by_id('frameName')
        self.driver.switch_to.frame(iframe)
        self.button.click_plus_button()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr/td[3]/div/span/i').click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.switch_to.default_content()
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_id('modelTree_2_check').click()
        self.button.click_save_button()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr/td[4]/input').send_keys('1')
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr/td[5]/div/span/i').click()
        self.common_action.scroll_and_switch_to_iframe()
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[3]/td[2]/input').click()
        self.button.click_save_button()
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.button.click('clauseLevel')
        self.button.click('//*[@id="clauseLevel"]/option[2]')
        self.button.click('//*[@id="grid"]/tbody/tr/td[8]/div[1]/span')
        self.common_action.scroll_and_switch_to_iframe()
        self.button.click('//*[@id="grid"]/tbody/tr[1]/td[2]/input')
        self.button.click_save_button()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr/td[7]/input').send_keys(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + 'sunhr测试检查要求')
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr/td[11]/input').send_keys('100')
        iframe = self.driver.find_element_by_id('frameName')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_id('bts').click()
        self.button.click_confirm_button()
        globalvar.set_value('food_template_name', template_name)
        return template_name

    def confirm_new_template(self, template_name):
        # 此处的原理为：
        # 因为业务上的测试需求是“建一个模板，然后根据模板走一个检查”，因此要在建立模板后现场检查时候定位到建立的模板。
        # 分析选择模板时候的元素【<a id="8ab200a664eac8230164f58b7da62d20" onclick="getDisplayColumn('8ab200a664eac8230164f58b7da62d20')"> 创城、创卫餐饮检查表<font style="color:orange;"></font> </a>】
        # 可见里边有一个ID，经过分析此ID会在模板列表中的herf中显示为【<a data-toggle="tooltip" title="" href="javascript:detail('8a8c81d1656b2f3a01656f4eac2803e0','01')" data-original-title="9527模板">9527模板</a>】
        # 因此只需要截取到herf中的id，现场录入时直接通过id定位即可
        url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkTemplate/dtdcheckftemplate_list.jsp?entParentId=food')
        self.driver.get(url)
        current_template_name = self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[1]/td[3]/a').text
        if current_template_name == template_name:
            # 获取herf内的字段如【javascript:detail('8a8c81d1656b2f3a01656f4eac2803e0','01')】
            current_template_ID = str(self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[1]/td[3]/a').get_attribute('href'))
            template_ID_suits = current_template_ID.split('\'')  # 通过【'】分割成四段【javascript:detail(】、【8a8c81d1656b2f3a01656f4eac2803e0】、【,】、【01】
            template_ID = template_ID_suits[1]  # 取第一段即为id
            globalvar.set_value('food_template_ID', template_ID)  # 通过globalvar存下来
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '新建模板成功，测试通过')
            return True
        else:
            print("查找新建模板【%s】失败，当前截图已保存为confirm_new_template_error" % template_name)
            driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\食品日常检查\\error_screenshot\\%sconfirm_new_template_error.png" %
                                          time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
            return False

    def clean_template(self):
        url = 'http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkTemplate/dtdcheckftemplate_list.jsp?entParentId=food'
        self.driver.get(url)
        template_name = globalvar.get_value('food_template_name')
        current_html = self.driver.page_source
        target = self.common_action.find('a', template_name)
        finaltarget = target.parent
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.get_text()
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[8]/button[4]' % finaltarget).click()
        self.button.click_confirm_button()
        time.sleep(0.5)
        self.button.click_confirm_button()
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[8]/button[2]' % finaltarget).click()
        iframe = self.driver.find_element_by_xpath('/html/body/iframe[1]')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_id("btt").click()
        self.button.click_confirm_button()
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[8]/button[5]' % finaltarget).click()
        self.button.click_confirm_button()
        time.sleep(0.5)
        self.button.click_confirm_button()
        print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '清理食品模板完成')
