import unittest
from food_daily_check import FoodDailyCheck

FDC = FoodDailyCheck()


class TestNewCheck(unittest.TestCase):
    """测试新建检查"""
#    @unittest.skip("I don't want to run this case.")

    def test_new_check(self):
        """Test method new_check()"""
        self.assertEqual(True, FDC.new_check())


class TestDoubleRandomTask(unittest.TestCase):
    """测试双随机任务"""
    @unittest.skip("I don't want to run this case.")
    def test_double_random_task(self):
        self.assertEqual(True, FDC.double_random_task())


class TestNormalTask(unittest.TestCase):
    """测试普通任务.py"""
    @unittest.skip("I don't want to run this case.")
    def test_normal_task(self):
        self.assertEqual(True, FDC.normal_task())


class TestNewTemplate(unittest.TestCase):
    """测试普通任务.py"""
#    @unittest.skip("I don't want to run this case.")

    def test_new_template(self):
        self.assertEqual(True, FDC.new_template())
if __name__ == '__main__':
    unittest.main()
