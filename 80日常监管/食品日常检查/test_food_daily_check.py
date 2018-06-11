import unittest
from food_daily_check import *
from food_actions import Template


class TestFoodDailyCheck(unittest.TestCase):

    def tearDownClass(self):
        print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '清理模板...')
        clean_template_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = clean_template_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
        template = Template(driver)
        template.clean_template()


#    @unittest.skip("I don't want to run this case.")

    def test_new_check(self):
        """测试新建检查"""
        self.assertEqual(True, new_check())


#    @unittest.skip("I don't want to run this case.")

    def test_double_random_task(self):
        """测试双随机任务"""
        self.assertEqual(True, double_random_task())

    @unittest.skip("I don't want to run this case.")
    def test_normal_task(self):
        """测试普通任务.py"""
        self.assertEqual(True, normal_task())


#    @unittest.skip("I don't want to run this case.")

    def test_simple_check(self):
        """测试简略检查.py"""
        self.assertEqual(True, simple_check())


#    @unittest.skip("I don't want to run this case.")

    def test_new_template(self):
        """测试普通任务.py"""
        self.assertEqual(True, new_template())
if __name__ == '__main__':
    unittest.main()
