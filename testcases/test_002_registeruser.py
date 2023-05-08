from time import sleep

from pageObject.homepage import homepage
from pageObject.registerpage import register


class Testclass:
    def test_002_registeruser(self,setup):
        self.driver=setup
        self.driver.get("https://demo.nopcommerce.com/")

        hp=homepage(self.driver)
        hp.fun_clickregister()

        rp=register(self.driver)
        rp.fun_setgender()
        sleep(2)
        rp.fun_setfname("saket")
        rp.fun_setlname("dhole")
        rp.fun_setdatemonthyear("23","5","1996")
        rp.fun_setemail("saket.dhole@gmail.com")
        rp.fun_setcname("Engineering works")
        rp.fun_password("saket123")
        rp.fun_cpassword("saket123")
        rp.fun_clickregister()
        self.confirmmsg=rp.fun_checkconfirmmessage()
        if self.confirmmsg == "Your registration completed":
            assert True
        else:
            assert False
