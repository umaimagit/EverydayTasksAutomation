# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:20:43 2019

@author: Umaima
"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
import json

def AmazonBot(url):
    
    driver = webdriver.Chrome()
    
    driver.get(url)
    time.sleep(2)
    try:
        XPATH_NAME = '//h1[@id="title"]'
        
        XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]'
           
        XPATH_ORIGINAL_PRICE = '//td[contains(text(), "List Price") or contains(text(), "M.R.P.:") or contains(text(), "Price")]/following-sibling::td'
        XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]'
        XPATH_AVAILABILITY = '//div[@id="availability"]'
        
        RAW_NAME = driver.find_element_by_xpath(XPATH_NAME).text
        try:
            RAW_SALE_PRICE = driver.find_element_by_xpath(XPATH_SALE_PRICE).text
        except:
            RAW_SALE_PRICE = "Unable to fetch"
        time.sleep(3)
        try:
            RAW_CATEGORY = driver.find_element_by_xpath(XPATH_CATEGORY).text
        except:
            RAW_CATEGORY = "Unable to fetch"
        #RAW_CATEGORY = "Baby"
        RAW_ORIGINAL_PRICE = driver.find_element_by_xpath(XPATH_ORIGINAL_PRICE).text
        
        RAw_AVAILABILITY = driver.find_element_by_xpath(XPATH_AVAILABILITY).text
        
        #print(RAW_NAME + "," + RAW_SALE_PRICE+ "," +RAW_CATEGORY+ "," + RAW_ORIGINAL_PRICE+ "," +RAw_AVAILABILITY)
        
        NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
        SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
        #CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
        CATEGORY = RAW_CATEGORY
        ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
        AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
 
        if not ORIGINAL_PRICE:
            ORIGINAL_PRICE = SALE_PRICE
 
#        if page.status_code!=200:
#            raise ValueError('captha')
            
        data = {
                'NAME':NAME,
                'SALE_PRICE':SALE_PRICE,
                'CATEGORY':CATEGORY,
                'ORIGINAL_PRICE':ORIGINAL_PRICE,
                'AVAILABILITY':AVAILABILITY,
                'URL':url,
                }
        
        #print(data)
        
        driver.close()
        
        return data
            
    except Exception as e:
        print(e)
            
def ReadProducts():
    # AsinList = csv.DictReader(open(os.path.join(os.path.dirname(__file__),"Asinfeed.csv")))
    ProductList = ['B00PFJ00U6',
                   'B07D5V12Y8',
                   'B010D771GK',
                   'B01LQQHI8I',
                   'B077RV8CCY']
    
    extracted_data = []
    for i in ProductList:
        url = "https://www.amazon.in/dp/"+i
        print("Processing: "+url)
        extracted_data.append(AmazonBot(url))
        time.sleep(5)
        
    f=open('amazondata.json','w')
    json.dump(extracted_data,f,indent=4)
 
 
if __name__ == "__main__":
    ReadProducts()