# coding=utf-8
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


# 建立驱动，选择系统，选择菜单


class Setup(object):

    def __init__(self, url):
        self.url = url

        # 连接浏览器驱动并选择所需要测试的系统
    def setup_driver(self, username, password, first_menu, second_menu):
        chrome_option = Options()
        # 是否选择以无头模式运行：可能使用不太正常
        # chrome_option.add_argument("--headless")

        chrome_option.add_argument('--log-level=3')
        driver = webdriver.Chrome(executable_path=(r'C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'), chrome_options=chrome_option)
        '''
        driver = webdriver.Ie()
        '''
        driver.maximize_window()
        self.driver = driver
        self.driver.get(self.url)
        self.driver.find_element_by_id("j_username").send_keys("%s" % username)
        self.driver.find_element_by_id("j_password").send_keys("%s" % password)
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@id='form-ok']").click()
        time.sleep(2)
        try:
            locate_first_menu = self.driver.find_element_by_xpath("//span[@class='applyText'][contains(text(),'%s')]" % first_menu)
            # locate_first_menu.click()  # chorme浏览器只需要点一下就可以
            ActionChains(self.driver).move_to_element(locate_first_menu).perform()  # IE浏览器需要移植元素上
            if second_menu == '行政执法' or second_menu == '投诉举报' or second_menu == '风险预警' or second_menu == '分析标准' or second_menu == '移动服务' or second_menu == '考试信息':
                second_menu_class = 'extApply'
            else:
                second_menu_class = 'pic-font'
            self.driver.find_element_by_xpath("//span[@class='%s'][contains(text(),'%s')]" % (second_menu_class, second_menu)).click()
        except Exception as e:
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\食品日常检查\\error_screenshot\\%ssetup_driver.png" %
                                               time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
            print('点击首页功能菜单失败，可能系统首页有报错，导致不能进行流程,截图已保存至setup_driver.png', e)
        return driver

        # 选择左侧菜单
    def choose_menu(self, first_menu, second_menu, third_menu):
        button = Button(self.driver)
        time.sleep(10)
        try:
            self.driver.switch_to.default_content()
            self.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\食品日常检查\\error_screenshot\\%schoose_menu.png" %
                                               time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
            button.click_confirm_button()
            print('系统首页检测到有错误弹窗,截图已保存至choose_menu.png')
        except:
            pass
        finally:
            self.driver.find_element_by_id("menu-toggler").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//span[@class='menu-text'][contains(text(),'%s')]" % first_menu).click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//span[@class='menu-text'][contains(text(),'%s')]" % second_menu).click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//span[@class='menu-text context-menu'][contains(text(),'%s')]" % third_menu).click()
            time.sleep(5)

# 切换Frame：MainFrame/default_content


class SwitchToFrame(object):

    def __init__(self, driver):
        self.driver = driver

    def switch_to_main_frame(self):
        time.sleep(2)
        self.driver.switch_to.frame("mainFrame")
        time.sleep(1)

    def switch_to_default_content(self):
        time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(1)

# 获取当前日期，获取当前星期，获取当前日期和详细时间


class Time(object):

    def get_current_date(self):
        return time.strftime('%Y%m%d', time.localtime(time.time()))

    def get_current_week(self):
        return time.strftime('%w', time.localtime(time.time()))

    def get_log_time(self):
        return time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


class SendKeys(object):

    def __init__(self, driver):
        self.driver = driver

    def send(self, id_or_xpath, text):
        if id_or_xpath.find('/'):
            try:
                self.driver.find_element_by_xpath(id_or_xpath).send_keys(text)
            except Exception as e:
                print(e)
        else:
            try:
                self.driver.find_element_by_id(id_or_xpath).send_keys(text)
            except Exception as e:
                print(e)


class Button(object):

    def __init__(self, driver):
        self.driver = driver

    def click(self, id_or_xpath):
        if id_or_xpath.find('/') == -1:
            try:
                self.driver.find_element_by_id(id_or_xpath).click()
            except Exception as e:
                print(e)
        else:
            try:
                self.driver.find_element_by_xpath(id_or_xpath).click()
            except Exception as e:
                print(e)

    def click_plus_button(self):
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//i[@class='fa fa-plus']").click()
        except Exception as e:
            self.driver.find_element_by_xpath("//i[@class='fa fa-plus fa-fw']").click()
        time.sleep(5)

    def click_edit_button(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='fa fa-edit']").click()
        time.sleep(5)

    def click_search_button(self):
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//i[@class='fa fa-search']").click()
        except Exception as e:
            self.driver.find_element_by_xpath("//span[@class='fa fa-search']").click()
        time.sleep(5)

    def click_right_arrow_button(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='fa fa-chevron-right fa-fw']").click()

    def click_calendar_start_button(self):
        self.driver.find_element_by_id("checkStartDate").click()

    def click_calendar_end_button(self):
        self.driver.find_element_by_id("checkEndDate").click()

    def click_save_button(self):
        try:
            self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        except Exception as e:
            self.driver.find_element_by_xpath("//button[@class='btn btn-success btn-sm']").click()

    def click_confirm_button(self):
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()


class CommonAction(object):

    def __init__(self, driver):
        self.driver = driver

    def get_screenshot(self, name):
        self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\食品日常检查\\error_screenshot\\%s%s.png" %
                                           (time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())), name))

    def find(self, find_target):
        while 1:
            try:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(2)
                current_html = self.driver.page_source
                soup = BeautifulSoup(current_html, 'lxml')
                target = soup.find('a', string=re.compile(find_target))
                if target == None:
                    # 如果本页没有查询到，则查询下一页
                    next_page_status = soup.find(class_='paginate_button next disabled')  # 判断是否已经到最后一页：即下一页按钮没法点了
                    if next_page_status == None:
                        try:
                            self.driver.find_element_by_xpath("//a[@href='#'][contains(text(),'下一页')]").click()
                        except Exception as e:
                            print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '查询%s失败，错误信息：' % task_name, e)
                    else:
                        print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '已至最后一页仍未发现结果')
                        return None
                else:
                    return target
            except Exception as e:
                print(e)
                break

    def data_exsists(self):
        while 1:
            try:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(2)
                current_html = self.driver.page_source
                soup = BeautifulSoup(current_html, 'lxml')
                target = soup.find('span', string=re.compile('没有查询到数据'))
                if target == None:  # 没有查到“没有查询到数据字样，证明有数据”
                    return True
                else:
                    return False
            except Exception as e:
                print(e)
                break

    def scroll_and_switch_to_iframe(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.switch_to.default_content()
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)
