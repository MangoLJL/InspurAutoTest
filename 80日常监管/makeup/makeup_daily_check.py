# coding=utf-8
import sys
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\common_modules')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\makeup')
import re
import time
import traceback
import common_modules.globalvar as globalvar
from functools import reduce
from makeup.makeup_actions import NewCheck, Template
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common_modules.common_action import Setup, SwitchToFrame, Time, Button, CommonAction, SendKeys


def new_template():
    makeup_new_template_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = makeup_new_template_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
    try:
        makeup_new_template_setup.choose_menu('化妆品监督检查', '检查表管理', '检查项目管理')
        #makeup_new_template_setup.choose_menu('食品监督检查', '检查表管理', '食品监督检查表制定')
        switch_to_frame = SwitchToFrame(driver)
        switch_to_frame.switch_to_main_frame()
        new_template = Template(driver)
        new_template_name = new_template.create_template()
        ture_or_false = new_template.confirm_new_template(new_template_name)
        driver.quit()
        return ture_or_false
    except Exception as e:
        print("测试未通过，截图已保存至new_template_error.png，当前url为：【%s】错误信息为：" % driver.current_url)
        traceback.print_exc()
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%smakeup_new_template_error.png" %
                                      time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
        driver.quit()
