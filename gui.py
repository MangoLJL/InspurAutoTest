import os
import time
import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlCombo
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlLabel


class AutoTestGUI(BaseWidget):

    def __init__(self):
        super(AutoTestGUI, self).__init__('AutoTestGUI')
        self.current_hour = None
        self.current_minute = None

        self.pull_from_github = ControlButton('Pull From GitHub')
        self.pull_from_github.value = self.pull_from_github_action

        self.run_daily_check_test_suite = ControlButton('Run Daily Check Test Suite')
        self.run_daily_check_test_suite.value = self.run_daily_check_test_suite_action

        self.open_test_report = ControlButton('Open Test Report')
        self.open_test_report.value = self.open_test_report_action

        self.delete_test_report = ControlButton('Delete Test Report')
        self.delete_test_report.value = self.delete_test_report_action

        self.delete_screenshot = ControlButton('Delete Screenshot')
        self.delete_screenshot.value = self.delete_screenshot_action

        self.lable = ControlLabel('运行结果:')
        self.result_text = ControlLabel('结果将在此处显示...')

        self.formset = [('pull_from_github', 'run_daily_check_test_suite', 'open_test_report'), ('delete_test_report', 'delete_screenshot'), 'lable', 'result_text']

    def pull_from_github_action(self):
        result = os.popen("cd C:\\Users\\Administrator\\Documents\\PythonAutoTest&&git pull")
        self.result_text.value = result.read()

    def run_daily_check_test_suite_action(self):
        self.current_hour = time.strftime('%Y-%m-%d_%H', time.localtime(time.time()))
        self.current_minute = time.strftime('%M', time.localtime(time.time()))
        result = os.popen("cd C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管&&python test_suite.py")
        self.result_text.value = result.read()

    def open_test_report_action(self):
        file_name = self.current_hour + '-' + self.current_minute
        try:
            my_file = ("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\TestReport\\%sTestReport.html" % file_name)
            if os.path.exists(my_file):
                os.popen("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\TestReport\\%sTestReport.html" % file_name)
            else:
                self.current_minute = str(int(self.current_minute) + 1)
                file_name = self.current_hour + '-' + self.current_minute
                os.popen("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\TestReport\\%sTestReport.html" % file_name)
        except Exception as e:
            print('打开文件失败...')

    def delete_test_report_action(self):
        my_file = 'C:\\Users\\Administrator\\Documents\\PythonAutoTest\\TestReport'
        if os.path.exists(my_file):
            shutil.rmtree(my_file)
        print('Test Report Deleted')

    def delete_screenshot_action(self):
        my_file = 'C:\\Users\\Administrator\\Documents\\PythonAutoTest\\ErrorScreenshot'
        if os.path.exists(my_file):
            shutil.rmtree(my_file)
        print('Screenshot Deleted...')

if __name__ == "__main__":
    pyforms.start_app(AutoTestGUI)
