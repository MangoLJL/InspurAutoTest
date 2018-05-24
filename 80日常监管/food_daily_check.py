# coding=utf-8
import time
from common_action import Setup, SwitchToFrame
from food_actions import NewCheck


def new_check():

    dc = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = dc.setup_driver('wangweixuan', '1', '智慧监管', '日常监管')
    new_check = NewCheck(driver)
    switch_to_frame = SwitchToFrame(driver)
#    new_check.click_food_new_check()
    dc.choose_menu('食品监督检查', '新建检查', '现场录入')
    switch_to_frame.switch_to_main_frame()
    new_check.first_step()
    new_check.second_step()
    new_check.third_step()
    new_check.fourth_step()
    new_check.fifth_step()
    new_check.final_step()
    driver.quit()
    print('流程测试成功，测试通过')
    return True


def double_random_task():
    dc = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = dc.setup_driver('wangweixuan', '1', '智慧监管', '日常监管')
