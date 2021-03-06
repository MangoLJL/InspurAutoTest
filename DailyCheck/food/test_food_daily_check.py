import sys
import time
import traceback
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\food')
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\common_modules')
import unittest
import food.food_daily_check as food_daily_check
import common_modules.globalvar as globalvar
from food.food_actions import Template
from common_modules.common_action import Setup


class TestFoodDailyCheck(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        try:
            template_ID = globalvar.get_value('food_template_ID')
            if template_ID == 'None':
                print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '没有需要清理的食品模板...')
            else:
                print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '清理食品模板...')
                clean_template_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
                driver = clean_template_setup.setup_driver('liubx', '1', '智慧监管', '日常监管')
                template = Template(driver)
                template.clean_template()
        except Exception as e:
            print("清理模板失败，截图已保存至清理食品模板失败.png，当前url为：【%s】错误信息为：" % driver.current_url)
            traceback.print_exc()
            driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\食品日常检查\\error_screenshot\\%s清理食品模板失败.png" %
                                          time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))

    @unittest.skip("跳过新建检查")
    def test_new_check(self):
        """测试新建检查"""
        self.assertEqual(True, food_daily_check.new_check())

#    @unittest.skip("跳过双随机任务")
    def test_double_random_task(self):
        """测试双随机任务"""
        self.assertEqual(True, food_daily_check.double_random_task())

#    @unittest.skip("跳过普通任务")
    def test_normal_task(self):
        """测试普通任务"""
        self.assertEqual(True, food_daily_check.normal_task())

#    @unittest.skip("跳过简略检查")
    def test_simple_check(self):
        """测试简略检查"""
        self.assertEqual(True, food_daily_check.simple_check())

#    @unittest.skip("跳过新建模板")
    def test_new_template(self):
        """测试新建模板"""
        self.assertEqual(True, food_daily_check.new_template())

#    @unittest.skip("跳过暂存草稿")
    def test_save_draft(self):
        """测试暂存草稿"""
        self.assertEqual(True, food_daily_check.save_draft())
if __name__ == '__main__':
    unittest.main()
