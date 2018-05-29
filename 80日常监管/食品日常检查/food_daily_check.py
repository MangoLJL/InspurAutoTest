# coding=utf-8
import time
from common_action import Setup, SwitchToFrame
from food_actions import NewCheck, NewDoubleRandom, NewNormalTask


def new_check():
    try:
        food_new_check_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = food_new_check_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
        food_new_check_setup.choose_menu('食品监督检查', '新建检查', '现场录入')
        switch_to_frame = SwitchToFrame(driver)
        switch_to_frame.switch_to_main_frame()
        new_check = NewCheck(driver)
        new_check.first_step()
        new_check.second_step()
        new_check.third_step()
        check_situation = new_check.fourth_step()
        new_check.fifth_step()
        new_check.final_step()
        new_check_confirmer = NewCheck(driver)
        ture_or_false = new_check_confirmer.confirm_new_check(check_situation)
        driver.quit()
        return ture_or_false
    except Exception as e:
        print("测试未通过，截图已保存至new_check.png，错误信息：", e)
        driver.get_screenshot_as_file("C:\\Users\\sunhaoran\\Desktop\\%snew_check.png" % time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))


def double_random_task():
    try:
        food_new_random_task_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = food_new_random_task_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
        food_new_random_task_setup.choose_menu('食品监督检查', '任务管理', '双随机任务')
        switch_to_frame = SwitchToFrame(driver)
        new_double_random = NewDoubleRandom(driver)
        switch_to_frame.switch_to_main_frame()
        task_name = new_double_random.create_new_random_task()  # 创建双随机任务
        new_random_test_confirmer_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = new_random_test_confirmer_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')  # 因为涉及到计划提交到其他人的情况，所以需要另外建一个driver
        new_random_test_receiver = NewDoubleRandom(driver)
        new_random_test_receiver.receive_new_random_test(task_name)  # 接收双随机任务
        driver.quit()
        new_random_test_confirmer_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = new_random_test_confirmer_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
        new_random_test_checker = NewDoubleRandom(driver)
        ture_or_false = new_random_test_checker.check_new_random_test(task_name)
        return ture_or_false
        driver.quit()
    except Exception as e:
        print("测试未通过，截图已保存至double_random_task_error.png，错误信息：", e)
        driver.get_screenshot_as_file("C:\\Users\\sunhaoran\\Desktop\\%sdouble_random_task_error.png" % time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))


def normal_task():
    try:
        food_new_random_task_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = food_new_random_task_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
        food_new_random_task_setup.choose_menu('食品监督检查', '任务管理', '计划管理')
        switch_to_frame = SwitchToFrame(driver)
        switch_to_frame.switch_to_main_frame()
        new_normal_task = NewNormalTask(driver)
        normal_plan_name = new_normal_task.create_task()
        new_normal_task_confirmer = NewNormalTask(driver)
        ture_or_false = new_normal_task_confirmer.confirm_new_normal_task(normal_plan_name)
        driver.quit()
        return ture_or_false
    except Exception as e:
        print("测试未通过，截图已保存至normal_task_error.png，错误信息：", e)
        driver.get_screenshot_as_file("C:\\Users\\sunhaoran\\Desktop\\%snormal_task_error.png" % time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
