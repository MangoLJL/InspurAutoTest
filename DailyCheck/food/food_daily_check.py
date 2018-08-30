# coding=utf-8
import sys
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\common_modules')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\food')
import re
import time
import traceback
import common_modules.globalvar as globalvar
from functools import reduce
from food.food_actions import NewCheck, NewDoubleRandom, NewNormalTask, Template
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common_modules.common_action import Setup, SwitchToFrame, Time, Button, CommonAction


def new_check():
    # 新建检查，基本废弃
    new_template_ID = globalvar.get_value('food_template_ID')

    def true_plus_false(a, b):
        return (a and b)
    try:
        for flag in range(0, 2):
            final_true_or_false = [False, False, False, False, False, False, False, False]
            true_or_false = [False, False, False, False, False]
            enterprise_type = ['小作坊', '食品摊贩', '小餐饮', '食品生产', '食品流通', '餐饮服务', '食品经营', '校外托管']
            check_type_name = ['日常检查', '专项检查', '量化评级', '学校季度检查', '飞行检查']
            for y in range(0, 8):
                if y != 6:  # 食品经营特殊化
                    for i in range(0, 5):
                        try:
                            print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '开始进行%s-%s测试' % (enterprise_type[y], check_type_name[i]))
                            food_new_check_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
                            driver = food_new_check_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
                            food_new_check_setup.choose_menu('食品监督检查', '新建检查', '现场录入')
                            switch_to_frame = SwitchToFrame(driver)
                            switch_to_frame.switch_to_main_frame()
                            new_check = NewCheck(driver)
                            new_check.first_step(y)
                            data_exsists = new_check.second_step()
                            if data_exsists:
                                checkTypeCode = 'checkTypeCode' + str(i)
                                new_check.third_step(checkTypeCode)
                                if flag == 0:
                                    check_describe = new_check.fourth_step_check_template(new_template_ID)
                                else:
                                    check_situation = new_check.fourth_step_check_situation()
                                new_check.fifth_step()
                                new_check.final_step()
                                new_check_confirmer = NewCheck(driver)
                                if flag == 0:
                                    true_or_false[i] = new_check_confirmer.confirm_new_check_check_template(check_describe)  # 共五个, checkTypeCode
                                else:
                                    true_or_false[i] = new_check_confirmer.confirm_new_check_check_situation(check_situation)
                                driver.quit()
                            else:
                                print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '【%s】企业列表无数据，跳过【%s】类别企业...' % (enterprise_type[y], enterprise_type[y]))
                                driver.quit()
                                break
                        except Exception as e:
                            true_or_false[i] = False
                            print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '测试【%s】-【%s】出错，截图已保存,当前url为：【%s】错误信息为：' %
                                  (enterprise_type[y], check_type_name[i], driver.current_url))
                            driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%s%s%sfood_new_check.png" % (
                                time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())), enterprise_type[y], check_type_name[i]))
                            continue
                    true_or_false_suite = reduce(true_plus_false, true_or_false)
                    final_true_or_false[y] = true_or_false_suite
                else:
                    food_bussiness_type = ['食品销售经营者', '餐饮服务经营者', '单位食堂']
                    print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '开始进行食品经营大类三个小类的测试，共15个事项')
                    food_bussiness_suite_true_or_false = [[], [], []]
                    for z in range(0, 3):
                        for i in range(0, 5):
                            try:
                                print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '开始进行【%s】-【%s】测试' % (food_bussiness_type[z], check_type_name[i]))
                                food_new_check_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
                                driver = food_new_check_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
                                common_action = CommonAction(driver)
                                food_new_check_setup.choose_menu('食品监督检查', '新建检查', '现场录入')
                                switch_to_frame = SwitchToFrame(driver)
                                switch_to_frame.switch_to_main_frame()
                                new_check = NewCheck(driver)
                                new_check.first_step(y)
                                enterprise_selector = driver.find_element_by_id("enterpriseName")
                                ActionChains(driver).double_click(enterprise_selector).perform()
                                driver.switch_to.default_content()
                                time.sleep(1)
                                iframe = driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
                                driver.switch_to.frame(iframe)
                                time.sleep(3)
                                data_exsists = common_action.data_exsists()
                                if data_exsists:
                                    enterprise_radio_button = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//html//tr[1]/td[2]/input[1]")))
                                    enterprise_radio_button.click()
                                    driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
                                    time.sleep(1)
                                    driver.switch_to.default_content()
                                    driver.switch_to.frame("mainFrame")
                                    businessItem = "businessItem" + str(z)  # 拼食品经营小类
                                    driver.find_element_by_id(businessItem).click()
                                    driver.find_element_by_id("secondBtn").click()
                                else:
                                    print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '【%s】企业列表无数据，跳过此类别企业...' % enterprise_type[y])
                                    driver.quit()
                                checkTypeCode = 'checkTypeCode' + str(i)
                                new_check.third_step(checkTypeCode)
                                if flag == 0:
                                    check_describe = new_check.fourth_step_check_template(new_template_ID)
                                else:
                                    check_situation = new_check.fourth_step_check_situation()
                                new_check.fifth_step()
                                new_check.final_step()
                                new_check_confirmer = NewCheck(driver)
                                if flag == 0:
                                    food_bussiness_suite_true_or_false[z].append(new_check_confirmer.confirm_new_check_check_template(check_describe))
                                else:
                                    food_bussiness_suite_true_or_false[z].append(new_check_confirmer.confirm_new_check_check_situation(check_situation))

                                driver.quit()
                            except Exception as e:
                                food_bussiness_suite_true_or_false[z].append(False)
                                print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '测试【%s】-【%s】出错，截图已保存,当前url为：【%s】错误信息为：' %
                                      (enterprise_type[y], check_type_name[i], driver.current_url))
                                driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%s%s%sfood_new_check.png" % (
                                    time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())), enterprise_type[y], check_type_name[i]))
                                continue
                    food_bussiness_middle_true_or_false = []
                    for z in range(0, 3):
                        food_bussiness_middle_true_or_false.append(reduce(true_plus_false, food_bussiness_suite_true_or_false[z]))  # 每组三个
                    food_bussiness_final_true_or_false = reduce(true_plus_false, food_bussiness_middle_true_or_false)  # 食品经营最终结果，一个
                    final_true_or_false[y] = food_bussiness_final_true_or_false
        return (reduce(true_plus_false, final_true_or_false))

    except Exception as e:
        return False
        print("【%s】-【%s】测试未通过，截图已保存至new_check.png，当前url为：【%s】错误信息为：" % (enterprise_type[y], check_type_name[i], driver.current_url))
        traceback.print_exc()
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%snew_check.png" %
                                      time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))


def simple_check():
    def true_plus_false(a, b):
        return (a and b)
    new_template_ID = globalvar.get_value('food_template_ID')
    check_type_name = ['日常检查', '专项检查', '量化评级', '学校季度检查', '飞行检查']
    enterprise_type = ['小作坊', '食品摊贩', '小餐饮', '食品生产', '食品流通', '餐饮服务', '食品经营', '校外托管']
    food_bussiness_type = ['食品销售经营者', '餐饮服务经营者', '单位食堂']
    true_or_false = [False, False, False, False, True]
    for flag in range(0, 2):
        if new_template_ID == 'None'and flag == 0:
            print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '没有查询到食品检查模板，跳过使用检查模板测试...')
            true_or_false[0] = True
            true_or_false[2] = True
        else:
            try:
                i = 0  # 日常检查
                y = 3  # 食品生产
                print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '开始进行【%s】-【%s】测试' % (enterprise_type[y], check_type_name[i]))
                food_new_check_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
                driver = food_new_check_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
                food_new_check_setup.choose_menu('食品监督检查', '新建检查', '现场录入')
                switch_to_frame = SwitchToFrame(driver)
                switch_to_frame.switch_to_main_frame()
                new_check = NewCheck(driver)
                new_check.first_step(y)
                data_exsists = new_check.second_step()
                if data_exsists:
                    checkTypeCode = 'checkTypeCode' + str(i)
                    new_check.third_step(checkTypeCode)
                    if flag == 0:
                        print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '使用检查模板进行检查...')
                        check_describe = new_check.fourth_step_check_template(new_template_ID)
                    else:
                        print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '使用检查情况说明进行检查...')
                        check_situation = new_check.fourth_step_check_situation()
                    new_check.fifth_step()
                    new_check.final_step()
                    new_check_confirmer = NewCheck(driver)
                    if flag == 0:
                        true_or_false[0] = new_check_confirmer.confirm_new_check_check_template(check_describe)
                    else:
                        true_or_false[1] = new_check_confirmer.confirm_new_check_check_situation(check_situation)
                    driver.quit()
                else:
                    print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '【%s】企业列表无数据，跳过【%s】类别企业...' % (enterprise_type[y], enterprise_type[y]))
                    driver.quit()
                    break
            except Exception as e:
                true_or_false[4] = False
                print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '测试【%s】-【%s】出错，截图已保存,当前url为：【%s】错误信息为' %
                      (enterprise_type[y], check_type_name[i], driver.current_url))
                traceback.print_exc()
                driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%s%s%sfood_new_check.png" % (
                    time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())), enterprise_type[y], check_type_name[i]))
            i = 0  # 日常检查
            y = 6  # 食品经营
            food_bussiness_suite_true_or_false = [[], [], []]
            # z = 0  # 食品销售经营者  # 此处逻辑已被删除2018/8/15
            try:
                print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '开始进行【%s】-【%s】-【%s】测试' % (enterprise_type[y], food_bussiness_type[z], check_type_name[i]))
                food_new_check_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
                driver = food_new_check_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
                common_action = CommonAction(driver)
                food_new_check_setup.choose_menu('食品监督检查', '新建检查', '现场录入')
                switch_to_frame = SwitchToFrame(driver)
                switch_to_frame.switch_to_main_frame()
                new_check = NewCheck(driver)
                new_check.first_step(y)
                enterprise_selector = driver.find_element_by_id("enterpriseName")
                ActionChains(driver).double_click(enterprise_selector).perform()
                driver.switch_to.default_content()
                time.sleep(1)
                iframe = driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
                driver.switch_to.frame(iframe)
                time.sleep(3)
                data_exsists = common_action.data_exsists()
                if data_exsists:
                    enterprise_radio_button = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//html//tr[1]/td[2]/input[1]")))
                    enterprise_radio_button.click()
                    driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
                    time.sleep(1)
                    driver.switch_to.default_content()
                    driver.switch_to.frame("mainFrame")
                    '''
                    businessItem = "businessItem" + str(z)  # 拼食品经营小类
                    try:  # 此处逻辑已被删除2018/8/15
                        driver.find_element_by_id(businessItem).click()
                    except:
                        pass
                    '''
                    driver.find_element_by_id("secondBtn").click()
                else:
                    print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '【%s】企业列表无数据，跳过此类别企业...' % enterprise_type[y])
                    driver.quit()
                    break
                checkTypeCode = 'checkTypeCode' + str(i)
                new_check.third_step(checkTypeCode)
                if flag == 0:
                    check_describe = new_check.fourth_step_check_template(new_template_ID)
                else:
                    check_situation = new_check.fourth_step_check_situation()
                new_check.fifth_step()
                new_check.final_step()
                new_check_confirmer = NewCheck(driver)
                if flag == 0:
                    print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '使用检查模板进行检查...')
                    true_or_false[2] = new_check_confirmer.confirm_new_check_check_template(check_describe)
                else:
                    print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '使用检查情况说明进行检查...')
                    true_or_false[3] = new_check_confirmer.confirm_new_check_check_situation(check_situation)
                driver.quit()
            except Exception as e:
                true_or_false[4] = False
                print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '测试【%s】-【%s】-【%s】出错，截图已保存,当前url为：【%s】错误信息为：' %
                      (enterprise_type[y], food_bussiness_type[z], check_type_name[i], driver.current_url))
                traceback.print_exc()
                driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%s%s%s%sfood_new_check.png" % (
                    time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())), enterprise_type[y],  food_bussiness_type[z], check_type_name[i]))
    return (reduce(true_plus_false, true_or_false))


def double_random_task():
    # 双随机任务新建并针对此任务发起检查
    try:
        food_new_random_task_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = food_new_random_task_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
        food_new_random_task_setup.choose_menu('食品监督检查', '任务管理', '双随机任务')
        switch_to_frame = SwitchToFrame(driver)
        new_double_random = NewDoubleRandom(driver)
        switch_to_frame.switch_to_main_frame()
        task_name = new_double_random.create_new_random_task()  # 创建双随机任务
        driver.quit()  # 0830修改过，可能有问题
        new_random_test_receiver_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = new_random_test_receiver_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')  # 因为涉及到计划提交到其他人的情况，所以需要另外建一个driver
        new_random_test_receiver = NewDoubleRandom(driver)
        new_random_test_receiver.receive_new_random_test(task_name)  # 接收双随机任务
        driver.quit()
        new_random_test_confirmer_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = new_random_test_confirmer_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
        new_random_test_checker = NewDoubleRandom(driver)
        enterprise_name = new_random_test_checker.check_new_random_test(task_name)
        true_or_false = new_random_test_checker.confirm_random_enterprise_check(task_name, enterprise_name)
        driver.quit()
        return true_or_false
    except Exception as e:
        print("测试未通过，截图已保存至double_random_task_error.png，当前url为：【%s】错误信息为：" % (driver.current_url))
        traceback.print_exc()
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%sfood_double_random_task_error.png" %
                                      time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))


def normal_task():
    # 普通任务新建并针对此任务发起检查
    food_new_random_task_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = food_new_random_task_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
    try:
        food_new_random_task_setup.choose_menu('食品监督检查', '任务管理', '任务管理')
        switch_to_frame = SwitchToFrame(driver)
        switch_to_frame.switch_to_main_frame()
        new_normal_task = NewNormalTask(driver)
        normal_plan_name = new_normal_task.create_task()
        new_normal_task_confirmer = NewNormalTask(driver)
        new_normal_task_true_or_false = new_normal_task_confirmer.confirm_new_normal_task(normal_plan_name)
        new_normal_task.receive_new_normal_task(normal_plan_name)
        new_random_test_confirmer_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = new_random_test_confirmer_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
        new_normal_task_check_creater = NewNormalTask(driver)
        enterprise_name = new_normal_task_check_creater.create_normal_task_check(normal_plan_name)
        new_normal_task_check_true_or_false = new_normal_task_check_creater.confirm_normal_task_check(normal_plan_name, enterprise_name)
        driver.quit()
        return new_normal_task_true_or_false and new_normal_task_check_true_or_false
    except Exception as e:
        print("测试未通过，截图已保存至normal_task_error.png，当前url为：【%s】错误信息为：" % (driver.current_url))
        traceback.print_exc()
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%sfood_normal_task_error.png" %
                                      time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))


def new_template():
    food_new_template_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = food_new_template_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
    try:
        food_new_template_setup.choose_menu('食品监督检查', '检查表管理', '食品监督检查表制定')
        switch_to_frame = SwitchToFrame(driver)
        switch_to_frame.switch_to_main_frame()
        new_template = Template(driver)
        new_template_name = new_template.create_template()
        ture_or_false = new_template.confirm_new_template(new_template_name)
        driver.quit()
        return ture_or_false
    except Exception as e:
        print("测试未通过，截图已保存至new_template_error.png，当前url为：【%s】错误信息为：" % (driver.current_url))
        traceback.print_exc()
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%sfood_new_template_error.png" %
                                      time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
        driver.quit()


def save_draft():
    food_save_draft_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = food_save_draft_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
    try:
        i = 0  # 日常检查
        y = 3  # 食品生产
        food_save_draft_setup.choose_menu('食品监督检查', '新建检查', '现场录入')
        switch_to_frame = SwitchToFrame(driver)
        switch_to_frame.switch_to_main_frame()
        new_check = NewCheck(driver)
        new_check.first_step(y)
        data_exsists = new_check.second_step()
        if data_exsists:
            checkTypeCode = 'checkTypeCode' + str(i)
            new_check.third_step(checkTypeCode)
            check_situation = new_check.fourth_step_check_situation()
            common_action = CommonAction(driver)
            common_action.click_error_button()
            switch_to_frame.switch_to_main_frame()
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            driver.find_element_by_id("dealMethod5").click()
            driver.find_element_by_id("isShowInfo1").click()
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            driver.find_element_by_xpath("//*[@id='fithBtn']/parent::div/preceding-sibling::div/button[@class='btn btn-info btn-sm']").click()
            time.sleep(2)
        else:
            print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '【%s】企业列表无数据，跳过此类别企业...' % enterprise_type[y])
            driver.quit()
        ture_or_false = new_check.confirm_save_as_draft(check_situation)
        new_check.delete_draft()
        driver.quit()
        return ture_or_false
    except Exception as e:
        print("测试未通过，截图已保存至save_draft_error.png，当前url为：【%s】错误信息为：" % (driver.current_url))
        traceback.print_exc()
        driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot\\%sfood_save_draft_error.png" %
                                      time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
        driver.quit()
