# coding=utf-8
from common_action import Setup, SwitchToFrame
from food_actions import NewCheck, NewDoubleRandom, NewNormalTask


def new_check():

    food_new_check_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = food_new_check_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
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
    try:
        food_new_random_task_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = food_new_random_task_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
        food_new_random_task_setup.choose_menu('食品监督检查', '任务管理', '双随机任务')
        switch_to_frame = SwitchToFrame(driver)
        new_double_random = NewDoubleRandom(driver)
        switch_to_frame.switch_to_main_frame()
        task_name = new_double_random.create_new_random_task()
        new_random_test_confirmer_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = new_random_test_confirmer_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
        new_random_test_confirmer = NewDoubleRandom(driver)
        ture_or_false = new_random_test_confirmer.confirm_new_random_test(task_name)
        driver.quit()
        return ture_or_false
    except Exception as e:
        driver.get_screenshot_as_file("C:\\Users\\sunhaoran\\Desktop\\error.png")


def normal_task():
    try:
        food_new_random_task_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = food_new_random_task_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
        food_new_random_task_setup.choose_menu('食品监督检查', '任务管理', '计划管理')
        switch_to_frame = SwitchToFrame(driver)
        switch_to_frame.switch_to_main_frame()
        new_normal_task = NewNormalTask(driver)
        normal_task_name = new_normal_task.create_task()

    except Exception as e:
        print(e)
        driver.get_screenshot_as_file("C:\\Users\\sunhaoran\\Desktop\\error.png")
