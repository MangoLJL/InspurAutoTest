# coding=utf-8
import time
from common_action import Setup, SwitchToFrame
from food_actions import NewCheck, NewDoubleRandom


def new_check():

    food_new_check_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = food_new_check_setup.setup_driver('wangweixuan', '1', '智慧监管', '日常监管')
    food_new_check_setup.choose_menu('食品监督检查', '新建检查', '现场录入')
    switch_to_frame = SwitchToFrame(driver)
    switch_to_frame.switch_to_main_frame()
    new_check = NewCheck(driver)
    new_check.first_step()
    new_check.second_step()
    new_check.third_step()
    new_check.fourth_step()
    new_check.fifth_step()
    new_check.final_step()
    driver.quit()
    print('食品新建日常检查流程测试成功，测试通过')
    return True


def double_random_task():
    food_new_random_task_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = food_new_random_task_setup.setup_driver('wangweixuan', '1', '智慧监管', '日常监管')
    food_new_random_task_setup.choose_menu('食品监督检查', '任务管理', '双随机任务')
    switch_to_frame = SwitchToFrame(driver)
    new_double_random = NewDoubleRandom(driver)
    switch_to_frame.switch_to_main_frame()
    new_double_random.new_random_task()
    driver.quit()
    print('食品双随机流程测试成功，测试通过')
    return True
