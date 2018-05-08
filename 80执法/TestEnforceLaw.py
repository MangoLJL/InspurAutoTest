#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class TestEnforceLaw(object):
	def __init__(self,url):
		self.url=url
		
		#连接浏览器驱动
	def SetupDriver(self):
		chrome_option=Options()
		#chrome_option.add_argument("--headless")
		driver=webdriver.Chrome(executable_path=(r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'),chrome_options=chrome_option)		
		driver.maximize_window()
		return driver

		#登陆页面并点击行政执法
	def LoginAndClickEnforceLaw(self,driver):
		driver.get(self.url)
		driver.find_element_by_id("j_username").send_keys("YUANGONG01")
		driver.find_element_by_id("j_password").send_keys("1")
		time.sleep(1)
		driver.find_element_by_xpath("//button[@id='form-ok']").click()
		time.sleep(2)
		driver.find_element_by_xpath("//span[@class='applyText'][contains(text(),'政务办公')]").click()
		driver.find_element_by_xpath("//a[@id='000000000000000000000000018266']//i[@class='fa fa-file-text-o circle fa-2x fa-blue']").click()


		#新建案件
	def NewCase(self,driver):
		driver.find_element_by_xpath("//span[@id='000000000000000000000000018267']").click()
		driver.find_element_by_xpath("//span[@id='ELCASE00002']").click()
		driver.switch_to.frame("mainFrame")
		time.sleep(2)
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		driver.find_element_by_xpath("//*[@id='productType']/li[1]/p[1]").click()
		driver.find_element_by_xpath("//html//ul[@id='caseProgram']/li[1]").click()
		driver.find_element_by_xpath("//div[@class='confirm f16 confirmselected']").click()
		time.sleep(5)
		driver.switch_to.frame("formFrame")
		time.sleep(2)
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")		
		driver.find_element_by_xpath("//html//div[@id='partyInfo']//div[1]/label[1]/input[1]").click()
		driver.find_element_by_xpath("//input[@id='partyName']").send_keys('SD')
		driver.find_element_by_xpath("//input[@id='partyName']").send_keys(Keys.ARROW_DOWN)
		time.sleep(1)
		driver.find_element_by_xpath("//input[@id='partyName']").send_keys(Keys.ARROW_DOWN)
		driver.find_element_by_xpath("//input[@id='partyName']").send_keys(Keys.ENTER)
		driver.find_element_by_id("orgTypeId0").click()
		driver.find_element_by_xpath("//html//div[@data-bind='foreach:caseSouTypeDs']/div[1]/label[1]/input[1]").click()
		driver.switch_to.parent_frame()
		driver.find_element_by_id("el_save").click()
		time.sleep(6)
		driver.find_element_by_id("el_saveAndSendFilCase").click()
		time.sleep(2)
		driver.switch_to.default_content()
		iframe=driver.find_element_by_xpath("//iframe[contains(@id,'layui-layer-iframe')]")
		driver.switch_to.frame(iframe)
		driver.find_element_by_xpath("//*[@id='organInfoTab']").click()
		time.sleep(2)
		driver.find_element_by_xpath("//i[@class='fa fa-long-arrow-right']").click()
		driver.find_element_by_xpath("//i[@class='fa fa-check fa-fw']").click()


		#案件查询
	def SearchCase(self,driver):
		driver.find_element_by_xpath("//span[@id='000000000000000000000000018267']").click()
		driver.find_element_by_id("ELCASE00005").click()
		driver.switch_to.frame("mainFrame")
		time.sleep(2)
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		driver.find_element_by_xpath("//a[@title='测试充电的']").click()



