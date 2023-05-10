from selenium import webdriver
from selenium.webdriver.common.by import By


class myaccount:
    LINK_LOGOUT_XPATH='//a[@class="ico-logout"]'

    def __init__(self,driver):
        self.driver=driver
        #self.driver=webdriver.Chrome()


    def fun_clicklogout(self):
        self.driver.find_element(By.XPATH,self.LINK_LOGOUT_XPATH).click()
