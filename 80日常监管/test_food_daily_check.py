import unittest
from food_daily_check import *


class TestFoodDailyCheck(unittest.TestCase):
    """Test food_daily_check.py"""
    @unittest.skip("I don't want to run this case.")
    def test_new_check(self):
        """Test method new_check()"""
        self.assertEqual(True, new_check())

    @unittest.skip("I don't want to run this case.")
    def test_double_random_task(self):
        self.assertEqual(True, double_random_task())

    def test_normal_task(self):
        self.assertEqual(True, normal_task())
if __name__ == '__main__':
    unittest.main()
