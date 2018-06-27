# coding=utf-8
import sys
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\food')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\makeup')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\common_modules')
import unittest
import schedule
import threading
import time
from food.test_food_daily_check import TestFoodDailyCheck
from makeup.test_makeup_daily_check import TestMakeupDailyCheck
from common_modules.HTMLTestRunner import HTMLTestRunner
# if __name__ == '__main__':


def job():
    print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '开始运行...')
    suite = unittest.TestSuite()
    tests = [TestFoodDailyCheck("test_new_template"), TestFoodDailyCheck("test_simple_check"), TestFoodDailyCheck("test_new_check"),
             TestFoodDailyCheck("test_double_random_task"), TestFoodDailyCheck("test_normal_task"), TestMakeupDailyCheck("test_new_template")]
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
