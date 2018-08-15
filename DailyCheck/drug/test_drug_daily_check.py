import sys
import traceback
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\drug')
import unittest
from drug.drug_daily_check import *
from drug.drug_actions import Template
import common_modules.globalvar as globalvar


class TestDrugDailyCheck(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        try:
            template_ID = globalvar.get_value('drug_template_ID')
            if template_ID == 'None':
                print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '没有需要清理的药品模板...')
            else:
                print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '清理药品模板...')
                clean_template_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
                driver = clean_template_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
                template = Template(driver)
                template.clean_template()
        except Exception as e:
            print("清理药品模板失败，截图已保存至new_template_error.png，当前url为：【%s】错误信息为：%s" % (driver.current_url, e))
            driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\食品日常检查\\error_screenshot\\%s清理药品模板失败.png" %
                                          time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))

#    @unittest.skip("I don't want to run this case.")

    def test_new_template(self):
        """测试新建检查"""
        self.assertEqual(True, new_template())

    def test_drug_simple_check(self):
        """测试新建检查"""
        self.assertEqual(True, drug_simple_check())
