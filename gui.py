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

        self.pull_from_github = ControlButton('pull from github')
        self.pull_from_github.value = self.pull_from_github_action

        self.run_daily_check_test_suite = ControlButton('run daily check test suite')
        self.run_daily_check_test_suite.value = self.run_daily_check_test_suite_action

        self.open_test_report = ControlButton('open test report')
        self.open_test_report.value = self.open_test_report_action

        self.test = ControlLabel('结果将在此处显示...')

        self.formset = [('pull_from_github', 'run_daily_check_test_suite', 'open_test_report'), 'test']

    def pull_from_github_action(self):
        os.popen("cd C:\\Users\\Administrator\\Documents\\PythonAutoTest")
        result = os.popen("git pull")
        self.test.value = result.read()

    def run_daily_check_test_suite_action(self):
        os.popen("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\80日常监管")
        self.current_hour = time.strftime('%Y-%m-%d_%H', time.localtime(time.time()))
        self.current_minute = time.strftime('%M', time.localtime(time.time()))
        os.popen("python test_suite")

    def open_test_report_action(self):
        file_name = self.current_hour + '-'self.current_minute
        try:
            os.popen("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\TestReport\\%sTestReport.html" % self.file_name)
        except Exception:
            self.current_minute = str(int(self.current_minute) + 1)
            file_name = self.current_hour + '-'self.current_minute
            os.popen("C:\\Users\\Administrator\\Documents\\PythonAutoTest\\TestReport\\%sTestReport.html" % self.file_name)

if __name__ == "__main__":
    pyforms.start_app(AutoTestGUI)
