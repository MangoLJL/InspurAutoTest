import unittest
from makeup_daily_check import *


class TestNewCheck(unittest.TestCase):
    """测试新建检查"""
#    @unittest.skip("I don't want to run this case.")

    def test_new_check(self):
        """Test method new_check()"""
        self.assertEqual(True, new_check())


class TestDoubleRandomTask(unittest.TestCase):
    """测试双随机任务"""
#    @unittest.skip("I don't want to run this case.")

    def test_double_random_task(self):
        self.assertEqual(True, double_random_task())


class TestNormalTask(unittest.TestCase):
    """测试普通任务.py"""
#    @unittest.skip("I don't want to run this case.")

    def test_normal_task(self):
        self.assertEqual(True, normal_task())
if __name__ == '__main__':
    unittest.main()
