from time import sleep

from selenium import webdriver

from utilities.readproperties import Readconfig
from pageObject.homepage import homepage
from pageObject.loginpage import login


class Testlogin:

    url =Readconfig.getapplicationurl()


    def test_003_login(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        hp=homepage(self.driver)
        hp.fun_clicklogin()
        sleep(2)

        lp=login(self.driver)
        lp.fun_enteremail("saket.dhole@gmail.com")
        lp.fun_enterpassword("saket123")
        sleep(2)
        lp.fun_clicklogin()
        sleep(3)
        self.welcome=lp.fun_checkwelcometext()

        if self.welcome=="Welcome to our store":
            assert True
        else:
            assert False


