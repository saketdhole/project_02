import os
from time import sleep

from pageObject.homepage import homepage
from pageObject.registerpage import register
from utilities.randomstring import random_string_genrator
from utilities.readproperties import Readconfig
from utilities.customLogger import logen


class Testclass:
    email=random_string_genrator()
    BASEURL=Readconfig.getapplicationurl()
    logs=logen.configure_logging()



    def test_002_registeruser(self,setup):
        self.driver=setup
        self.logs.info("*** Started registration testcase ***")

        self.driver.get(self.BASEURL)
        hp=homepage(self.driver)

        self.logs.info("Clicking register")
        hp.fun_clickregister()

        rp=register(self.driver)
        rp.fun_setgender()
        sleep(2)
        self.logs.info("Entering firstname")
        rp.fun_setfname("saket")
        self.logs.info("Entering lastname")
        rp.fun_setlname("dhole")
        self.logs.info("Entering dob")
        rp.fun_setdatemonthyear("23","5","1996")
        self.logs.info("Entering email")
        rp.fun_setemail(self.email+"@gmail.com")
        self.logs.info("Entering company name")
        rp.fun_setcname("Engineering works")
        sleep(2)
        self.logs.info("Entering password")
        rp.fun_password("saket123")
        sleep(2)
        self.logs.info("Confirming password")
        rp.fun_confirmpassword("saket123")
        rp.fun_clickregister()
        self.confirmmsg=rp.fun_checkconfirmmessage()
        self.logs.info("Checking validation message")
        if self.confirmmsg == "Your registration completed":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "register.png")
            assert False
        sleep(2)

        self.logs.info("**** Registration test case Ends ***")
