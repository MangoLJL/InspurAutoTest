# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from actions import Setup, LoginAndClick, SwitchToFrame, NewCheck

dc = Setup()
driver = dc.setup_driver()
login_and_click = LoginAndClick(driver, 'http://10.12.1.80/portal/jsp/public/login.jsp')
new_check = NewCheck(driver)
switch_to_frame = SwitchToFrame(driver)


login_and_click.login_and_click()
new_check.click_food_new_check()
switch_to_frame.switch_to_main_frame()
new_check.first_step()
new_check.second_step()
new_check.third_step()
