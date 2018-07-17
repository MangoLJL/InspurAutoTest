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


def job():
    print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '开始运行...')
    suite = unittest.TestSuite()
    tests = []
    tests.append(TestFoodDailyCheck("test_new_template"))  # 食品新建模板
    # tests.append(TestFoodDailyCheck("test_simple_check"))  # 食品现场录入简易版本
    tests.append(TestFoodDailyCheck("test_new_check"))  # 食品现场录入全覆盖版本
    # tests.append(TestFoodDailyCheck("test_double_random_task"))  # 食品双随机
    # tests.append(TestFoodDailyCheck("test_normal_task"))  # 食品普通计划
    tests.append(TestFoodDailyCheck("test_save_draft"))  # 食品暂存草稿
    # tests.append(TestMakeupDailyCheck("test_new_template"))  # 化妆品新建模板
    # tests.append(TestMakeupDailyCheck("test_makeup_simple_check"))  # 化妆品现场录入简易版本
    tests.append(TestDrugDailyCheck("test_new_template"))  # 药品新建模板
    tests.append(TestDrugDailyCheck("test_drug_simple_check"))  # 药品现场录入建议版本

    suite.addTests(tests)

    with open('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\TestReport\\%sTestReport.html' % time.strftime('%Y-%m-%d_%H-%M', time.localtime(time.time())), 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Test Report',
                                verbosity=2
                                )
        runner.run(suite)
job()

# schedule.every(4).hours.do(job)
'''
def job_task23():
    threading.Thread(target=job).start()


def job_task01():
    threading.Thread(target=job).start()


def job_task03():
    threading.Thread(target=job).start()


def job_task05():
    threading.Thread(target=job).start()

schedule.every().day.at("23:00").do(job_task23)
schedule.every().day.at("01:00").do(job_task01)
schedule.every().day.at("03:00").do(job_task03)
schedule.every().day.at("05:00").do(job_task05)
while True:

    schedule.run_pending()
    time.sleep(1)
'''
