from selenium import webdriver
from selenium.common import exceptions
import time
import pandas as pd
DRIVER_PATH = 'C:/Users/Alizeh/Desktop/asugsv/chromedriver_win32/chromedriver.exe'
EMAIL = 'alizehfatima96@gmail.com'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://virtual.asugsvsummit.com/auth/emailLogin/verify?token=NkqZ7YheqPPF3ahotKTV7ezLvQGdcmdXJWErd6SzBq3Nt1jxC&eventGroupId=32821&redirectUrl=https://virtual.asugsvsummit.com/2020/community')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

names = []
roles = []
organization = []
i=1

try:
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(6)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        
        if lastCount==lenOfPage:
            match=True
    
    while(driver.find_element_by_xpath('//div[@class="padding-bottom-huge"]/div[1]/div[@class="community-list-item"]['+str(i)+']')!=None):
        print("Got item " + str(i))
        names.append(driver.find_element_by_xpath('//div[@class="padding-bottom-huge"]/div[1]/div[@class="community-list-item"]['+str(i)+']/div[@class="community-box margin-bottom-small"]/a[@class="no-color"]/div[@class="community-list-item-content"]/div[@class="header"]').text)
        roles.append(driver.find_element_by_xpath('//div[@class="padding-bottom-huge"]/div[1]/div[@class="community-list-item"]['+str(i)+']/div[@class="community-box margin-bottom-small"]/a[@class="no-color"]/div[@class="community-list-item-content"]/div[@class="sub-header one-liner padding-horizontal-small"][1]').text)
        organization.append(driver.find_element_by_xpath('//div[@class="padding-bottom-huge"]/div[1]/div[@class="community-list-item"]['+str(i)+']/div[@class="community-box margin-bottom-small"]/a[@class="no-color"]/div[@class="community-list-item-content"]/div[@class="sub-header one-liner padding-horizontal-small"][2]').text)
        i+=1
    raise exceptions.NoSuchElementException("Elements complete")
    
except exceptions.NoSuchElementException as e:
    data = {'Names': names, 'Roles': roles, 'Organizations': organization}
    df = pd.DataFrame(data)	
    df.to_csv('asugsv.csv', index=False)


# =============================================================================
# lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# match=False
# while(match==False):
#     lastCount = lenOfPage
#     time.sleep(3)
#     lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
#     if lastCount==lenOfPage:
#         match=True
#         names = driver.find_element_by_xpath('//div[@class="community-box margin-bottom-small"]/a[@class="no-color"]/div[@class="community-list-item-content"]/div[@class="header"]').text
#         roles = driver.find_element_by_xpath('//div[@class="community-box margin-bottom-small"]/a[@class="no-color"]/div[@class="community-list-item-content"]/div[@class="sub-header one-liner padding-horizontal-small"][1]').text
#         organization = driver.find_element_by_xpath('//div[@class="community-box margin-bottom-small"]/a[@class="no-color"]/div[@class="community-list-item-content"]/div[@class="sub-header one-liner padding-horizontal-small"][2]').text
# 
