import unittest
from test_food_daily_check import TestFoodDailyCheck
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFoodDailyCheck))

    with open('HTMLReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Test Report',
                                verbosity=2
                                )
        runner.run(suite)
