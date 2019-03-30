# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:51:35 2019

@author: Umaima
"""

# importing necessary classes 
# from different modules 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 

class FacebookBot:

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        
         
  
        browser = self.driver
        browser.get("https://www.facebook.com/")
        time.sleep(2)
        element = browser.find_elements_by_xpath('//*[@id ="email"]') 
        element[0].send_keys(self.email) 
  
        #print("Username Entered") 
          
        element = browser.find_element_by_xpath('//*[@id ="pass"]') 
        element.send_keys(self.password) 
          
        #print("Password Entered") 
          
        # logging in 
        log_in = browser.find_elements_by_id('loginbutton') 
        log_in[0].click() 
  
        #print("Login Successfull") 
    
    def birthdayPost(self):
        
        browser = self.driver
        browser.get('https://www.facebook.com/events/birthdays/') 
  
        feed = 'Happy Birthday !'
          
        element = browser.find_elements_by_xpath("//*[@class ='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']") 
          
        cnt = 0
          
        for el in element: 
            cnt += 1
            element_id = str(el.get_attribute('id')) 
            XPATH = '//*[@id ="' + element_id + '"]'
            post_field = browser.find_element_by_xpath(XPATH) 
            post_field.send_keys(feed) 
            post_field.send_keys(Keys.RETURN) 
            #print("Birthday Wish posted for friend" + str(cnt)) 
    
    def logout(self):
        
        browser = self.driver
        
        nav = browser.find_element_by_xpath('//a[@id ="pageLoginAnchor"]') 
        nav.click()
        time.sleep(2)
        logout = browser.find_element_by_xpath('//li[@class ="_54ni navSubmenu _6398 _64kz __MenuItem"]')
        logout.click()
        
if __name__ == "__main__":

    email = "email id"
    password = "password"

    fb = FacebookBot(email, password)
    fb.login()
    time.sleep(5)
    fb.birthdayPost()
    time.sleep(5)
    fb.logout()
    fb.closeBrowser()