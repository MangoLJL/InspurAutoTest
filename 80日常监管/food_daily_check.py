# coding=utf-8
import time
from food_actions import Setup, LoginAndClick, SwitchToFrame, NewCheck


def new_check():

    dc = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
    driver = dc.setup_driver()
    new_check = NewCheck(driver)
    switch_to_frame = SwitchToFrame(driver)
    new_check.click_food_new_check()
    switch_to_frame.switch_to_main_frame()
    new_check.first_step()
    new_check.second_step()
    new_check.third_step()
    new_check.fourth_step()
    new_check.fifth_step()
    new_check.final_step()
    driver.quit()
    print('流程测试成功，测试通过')
    return True
