import os
from time import sleep

from selenium import webdriver

from pageObject.myaccountpage import myaccount
from utilities.readproperties import Readconfig
from pageObject.homepage import homepage
from pageObject.loginpage import login
from utilities.customLogger import logen


class Testlogin:

    url =Readconfig.getapplicationurl()
    email=Readconfig.getemail()
    pas=Readconfig.getpassword()
    log=logen.configure_logging()


    def test_003_login(self,setup):

        self.log.info("*** Starting login testcase***")
        self.driver=setup

        self.log.info("Fetching url")
        self.driver.get(self.url)
        hp=homepage(self.driver)
        self.log.info("clicking on login")
        hp.fun_clicklogin()
        sleep(2)
        self.log.info("Entering login page")

        lp=login(self.driver)
        self.log.info("Entering email")
        lp.fun_enteremail(self.email)
        self.log.info("Enrtering password")
        lp.fun_enterpassword(self.pas)
        sleep(2)
        self.log.info("Clicking on login")
        lp.fun_clicklogin()
        sleep(3)
        self.log.info("Checking validation after login")
        self.welcome=lp.fun_checkwelcometext()

        if self.welcome=="Welcome to our store":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+ "\\screenshots\\"+ "login.png")
            assert False

        self.ap=myaccount(self.driver)
        self.ap.fun_clicklogout()
        sleep(2)


        self.log.info("***End of login test case ***")

