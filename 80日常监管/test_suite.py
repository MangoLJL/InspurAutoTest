# coding=utf-8
import sys
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\food')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\makeup')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\drug')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\common_modules')
import unittest
import schedule
import threading
import time
from food.test_food_daily_check import TestFoodDailyCheck
from makeup.test_makeup_daily_check import TestMakeupDailyCheck
from drug.test_drug_daily_check import TestDrugDailyCheck
from common_modules.HTMLTestRunner import HTMLTestRunner
# if __name__ == '__main__':


def job(test_str):
    print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '开始运行...')
    suite = unittest.TestSuite()
    tests = []
    print(test_str)
    if 'Food New Template' in test_list:
        tests.append(TestFoodDailyCheck("test_new_template"))  # 食品新建模板
    if 'Food Simple Template' in test_list:
        tests.append(TestFoodDailyCheck("test_simple_check"))  # 食品现场录入简易版本
    if 'Food New Check' in test_list:
        tests.append(TestFoodDailyCheck("test_new_check"))  # 食品现场录入全覆盖版本
    if 'Food Double Random Check' in test_list:
        tests.append(TestFoodDailyCheck("test_double_random_task"))  # 食品双随机
    if 'Food Normal Task' in test_list:
        tests.append(TestFoodDailyCheck("test_normal_task"))  # 食品普通计划
    if 'Food Save Draft' in test_list:
        tests.append(TestFoodDailyCheck("test_save_draft"))  # 食品暂存草稿
    if 'Makeup New Template' in test_list:
        tests.append(TestMakeupDailyCheck("test_new_template"))  # 化妆品新建模板
    if 'Makeup Simple Template' in test_list:
        tests.append(TestMakeupDailyCheck("test_makeup_simple_check"))  # 化妆品现场录入简易版本
    if 'Drug New Template' in test_list:
        tests.append(TestDrugDailyCheck("test_new_template"))  # 药品新建模板
    if 'Drug Simple Template' in test_list:
        tests.append(TestDrugDailyCheck("test_drug_simple_check"))  # 药品现场录入建议版本
    print(tests)
    '''
    suite.addTests(tests)

    with open('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\TestReport\\%sTestReport.html' % time.strftime('%Y-%m-%d_%H-%M', time.localtime(time.time())), 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Test Report',
                                verbosity=2
                                )
        runner.run(suite)
    '''
test_str = sys.argv[1]
job(test_str)
