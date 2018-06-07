import unittest
import schedule
import threading
import time

from test_food_daily_check import TestNewCheck, TestDoubleRandomTask, TestNormalTask, TestNewTemplate
from HTMLTestRunner import HTMLTestRunner

# if __name__ == '__main__':


def job():
    global new_template_name
    new_template_name = 'None'
    print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '开始运行...')
    suite = unittest.TestSuite()
    tests = [TestNewTemplate("test_new_template"), TestNewCheck("test_new_check"), TestDoubleRandomTask("test_double_random_task"), TestNormalTask("test_normal_task")]
    suite.addTests(tests)

    with open('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\食品日常检查\\TestReport\\%sTestReport.html' % time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())), 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Test Report',
                                verbosity=2
                                )
        runner.run(suite)
job()
schedule.every(3).hours.do(job)
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
