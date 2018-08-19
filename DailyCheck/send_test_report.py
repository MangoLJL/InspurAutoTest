# coding=utf-8
import sys
import time
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\common_modules')
from common_modules.MailSender import MailSender


receiver_addr = []
sender_name = 'TestResult'
subject = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + 'TestReport'


def send_text_report_html(test_report_path, sender_address, sender_password, receiver_address):
    my_sender = sender_address
    my_pass = sender_password
    receiver_addr.append(receiver_address)
    MS = MailSender(my_sender, my_pass, sender_name, receiver_addr, subject)
    MS.send_html(test_report_path)
