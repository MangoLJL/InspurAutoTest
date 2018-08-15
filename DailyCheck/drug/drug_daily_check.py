# coding=utf-8
import sys
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\common_modules')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\drug')
import re
import time
import traceback
import common_modules.globalvar as globalvar
from functools import reduce
from drug.drug_actions import NewCheck, Template
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common_modules.common_action import Setup, SwitchToFrame, Time, Button, CommonAction, SendKeys


def new_template():
    drug_new_template_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = drug_new_template_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
    try:
        drug_new_template_setup.choose_first_menu('药品检查')
        time.sleep(0.5)
        driver.find_element_by_id('000000000000000000000000019462').click()
        time.sleep(0.5)
        drug_new_template_setup.choose_third_menu('药品检查表制定')
        switch_to_frame = SwitchToFrame(driver)
        switch_to_frame.switch_to_main_frame()
        new_template = Template(driver)
        new_template_name = new_template.create_template()
        ture_or_false = new_template.confirm_new_template(new_template_name)
        driver.quit()
        return ture_or_false
    except Exception as e:
        print("测试未通过，截图已保存至drug_new_template_error.png，当前url为：【%s】错误信息为：" % driver.current_url)
        traceback.print_exc()
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%sdrug_new_template_error.png" %
                                      time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
    finally:
        driver.quit()


def drug_simple_check():
    drug_template_ID = globalvar.get_value('drug_template_ID')
    drug_simple_check_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = drug_simple_check_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
    try:
        drug_simple_check_setup.choose_first_menu('药品检查')
        driver.find_element_by_id('000000000000000000000000019460').click()
        driver.find_element_by_id('check0201010001').click()
        switch_to_frame = SwitchToFrame(driver)
        switch_to_frame.switch_to_main_frame()
        new_check = NewCheck(driver)
        new_check.first_step()
        new_check.second_step()
        new_check.third_step('checkTypeCode0')
        check_describe = new_check.fourth_step_check_template(drug_template_ID)
        new_check.fifth_step()
        new_check.final_step()
        true_or_false = new_check.confirm_new_check_check_template(check_describe)
        driver.quit()
        return true_or_false
    except Exception as e:
        print("测试未通过，截图已保存至drug_simple_check_error.png，当前url为：【%s】错误信息为：" % driver.current_url)
        traceback.print_exc()
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%sdrug_simple_check_error.png" %
                                      time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
    finally:
        driver.quit()
