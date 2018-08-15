# coding=utf-8
import sys
sys.path.append('C:\\Users\\Administrator\\Documents\\PythonAutoTest\\DailyCheck\\common_modules')
from common_modules.MailSender import MailSender


receiver_addr = ['shr1213@live.com']  # 填写收件人邮箱
sender_name = 'GoldMonitor'
my_sender = '345753110@qq.com'
my_pass = 'kohdrckbrfoicahj'
subject = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + 'TestReport'


def send_text_report_html(test_report_path):
    MS = MailSender(my_sender, my_pass, sender_name, receiver_addr, content, subject)
    MS.send_html(test_report_path)
