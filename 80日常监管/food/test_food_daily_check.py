import sys
import time
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\food')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\common_modules')
import unittest
import food.food_daily_check as food_daily_check
from food.food_actions import Template
from common_modules.common_action import Setup


class TestFoodDailyCheck(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        try:
            print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '清理模板...')
            clean_template_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
            driver = clean_template_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
            template = Template(driver)
            template.clean_template()
        except Exception as e:
            print("清理模板失败，截图已保存至new_template_error.png，当前url为：【%s】错误信息为：%s" % (driver.current_url, e))
            driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\食品日常检查\\error_screenshot\\%sdelete_template_error.png" %
                                          time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))

    @unittest.skip("I don't want to run this case.")
    def test_new_check(self):
        """测试新建检查"""
        self.assertEqual(True, food_daily_check.new_check())

#    @unittest.skip("I don't want to run this case.")
    def test_double_random_task(self):
        """测试双随机任务"""
        self.assertEqual(True, food_daily_check.double_random_task())

#    @unittest.skip("I don't want to run this case.")
    def test_normal_task(self):
        """测试普通任务"""
        self.assertEqual(True, food_daily_check.normal_task())

#    @unittest.skip("I don't want to run this case.")
    def test_simple_check(self):
        """测试简略检查"""
        self.assertEqual(True, food_daily_check.simple_check())

#    @unittest.skip("I don't want to run this case.")
    def test_new_template(self):
        """测试新建模板"""
        self.assertEqual(True, food_daily_check.new_template())
if __name__ == '__main__':
    unittest.main()
