# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:16:27 2019

@author: Umaima
"""

# Gmail automation with selenium

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

class GmailBot:

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.gmail.com/")
        time.sleep(2)
        
        emailElem = driver.find_element_by_id('identifierId')
        emailElem.send_keys(self.email)
        nextButton = driver.find_element_by_id('identifierNext')
        nextButton.click()
        time.sleep(2)
        passwordElem = driver.find_element_by_name('password')
        passwordElem.send_keys(self.password)
        driver.find_element_by_id('passwordNext').click()
        
        # scroll all mails
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        account_button = driver.find_element_by_xpath("//a[@href='https://accounts.google.com/SignOutOptions?hl=en-GB&continue=https://mail.google.com/mail&service=mail']")
        account_button.click()
        time.sleep(6)
        logout_button = driver.find_element_by_xpath("//a[@id='gb_71']")
        logout_button.click()
        
        
if __name__ == "__main__":

    email = "email id"
    password = "password"

    gb = GmailBot(email, password)
    gb.login()
    time.sleep(5)
    gb.closeBrowser()