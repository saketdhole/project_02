from time import sleep

from pageObject.homepage import homepage


class Testregistration:
    def test_001_registration(self,setup):
        self.driver=setup
        self.driver.get("https://demo.nopcommerce.com/")
        hp=homepage(self.driver)
        hp.fun_clickregister()
        sleep(2)
