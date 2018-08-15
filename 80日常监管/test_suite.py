# coding=utf-8
import sys
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\food')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\makeup')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\drug')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\common_modules')
import unittest
import schedule
import threading
import time
import send_test_report
from food.test_food_daily_check import TestFoodDailyCheck
from makeup.test_makeup_daily_check import TestMakeupDailyCheck
from drug.test_drug_daily_check import TestDrugDailyCheck
from common_modules.HTMLTestRunner import HTMLTestRunner
# if __name__ == '__main__':


def job(test_str):
    suite = unittest.TestSuite()
    tests = []
    if 'Food_New_Template' in test_str:
        tests.append(TestFoodDailyCheck("test_new_template"))  # 食品新建模板
    if 'Food_Simple_Check' in test_str:
        tests.append(TestFoodDailyCheck("test_simple_check"))  # 食品现场录入简易版本
    if 'Food_New_Check' in test_str:
        tests.append(TestFoodDailyCheck("test_new_check"))  # 食品现场录入全覆盖版本
    if 'Food_Double_Random Check' in test_str:
        tests.append(TestFoodDailyCheck("test_double_random_task"))  # 食品双随机
    if 'Food_Normal_Task' in test_str:
        tests.append(TestFoodDailyCheck("test_normal_task"))  # 食品普通计划
    if 'Food_Save_Draft' in test_str:
        tests.append(TestFoodDailyCheck("test_save_draft"))  # 食品暂存草稿
    if 'Makeup_New_Template' in test_str:
        tests.append(TestMakeupDailyCheck("test_new_template"))  # 化妆品新建模板
    if 'Makeup_Simple_Check' in test_str:
        tests.append(TestMakeupDailyCheck("test_makeup_simple_check"))  # 化妆品现场录入简易版本
    if 'Drug_New_Template' in test_str:
        tests.append(TestDrugDailyCheck("test_new_template"))  # 药品新建模板
    if 'Drug_Simple_Check' in test_str:
        tests.append(TestDrugDailyCheck("test_drug_simple_check"))  # 药品现场录入建议版本
    suite.addTests(tests)
    test_report_path = ('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\TestReport\\%sTestReport.html' % time.strftime('%Y-%m-%d_%H-%M', time.localtime(time.time())))
    with open(test_report_path, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Test Report',
                                verbosity=2
                                )
        runner.run(suite)
    send_test_report.send_text_report_html(test_report_path)

test_str = sys.argv[1]
job(test_str)
