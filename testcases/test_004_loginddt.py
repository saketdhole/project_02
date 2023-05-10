import os
from time import sleep

from utilities.customLogger import logen
from utilities.readproperties import Readconfig
from pageObject.homepage import homepage
from pageObject.loginpage import login
from pageObject.myaccountpage import myaccount
from utilities import XLUtils

class Testloginddt:

    url= Readconfig.getapplicationurl()

    logs=logen.configure_logging()
    path=os.path.abspath(os.curdir) + "\\Testdata\\"+"Nopcommerce_logindata.xlsx"

    def test_004_loginddt(self,setup):
        self.logs.info("***Starting DDT testcase***")

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        status=[]
        self.driver=setup
        self.logs.info("Fetching url")
        self.driver.get(self.url)
        self.logs.info("Clicking login button")
        self.hp=homepage(self.driver)
        self.lp=login(self.driver)
        self.ma=myaccount(self.driver)

        for r in range(2,self.rows+1):
            self.hp.fun_clicklogin()
            self.email=XLUtils.readData(self.path,"Sheet1",r,1)
            self.pas=XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp=XLUtils.readData(self.path,"Sheet1",r,3)
            self.lp.fun_enteremail(self.email)
            self.lp.fun_enterpassword(self.pas)
            self.lp.fun_clicklogin()
            sleep(2)
            self.target=self.lp.fun_checkwelcometext()
            if self.exp=="Pass":
                if self.target=="Welcome to our store":
                    status.append('Pass')
                    self.ma.fun_clicklogout()
                else:
                    status.append('Fail')

            elif self.exp=="Fail":
                if self.target=="Welcome to our store":
                    status.append("Fail")
                    self.ma.fun_clicklogout()
                else:
                    status.append('True')

            if "Fail" not in status:
                assert True
            else:
                assert False
            self.logs.info("***Login DDT Ends***")





