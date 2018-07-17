import sys
import traceback
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\makeup')
import unittest
from makeup.makeup_daily_check import *
from makeup.makeup_actions import Template


class TestMakeupDailyCheck(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        try:
            print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '清理化妆品模板...')
            clean_template_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
            driver = clean_template_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
            template = Template(driver)
            template.clean_template()
        except Exception as e:
            print("清理化妆品模板失败，截图已保存至new_template_error.png，当前url为：【%s】错误信息为：%s" % (driver.current_url, e))
            driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\食品日常检查\\error_screenshot\\%s清理化妆品模板失败.png" %
                                          time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))

#    @unittest.skip("I don't want to run this case.")

    def test_new_template(self):
        """测试新建检查"""
        self.assertEqual(True, new_template())

    def test_makeup_simple_check(self):
        """测试新建检查"""
        self.assertEqual(True, makeup_simple_check())
