# coding=utf-8
import sys
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\common_modules')
import time
import re
import random
import common_modules.globalvar as globalvar
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common_modules.common_action import Setup, SwitchToFrame, Time, Button, CommonAction, SendKeys
globalvar._init()


class NewCheck(object):

    def __init__(self, driver):
        self.driver = driver
        self.button = Button(self.driver)
        self.common_action = CommonAction(self.driver)
        self.send = SendKeys(self.driver)

    def first_step(self):
        radiobuttonindex = 'radio0'
        radiobutton = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, radiobuttonindex)))
        radiobutton.click()
        self.button.click_right_arrow_button()

    def second_step(self):
        enterprise_selector = self.driver.find_element_by_id("enterpriseName")
        ActionChains(self.driver).double_click(enterprise_selector).perform()
        self.common_action.scroll_and_switch_to_iframe()
        data_exsists = self.common_action.data_exsists()
        if data_exsists:
            random_enterprise = random.randint(1, 5)
            enterprise_radio_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//html//tr[%s]/td[2]/input[1]" % random_enterprise)))
            enterprise_name = self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[%s]/td[3]/span' % random_enterprise).text
            print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '检查的企业为' + enterprise_name)
            enterprise_radio_button.click()
            self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
            time.sleep(1)
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("mainFrame")
            self.button.click_right_arrow_button()
            return True
        else:
            return False

    def third_step(self, checktype):
        check_type_button = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, checktype)))
        check_type_button.click()
        self.button.click_search_button()
        self.common_action.scroll_and_switch_to_iframe()
        collect_tab = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#collection']")))
        collect_tab.click()
        self.button.click("//html//tr[1]/td[2]/input[1]")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.button.click("//table[@id='queryTable1']//tbody//tr//td[@class='queryTable-btn-td']//button[@id='save']")
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.button.click_right_arrow_button()

    def fourth_step_check_template(self, template_name):
        # 使用检查模板
        self.driver.find_element_by_id(template_name).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//input[@class='clauseRes'][last()]").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-default btn-xs']").click()
        time.sleep(1)
        self.common_action.scroll_and_switch_to_iframe()
        check_describe = ("%ssunhr问题描述" % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        self.driver.find_element_by_id("checkDescribe").send_keys('$' + check_describe + '$')
        self.button.click_save_button()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_xpath("//input[@class='scoreValue']").send_keys('66')
        self.button.click_right_arrow_button()
        return check_describe

    def fourth_step_check_situation(self):
        # 使用检查情况
        question_sheet = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "card1")))
        question_sheet.click()
        check_situation = ("【" + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "】sunhr测试用文字")
        self.driver.find_element_by_id("basicSituation").send_keys(check_situation)
        self.button.click_right_arrow_button()
        return check_situation

    def fifth_step(self):
        checkResult0 = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "checkResult1")))
        checkResult0.click()
        self.driver.find_element_by_id("dealMethod5").click()
        self.driver.find_element_by_id("isShowInfo1").click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.button.click_right_arrow_button()

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
        pass
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


class Template(object):

    def __init__(self, driver):
        self.driver = driver
        self.button = Button(self.driver)
        self.common_action = CommonAction(self.driver)

    def create_template(self):
        self.button.click_plus_button()
        template_name = ("%ssunhr测试模板" % time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        self.driver.find_element_by_id('templateName').send_keys(template_name)
        self.button.click('radio0')
        self.button.click('radio1')
        self.button.click('radio2')
        # self.driver.find_element_by_id('checkTableType0').click()
        self.driver.find_element_by_id('isPeriod1').click()
        # self.driver.find_element_by_id('checkProgramNum').send_keys('1')
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
        iframe = self.driver.find_element_by_xpath('//iframe[last]')
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
        iframe = self.driver.find_element_by_id('frameName')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_id('bts').click()
        self.button.click_confirm_button()
        globalvar.set_value('makeup_template_name', template_name)
        return template_name

    def confirm_new_template(self, template_name):
        url = ('10.12.1.80/checkOfCity/jsp/dtdcheck/basic/checkTemplate/dtdcheckftemplate_list.jsp?entParentId=hz')
        self.driver.get(url)
        current_template_name = self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[1]/td[3]/a').text
        if current_template_name == template_name:
            current_template_ID = str(self.driver.find_element_by_xpath('//*[@id="grid"]/tbody/tr[1]/td[3]/a').get_attribute('href'))
            template_ID_suits = current_template_ID.split('\'')
            template_ID = template_ID_suits[1]
            globalvar.set_value('template_ID', template_ID)
            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '新建模板成功，测试通过')
            return True
        else:
            print("查找新建模板【%s】失败，当前截图已保存为confirm_new_template_error" % driver.template_name)
            driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\食品日常检查\\error_screenshot\\%sconfirm_new_template_error.png" %
                                          time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
            return False

    def clean_template(self):
        url = 'http://10.12.1.80/checkOfCity/jsp/dtdcheck/food/checkTemplate/dtdcheckftemplate_list.jsp?entParentId=food'
        self.driver.get(url)
        template_name = globalvar.get_value('template_name')
        current_html = self.driver.page_source
        self.driver.find_element_by_id("grid_length").click()
        self.driver.find_element_by_xpath("//option[@value='100']").click()
        target = self.common_action.find(template_name)
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
        print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '清理模板完成')
