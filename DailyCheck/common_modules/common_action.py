# coding=utf-8
import re
import time
import shutil
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class Setup(object):

    # 建立驱动，选择系统，选择菜单
    def __init__(self, url):
        self.url = url

    def setup_driver(self, username, password, first_menu, second_menu):
        # 连接浏览器驱动并选择所需要测试的系统
        chrome_option = Options()
        # 是否选择以无头模式运行：可能使用不太正常
        # chrome_option.add_argument("--headless")
        chrome_option.add_argument('--log-level=3')
        driver = webdriver.Chrome(executable_path=(r'C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'), chrome_options=chrome_option)
        '''
        driver = webdriver.Ie()
        '''
        driver.maximize_window()  # 窗口最大化
        self.driver = driver
        self.driver.get(self.url)
        self.driver.find_element_by_id("j_username").send_keys("%s" % username)
        self.driver.find_element_by_id("j_password").send_keys("%s" % password)
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@id='form-ok']").click()
        time.sleep(2)
        x = 0
        while x < 10:  # 因为系统升级后经常登陆后跳转到404，所以此处while逻辑为判断是否是404，是的话则重新登陆
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            current_html = self.driver.page_source
            soup = BeautifulSoup(current_html, 'lxml')
            target = soup.find('h1', string=re.compile('404 Not Found'))
            if target == None:  # 没有查到“没有查询到数据字样，证明有数据”
                true_or_false = True
            else:
                true_or_false = False
            if true_or_false:
                break
            else:
                self.driver.get(self.url)
                self.driver.find_element_by_id("j_username").send_keys("%s" % username)
                self.driver.find_element_by_id("j_password").send_keys("%s" % password)
                time.sleep(1)
                self.driver.find_element_by_xpath("//button[@id='form-ok']").click()
                time.sleep(2)
                x += 1
        try:
            locate_first_menu = self.driver.find_element_by_xpath("//span[@class='applyText'][contains(text(),'%s')]" % first_menu)
            if second_menu == '行政执法' or second_menu == '投诉举报' or second_menu == '风险预警' or second_menu == '分析标准' or second_menu == '移动服务' or second_menu == '考试信息':
                second_menu_class = 'extApply'  # 看前台dom可知这几个菜单的class可能是开发不规范，与别的不同
            else:
                second_menu_class = 'pic-font'
            ActionChains(self.driver).move_to_element(locate_first_menu).perform()  # IE浏览器需要移植元素上
            locate_first_menu.click()  # chorme浏览器只需要点一下就可以
            self.driver.find_element_by_xpath("//span[@class='%s'][contains(text(),'%s')]" % (second_menu_class, second_menu)).click()
        except Exception as e:
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\食品日常检查\\error_screenshot\\%ssetup_driver.png" %
                                               time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
            print('点击首页功能菜单失败，可能系统首页有报错，导致不能进行流程,截图已保存至setup_driver.png', e)
        return driver

    def choose_menu(self, first_menu, second_menu, third_menu):
        # 选择左侧菜单(如果出现冲突需要使用下边的分开写的方法)
        button = Button(self.driver)
        time.sleep(5)
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

    def choose_first_menu(self, first_menu):
        # choose_menu函数不可用（出现重复的菜单名字）时候使用此函数进行选择
        button = Button(self.driver)
        time.sleep(5)
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
            time.sleep(2)
            self.driver.find_element_by_xpath("//span[@class='menu-text'][contains(text(),'%s')]" % first_menu).click()

    def choose_second_menu(self, second_menu):
        # choose_menu函数不可用（出现重复的菜单名字）时候使用此函数进行选择
        self.driver.find_element_by_xpath("//span[@class='menu-text'][contains(text(),'%s')]" % second_menu).click()
        time.sleep(0.5)

    def choose_third_menu(self, third_menu):
        # choose_menu函数不可用（出现重复的菜单名字）时候使用此函数进行选择
        self.driver.find_element_by_xpath("//span[@class='menu-text context-menu'][contains(text(),'%s')]" % third_menu).click()
        time.sleep(3)


class SwitchToFrame(object):
    # 切换Frame：MainFrame/default_content

    def __init__(self, driver):
        self.driver = driver

    def switch_to_main_frame(self):
        # 切换到mainframe
        time.sleep(2)
        self.driver.switch_to.frame("mainFrame")
        time.sleep(1)

    def switch_to_default_content(self):
        # 切换到默认
        time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(1)


class Time(object):
    # 获取当前日期，获取当前星期，获取当前日期和详细时间

    def get_current_date(self):
        # 输出20180827
        return time.strftime('%Y%m%d', time.localtime(time.time()))

    def get_current_week(self):
        # 输出0123456，0代表周日
        return time.strftime('%w', time.localtime(time.time()))

    def get_log_time(self):
        # 输出201808271430
        return time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


class SendKeys(object):

    def __init__(self, driver):
        self.driver = driver

    def send(self, id_or_xpath, text):
        if id_or_xpath.find('/') == -1:
            # 因为xpath必然有右斜杠，如果没有的话则find方法返回的是-1，因此为id，使用方法为【SendKeys.send('id/xpath','xxx')】
            try:
                self.driver.find_element_by_id(id_or_xpath).send_keys(text)
            except Exception as e:
                print(e)
        else:
            # 如不为-1，则证明有右斜杠，则为xpath
            try:
                self.driver.find_element_by_xpath(id_or_xpath).send_keys(text)
            except Exception as e:
                print(e)


class Button(object):

    def __init__(self, driver):
        self.driver = driver

    def click(self, id_or_xpath):
        # 使用方法为【Button.click('id/xpath')】
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
        # 点击加号图标
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//i[@class='fa fa-plus']").click()
        except Exception as e:
            self.driver.find_element_by_xpath("//i[@class='fa fa-plus fa-fw']").click()
        time.sleep(5)

    def click_edit_button(self):
        # 点击编辑图标
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='fa fa-edit']").click()
        time.sleep(5)

    def click_search_button(self):
        # 点击放大镜图标
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//i[@class='fa fa-search']").click()
        except Exception as e:
            try:
                self.driver.find_element_by_xpath("//span[@class='fa fa-search']").click()
            except Exception as ee:
                self.driver.find_element_by_xpath("//i[@class='fa fa-search fa-fw']").click()
        time.sleep(5)

    def click_right_arrow_button(self):
        # 点击向右箭头图标
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='fa fa-chevron-right fa-fw']").click()

    def click_calendar_start_button(self):
        # 点击向日历开始
        self.driver.find_element_by_id("checkStartDate").click()

    def click_calendar_end_button(self):
        # 点击向日历结束
        self.driver.find_element_by_id("checkEndDate").click()

    def click_save_button(self):
        # 点击保存按钮
        try:
            self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        except Exception as e:
            self.driver.find_element_by_xpath("//button[@class='btn btn-success btn-sm']").click()

    def click_confirm_button(self):
        # 点击确认按钮
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()

    def click_save_as_draft_button(self):
        # 点击【存草稿按钮】
        self.driver.find_element_by_xpath("//i[@class='fa fa-save1 fa-fw']").click()

    def click_previous_button(self):
        # 点击上一步按钮
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary btn-sm nap-step-pre']").click()


class CommonAction(object):

    def __init__(self, driver):
        self.driver = driver

    def get_screenshot(self, name):
        # 使用方法为【CommonAction.get_screenshot('XXX')】,截图名称为'日期＋XXX.png'
        self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\食品日常检查\\error_screenshot\\%s%s.png" %
                                           (time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())), name))

    def find(self, find_type, find_target):
        # 输入需要查询的标签类型（如：span/a）和要查询的标签内的文字，如【soup.find('span','XXX')】，返回BS类型的元素，可以用来操作'previous_sibling'等
        # BS元素可使用的属性见：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
        while 1:
            try:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(2)
                try:
                    self.driver.find_element_by_id("grid_length").click()
                    self.driver.find_element_by_xpath("//option[@value='100']").click()
                except Exception:
                    pass
                current_html = self.driver.page_source
                soup = BeautifulSoup(current_html, 'lxml')
                target = soup.find(find_type, string=re.compile(find_target))
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
        # 判断数据是否存在，适用于日常检查选择企业的对话框
        while 1:
            try:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 避免动态加载
                time.sleep(2)
                current_html = self.driver.page_source
                soup = BeautifulSoup(current_html, 'lxml')
                target = soup.find('span', string=re.compile('没有查询到数据'))
                if target == None:  # 没有查到“没有查询到数据”字样，证明有数据
                    return True
                else:
                    return False
            except Exception as e:
                print(e)
                break

    def scroll_and_switch_to_iframe(self):
        # 滚动一下避免动态加载，然后切换到iframe
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.switch_to.default_content()
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
        self.driver.switch_to.frame(iframe)

    def log(self):
        # 保存当前html
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + 'logging error...')
        with open('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\error_HTML.txt', 'a', encoding='UTF-8')as f:
            f.write('=' * 50)
            f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            f.write(self.driver.page_source)
            f.write('=' * 50)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + 'logged...')

    def clean_log(self):
        # 删除log
        my_file = 'C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\error_HTML.txt'
        if os.path.exists(my_file):
            shutil.rmtree(my_file)
        print('error_HTML.txt已被删除')

    def click_error_button(self):
        # 点击报错提示的确定按钮
        try:
            time.sleep(5)
            self.driver.switch_to.default_content()
            self.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管\\食品日常检查\\error_screenshot\\%schoose_menu.png" %
                                               time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
            button.click_confirm_button()
            print(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '检测到有错误弹窗')
        except:
            pass
