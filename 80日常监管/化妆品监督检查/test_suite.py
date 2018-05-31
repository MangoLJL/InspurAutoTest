import unittest
import schedule
import time
from test_food_daily_check import TestNewCheck, TestDoubleRandomTask, TestNormalTask
from HTMLTestRunner import HTMLTestRunner

# if __name__ == '__main__':


def job():
    print('开始运行...')
    suite = unittest.TestSuite()
    tests = [TestNewCheck("test_new_check"), TestDoubleRandomTask("test_double_random_task"), TestNormalTask("test_normal_task")]
    suite.addTests(tests)

    with open('%sTestReport.html' % time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())), 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Test Report',
                                verbosity=2
                                )
        runner.run(suite)
'''
schedule.every(2).hours.do(job)
# schedule.every().day.at("20:01").do(job)
while True:

    schedule.run_pending()
    time.sleep(1)
'''
job()
