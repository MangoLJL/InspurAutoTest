import os
import time
import shutil
import pyforms
import threading
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlCombo
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlLabel
from pyforms.controls import ControlCheckBoxList


class AutoTestGUI(BaseWidget):

    def __init__(self):
        super(AutoTestGUI, self).__init__('AutoTestGUI')
        self.current_hour = None
        self.current_minute = None

        self.check_box_list = ControlCheckBoxList('Choose Tests:')
        self.check_box_list += ('Food New Template', False)
        self.check_box_list += ('Food Simple Template', False)
        self.check_box_list += ('Food New Check', False)
        self.check_box_list += ('Food Double Random Check', False)
        self.check_box_list += ('Food Normal Task', False)
        self.check_box_list += ('Food Save Draft', False)
        self.check_box_list += ('Makeup New Template', False)
        self.check_box_list += ('Makeup Simple Template', False)
        self.check_box_list += ('Drug New Template', False)
        self.check_box_list += ('Drug Simple Template', False)

        self.pull_from_github = ControlButton('Pull From GitHub')
        self.pull_from_github.value = self.pull_from_github_action_thread_button

        self.run_daily_check_test_suite = ControlButton('Run Test Suite')
        self.run_daily_check_test_suite.value = self.run_daily_check_test_suite_action_thread_button

        self.open_test_report = ControlButton('Open Latest Test Report')
        self.open_test_report.value = self.open_test_report_action_thread_button

        self.delete_test_report = ControlButton('Delete Test Report')
        self.delete_test_report.value = self.delete_test_report_action_thread_button

        self.delete_screenshot = ControlButton('Delete Screenshot')
        self.delete_screenshot.value = self.delete_screenshot_action_thread_button

        self.label = ControlLabel('运行结果:')
        self.result_text = ControlLabel('结果将在此处显示...')

        self.set_margin(20)
        self.formset = ['check_box_list', ('pull_from_github', 'run_daily_check_test_suite', 'open_test_report'),
                        ('delete_test_report', 'delete_screenshot'), 'label', 'result_text']

    def pull_from_github_action_thread_button(self):
        self.pull_from_github_action_thread = threading.Thread(target=self.pull_from_github_action)
        self.pull_from_github_action_thread.start()

    def run_daily_check_test_suite_action_thread_button(self):
        self.run_daily_check_test_suite_action_thread = threading.Thread(target=self.run_daily_check_test_suite_action)
        self.run_daily_check_test_suite_action_thread.start()

    def open_test_report_action_thread_button(self):
        self.open_test_report_action_thread = threading.Thread(target=self.open_test_report_action)
        self.open_test_report_action_thread.start()

    def delete_test_report_action_thread_button(self):
        self.delete_test_report_action_thread = threading.Thread(target=self.delete_test_report_action)
        self.delete_test_report_action_thread.start()

    def delete_screenshot_action_thread_button(self):
        self.delete_screenshot_action_thread = threading.Thread(target=self.delete_screenshot_action)
        self.delete_screenshot_action_thread.start()

    def pull_from_github_action(self):
        result = os.popen("cd C:\\Users\\Administrator\\Documents\\PythonAutoTest&&git pull")
        self.result_text.value = result.read()

    def run_daily_check_test_suite_action(self):
        test_list = self.check_box_list.value
        test_str = ''
        for i in range(len(test_list)):
            test_str = test_str + test_list[i] + ';'
        self.current_hour = time.strftime('%Y-%m-%d_%H', time.localtime(time.time()))
        self.current_minute = time.strftime('%M', time.localtime(time.time()))
        result = os.popen("cd C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管&&python test_suite.py %s" % test_str)
        self.result_text.value = result.read()

    def open_test_report_action(self):
        try:
            file_path = 'C:\\Users\\Administrator\\Documents\\PythonAutoTest\\TestReport'
            lists = os.listdir(file_path)
            lists.sort(key=lambda fn: os.path.getmtime(file_path + '/' + fn))
            latest_file_path = file_path + '\\' + lists[-1]
            os.popen(latest_file_path)
        except Exception as e:
            self.result_text.value = '打开文件失败...'

    def delete_test_report_action(self):
        my_file = 'C:\\Users\\Administrator\\Documents\\PythonAutoTest\\TestReport'
        if os.path.exists(my_file):
            shutil.rmtree(my_file)
            os.makedirs(my_file)
            self.result_text.value = 'Test Report Deleted'
        else:
            os.makedirs(my_file)
            self.result_text.value = 'Dictionary Created...'

    def delete_screenshot_action(self):
        my_file = 'C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot'
        if os.path.exists(my_file):
            shutil.rmtree(my_file)
            os.makedirs(my_file)
            self.result_text.value = 'Screenshot Deleted'
        else:
            os.makedirs(my_file)
            self.result_text.value = 'Dictionary Created...'

if __name__ == "__main__":
    pyforms.start_app(AutoTestGUI)
'''

class main:

    def newThread(self):
        Thread(target=self.method).start()

    def method(self):
        for i in range(3):
            time.sleep(1)
            print(i)

op = main()
win = tk.Tk()
win.title("Python")


def click():
    op.newThread()

action = ttk.Button(win, text="Click Me!", command=click)  # 7
action.grid(column=0, row=0)
win.mainloop()
'''
