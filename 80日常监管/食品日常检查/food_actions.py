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
        ActionChains(self.driver).double_click(enterprise_selector).perform()
        self.driver.switch_to.default_content()
        time.sleep(1)
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        time.sleep(3)
        data_exsists = self.common_action.data_exsists()
        if data_exsists:
            enterprise_radio_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//html//tr[1]/td[2]/input[1]")))
            enterprise_radio_button.click()
            self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
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
        self.driver.find_element_by_id("thirdhBtn").click()

    def fourth_step(self):

        question_sheet = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "card1")))
        question_sheet.click()
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

    def confirm_new_check(self, check_situation, checktype):
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


class NewDoubleRandom(object):
    # 双随机任务新建并发起检查

    def __init__(self, driver):
        self.driver = driver
        self.button = Button(self.driver)
        self.common_action = CommonAction(self.driver)

    def create_new_random_task(self):
        # 新建双随机任务
        self.button.click_plus_button()
        task_name = ("%ssunhr测试双随机" % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        self.driver.find_element_by_id("planName").send_keys(task_name)
        self.driver.find_element_by_id("planCode").send_keys(time.strftime('%Y%m%d', time.localtime(time.time())))
        self.driver.find_element_by_id("radio0").click()
        self.driver.find_element_by_id("s2id_checkTypeCode").click()
        self.driver.find_element_by_id("select2-results-1").click()
        self.button.click_calendar_start_button()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//html//div[3]/div[3]/table[1]/tbody[1]/tr[1]/td[1]").click()
        self.button.click_calendar_end_button()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//html//div[4]/div[3]/table[1]/tbody[1]/tr[5]/td[7]").click()
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
        self.driver.find_element_by_id("planTemplateName").click()  # 指定检查表模板
        self.driver.switch_to.default_content()
        time.sleep(1)
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[3]/td[2]/input').click()
        self.button.click_save_button()
        time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame("mainFrame")

        self.driver.find_element_by_id("planContent").send_keys("【%s】sunhr测试双随机任务概要" % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        self.driver.find_element_by_xpath("//a[@href='#planEntInfo']").click()
        time.sleep(3)
        self.driver.find_element_by_id("mainEntAmount").send_keys("10")
        self.driver.find_element_by_id("mainEntRadomButton").click()
        try:
            self.driver.find_element_by_xpath("//a[@href='#planPersonInfo']").click()
        except Exception as e:
            print('企业列表未正确加载或有报错，错误信息：', e)
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
            print('员工列表可能加载有误，错误信息：', e)
        time.sleep(1)
        self.button.click_save_button()
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
        target = self.common_action.find(task_name)
        finaltarget = target.parent
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.get_text()
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[8]/button' % finaltarget).click()
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
            print(e)

    def confirm_random_enterprise_check(self, task_name, enterprise_name):
        # 确定根据双随机任务发起的检查建立成功
        url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkPlan/dtdcheckplansd_list.jsp?entParentId=food')
        self.driver.get(url)
        target = self.common_action.find(task_name)
        finaltarget = target.parent
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.get_text()
        self.driver.find_element_by_xpath('//html//tr[%s]/td[9]/a[1]' % finaltarget).click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
        target = self.common_action.find(enterprise_name)
        if target != None:
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "依据双随机任务新建检查成功，检查企业为%s" % enterprise_name)
            return True
        else:
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
            else:
                print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "普通任务创建成功,测试通过，任务名称为：" + plan_name)
                self.driver.quit()
        except Exception as e:
            print(e)

    def create_normal_task_check(self, plan_name):
        # 针对新建的普通任务发起检查
        url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/basic/publicRecord/my_record_task_list.jsp?parentId=food')
        self.driver.get(url)
        self.button.click_search_button()
        time.sleep(2)
        target = self.common_action.find(plan_name)
        finaltarget = target.parent
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.previous_sibling
        finaltarget = finaltarget.get_text()
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[8]/button' % finaltarget).click()
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
            self.driver.find_element_by_id("firstBtn").click()
            check_type_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "checkTypeCode0")))
            check_type_button.click()
            self.driver.find_element_by_xpath("//*[@id='nametr2']/td/div[1]/span/i").click()  # 123
            self.driver.switch_to.default_content()
            time.sleep(1)
            iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
            self.driver.switch_to.frame(iframe)
            print(2)
            collect_tab = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#collection']")))
            collect_tab.click()
            self.driver.find_element_by_xpath("//html//tr[1]/td[2]/input[1]").click()
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            print(3)
            time.sleep(2)
            self.driver.find_element_by_xpath("//table[@id='queryTable1']//tbody//tr//td[@class='queryTable-btn-td']//button[@id='save']").click()
            time.sleep(2)
            self.driver.switch_to.default_content()
            self.driver.find_element_by_id("secondBtn").click()
            question_sheet = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "card1")))
            question_sheet.click()
            print(4)
            check_situation = ("【" + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "】sunhr测试用文字")
            self.driver.find_element_by_id("basicSituation").send_keys(check_situation)
            self.driver.find_element_by_id("thirdhBtn").click()
            checkResult0 = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "checkResult0")))
            checkResult0.click()
            self.driver.find_element_by_id("dealMethod0").click()
            print(5)
            self.driver.find_element_by_id("fourBtn").click()
            self.driver.find_element_by_xpath("//div[@class='common-btn']//button[@class='btn btn-success btn-sm']").click()
            self.button.click_confirm_button()
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "依据普通任务新建检查已提交，检查企业为【%s】" % enterprise_name)
            return enterprise_name
        except Exception as e:
            self.common_action.get_screenshot("check_new_random_test")
            print("根据普通任务【%s】创建针对【%s】的流程失败" % (plan_name, enterprise_name))
            print(e)

    def confirm_normal_task_check(self, task_name, enterprise_name):
        # 确认针对普通任务发起的检查新建成功
        try:
            url = ('http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkPlan/dtdcheckplansd_list.jsp?entParentId=food')
            self.driver.get(url)
            target = self.common_action.find(task_name)
            finaltarget = target.parent
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.previous_sibling
            finaltarget = finaltarget.get_text()
            self.driver.find_element_by_xpath('//html//tr[%s]/td[9]/a[1]' % finaltarget).click()
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            self.driver.switch_to.default_content()
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
            self.driver.switch_to.frame(iframe)
            target = self.common_action.find(enterprise_name)
            if target != None:
                print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "依据普通任务新建检查成功，检查企业为【%s】" % enterprise_name)
                return True
            else:
                return False
        except Exception as e:
            print(e)


class NewTemplate(object):

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
        self.driver.find_element_by_id('checkTableType0').click()
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
        self.driver.find_element_by_id('displayColumn7').click()
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
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr/td[7]/input').send_keys('sunhr测试检查要求')
        self.driver.find_element_by_id('defaultConclusion').click()
        self.driver.find_element_by_xpath('//*[@id="defaultConclusion"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr/td[11]/input').send_keys('100')
        iframe = self.driver.find_element_by_id('frameName')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_id('bts').click()
        self.button.click_confirm_button()
        return template_name
