import unittest
from test_food_daily_check import TestNewCheck, TestDoubleRandomTask, TestNormalTask
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestNewCheck("test_new_check"), TestDoubleRandomTask("test_double_random_task"), TestNormalTask("test_normal_task")]
    suite.addTests(tests)

    with open('HTMLReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Test Report',
                                verbosity=2
                                )
        runner.run(suite)
