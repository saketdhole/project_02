from selenium import webdriver
from selenium.webdriver.common.by import By


class register:
    radiobutton_gender_ID="gender-male"
    textbox_firstname_ID="FirstName"
    textbox_lastname_ID="LastName"
    dropdown_day_XPATH="//select[@name='DateOfBirthDay']"
    dropdown_month_XPATH="//select[@name='DateOfBirthMonth']"
    dropdown_year_xpath="//select[@name='DateOfBirthYear']"
    textbox_email_ID="Email"
    textbox_company_ID="Company"
    textbox_password_ID="Password"
    textbox_confirmpassword_ID="ConfirmPassword"
    button_register_ID="register-button"
    confirmation_message_xpath='//div[@class="result"]'


    def __init__(self,driver):
        self.driver=driver
        #self.driver=webdriver.Chrome()

    def fun_setgender(self):
        self.driver.find_element(By.ID,self.radiobutton_gender_ID).click()

    def fun_setfname(self,fname):
        ele_fname=self.driver.find_element(By.ID,self.textbox_firstname_ID)
        ele_fname.clear()
        ele_fname.send_keys(fname)

    def fun_setlname(self,lname):
        ele_lname=self.driver.find_element(By.ID,self.textbox_lastname_ID)
        ele_lname.clear()
        ele_lname.send_keys(lname)

    def fun_setdatemonthyear(self,select_date,select_month,select_year):
        ele_date=self.driver.find_element(By.XPATH,self.dropdown_day_XPATH).click()
        ele_dateoption=self.driver.find_element(By.XPATH,f"//option[@value='{select_date}']")
        ele_dateoption.click()

        ele_month=self.driver.find_element(By.XPATH,self.dropdown_month_XPATH).click()
        ele_months=self.driver.find_element(By.CSS_SELECTOR,f"select[name='DateOfBirthMonth'] option[value='{select_month}']")
        ele_months.click()

        ele_year=self.driver.find_element(By.XPATH,self.dropdown_year_xpath).click()
        ele_yearoption=self.driver.find_element(By.XPATH,f"//select[@name='DateOfBirthYear']/option[@value='{select_year}']")
        ele_yearoption.click()

    def fun_setemail(self,email):
        ele_email=self.driver.find_element(By.ID,self.textbox_email_ID)
        ele_email.clear()
        ele_email.send_keys(email)

    def fun_setcname(self,cname):
        ele_cname= self.driver.find_element(By.ID,self.textbox_company_ID)
        ele_cname.clear()
        ele_cname.send_keys(cname)

    def fun_password(self,passs):
        ele_passs=self.driver.find_element(By.ID,self.textbox_password_ID)
        ele_passs.clear()
        ele_passs.send_keys(passs)

    def fun_cpassword(self,cpas):
        ele_cpas=self.driver.find_element(By.XPATH,self.textbox_confirmpassword_ID)
        ele_cpas.clear()
        ele_cpas.send_keys(cpas)

    def fun_clickregister(self):
        self.driver.find_element(By.ID,self.button_register_ID).click()

    def fun_checkconfirmmessage(self):
        cmsg=self.driver.find_element(By.XPATH,self.confirmation_message_xpath)
        Got=cmsg.text
        return Got

        # try:
        #     return self.driver.find_element(By.XPATH,self.confirmation_message_xpath).text
        # except:
        #     None




