import TestEnforceLaw.py

mytest=TestEnforceLaw("http://10.12.1.80/portal/jsp/public/login.jsp")
driver=mytest.SetupDriver()
mytest.LoginAndClickEnforceLaw(driver)
mytest.NewCase(driver)
