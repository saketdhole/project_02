from selenium import webdriver
from selenium.webdriver.common.by import By


class login:
    TEXTBOX_EMAIL_ID="Email"
    TEXTBOX_PASSWORD_ID="Password"
    BUTTON_LOGIN_XPATH="//button[@class='button-1 login-button']"
    TEXT_WELCOMETEXT_XPATH="//div[@class='topic-block-title']/h2"

    def __init__(self,driver):
        self.driver=driver
        #self.driver=webdriver.Chrome()

    def fun_enteremail(self,email):
        ele_email=self.driver.find_element(By.ID,self.TEXTBOX_EMAIL_ID)
        ele_email.clear()
        ele_email.send_keys(email)

    def fun_enterpassword(self,pa):
        ele_pa=self.driver.find_element(By.ID,self.TEXTBOX_PASSWORD_ID)
        ele_pa.clear()
        ele_pa.send_keys(pa)

    def fun_clicklogin(self):
        self.driver.find_element(By.XPATH,self.BUTTON_LOGIN_XPATH).click()

    def fun_checkwelcometext(self):
        try:
            return self.driver.find_element(By.XPATH,self.TEXT_WELCOMETEXT_XPATH).text
        except:
            None
