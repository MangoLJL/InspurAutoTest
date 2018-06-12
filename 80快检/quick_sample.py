from common_action import *
from sample_actions import *


def new_sample():
    # 新建快检并针对此任务发起检查
    try:
        new_sample_setup = Setup('http://10.12.1.80/portal/jsp/public/login.jsp')
        driver = new_sample_setup.setup_driver('YUANGONG01', '1', '智慧监管', '济南食品快检')
        new_sample_setup.choose_menu('新建快检', '新建快检')
        switch_to_frame = SwitchToFrame(driver)
        switch_to_frame.switch_to_main_frame()
        sample_actions = SampleActions(driver)
        sample_actions.new_sample()
    except Exception as e:
        print(e)
new_sample()
