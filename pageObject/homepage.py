from selenium import webdriver
from selenium.webdriver.common.by import By


class homepage:
    linktext_register_linktext="Register"

    def __init__(self,driver):
        self.driver=driver
        #self.driver=webdriver.Chrome()

    def fun_clickregister(self):
        self.driver.find_element(By.LINK_TEXT,self.linktext_register_linktext).click()


