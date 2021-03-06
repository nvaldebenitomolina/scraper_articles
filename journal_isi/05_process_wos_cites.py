#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import re
import operator
import matplotlib.pyplot as plt
import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#open dataframe DOI
df = pd.read_csv("input_table/00_cr2_articles.csv", sep=',', encoding='utf-8')

DOI = df["DOI"]
#print(DOI_1[65])

#DOI= DOI_1.drop(DOI_1.index[65])
#print(DOI[64])

#DOI.reset_index(drop=True)

#DOI.index = pd.RangeIndex(len(DOI.index))
#DOI.remove["10.1177/0263774X15614734"]
#10.1080/17477891.2015.1134427
#print(DOI[64])
#print(DOI[65])
#print(DOI[66])

DOI_SCOPUS=[]
DOI_WEBOFS=[]

#write string
for i in range(0,len(DOI)):
	DOI_SCOPUS.append(str(" DOI(")+str(DOI[i])+str(")"))

for i in range(0,len(DOI)):
	DOI_WEBOFS.append(str(" DO=(")+str(DOI[i])+str(")"))

DOI_SCOPUS="".join(DOI_SCOPUS)
DOI_WEBOFS=" OR".join(DOI_WEBOFS)

#print(DOI_WEBOFS)
user_webofs="nancyvaldebenitomo@gmail.com"
password_webofs="nancy@176237015"




#Affiliations with Web of Science
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get("http://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?SID=7CWt7eMDxKOrXhHC3cS&product=WOS&search_mode=AdvancedSearch")

#click item add user and password
enter = driver.find_elements_by_xpath('//div[contains(@class, "navBar") and contains(@class,"clearfix")]')
enter = driver.find_elements_by_xpath('//ul[contains(@class, "UserCabinet") and contains(@class,"nav-list")]')
enter = driver.find_elements_by_xpath('//li[contains(@class, "nav-item")]')
enter = driver.find_elements_by_xpath('//li[contains(@class, "nav-item") and contains(@class,"show-subnav")]')
enter = driver.find_element_by_xpath('//a[contains(@title, "Iniciar sesión") and contains(@class,"nav-link") and contains(@id,"signin")]')
enter.click()

#sign in
enter = driver.find_element_by_xpath('//ul[contains(@class, "subnav")]')
enter = driver.find_element_by_xpath('//li[contains(@class, "subnav-item")]')
enter = driver.find_element_by_xpath('//a[contains(@class, "subnav-link") and contains(@class,"snowplow-header-signin")]')
enter.click()

#add user
enter = driver.find_elements_by_xpath('//td[contains(@width, "50%") and contains(@class,"csi-left-column")]')
enter = driver.find_elements_by_xpath('//td[contains(@align, "left") and contains(@class,"csi-login-input")]')
enter = driver.find_element_by_id('email')
enter.send_keys(user_webofs)

#add password
enter = driver.find_elements_by_xpath('//td[contains(@width, "50%") and contains(@class,"csi-left-column")]')
enter = driver.find_elements_by_xpath('//td[contains(@align, "left") and contains(@class,"csi-login-input")]')
enter = driver.find_element_by_xpath('//input[contains(@type, "password") and contains(@name,"password") and contains(@id,"password")]')
enter.send_keys(password_webofs)

#click enter 
enter = driver.find_elements_by_xpath('//td[contains(@class,"csi-button")]')
enter = driver.find_element_by_xpath('//button[contains(@id,"signInButton")]')
enter.click()


delay = 50 # seconds

WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@title,"Nancy") and contains(@class,"nav-link")]')))


#advanced
search = driver.find_elements_by_xpath('//div[contains(@class,"block-search") and contains(@class,"block-search-header")]')
search = driver.find_elements_by_xpath('//li[contains(@class,"searchtype-sub-nav")]')
search = driver.find_elements_by_xpath('//ul[contains(@class,"searchtype-nav")]')
search = driver.find_elements_by_xpath('//li[contains(@class,"searchtype-sub-nav__list-item")]')
search = driver.find_element_by_xpath('//a[contains(@title,"Use la búsqueda avanzada para restringir los resultados a unos criterios específicos")]')
search.click()
#add DOI
button = driver.find_element_by_id('value(input1)')
button.send_keys(DOI_WEBOFS)

#start to search
enter = driver.find_element_by_id('search-button')
enter.click()

number = driver.find_elements_by_xpath('//div[contains(@class,"historyResults")]')
number = driver.find_elements_by_xpath('//a[contains(@title,"Hacer clic para ver los resultados")]')[0].text
print(number)


#click in number of publications found
enter = driver.find_elements_by_xpath('//div[contains(@class,"historyResults")]')
enter = driver.find_element_by_xpath('//a[contains(@title,"Hacer clic para ver los resultados")]')
enter.click()

#cites
enter = driver.find_elements_by_xpath('//div[contains(@class,"l-content")]')
enter = driver.find_elements_by_xpath('//div[contains(@class,"page-options-inner")]')
enter = driver.find_elements_by_xpath('//div[contains(@class,"create-cite-report")]')
enter = driver.find_element_by_id('view_citation_report_image_placeholder')
enter = driver.find_elements_by_xpath('//div[contains(@class,"display:inline-block;whitespace:no-wrap;")]')
enter = driver.find_element_by_xpath('//a[contains(@alt,"Ver informe de citas") and contains(@title,"Ver informe de citas") and contains(@class,"snowplow-citation-report citation-report-summary-link")]')
enter.click()

#save
enter = driver.find_elements_by_xpath('//div[contains(@class,"l-content")]')
enter = driver.find_elements_by_xpath('//div[contains(@class,"select-container")]')
enter = driver.find_elements_by_xpath('//span[contains(@class,"cr_saveToButton")]')
enter = driver.find_elements_by_xpath('//select[contains(@class,"saveToMenuBottom cr_saveToMenu select2-hidden-accessible")]')
enter = driver.find_element_by_xpath('//option[contains(@selected,"selected") and contains(@value,"xls")]')
enter.click()

#from number
enter = driver.find_element_by_id('markFrom')
#enter.send_keys(1)

#to number 
enter = driver.find_element_by_id('markTo')
#enter.send_keys(number)

#Click on the input type radio, where we're selecting all.
enter = driver.find_elements_by_xpath('//div[contains(@class, "quick-output-section-content")]')
enter = driver.find_elements_by_xpath('//div[contains(@id, "records-range-radio-button")]')
enter = driver.find_element_by_xpath('//input[contains(@type, "radio") and contains(@id,"numberOfRecordsRange") and contains(@onchange,"enableExportButton()")]')
enter.click()

#download citations in csv format
enter = driver.find_element_by_xpath('//div[contains(@class,"quickoutput-overlay-buttonset")]')
enter = driver.find_element_by_xpath('//span[contains(@class,"quickoutput-action")]')
enter = driver.find_element_by_xpath('//button[contains(@class,"onload-primary-button") and contains(@id,exportButton) and contains(@alt,"Enviar")]')
enter.click()

#close
#close = driver.find_elements_by_xpath('//div[contains(@class,"ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-dialog-quickoutput")]')
#close = driver.find_element_by_id('ui-id-6')
#close = driver.find_elements_by_xpath('//form[contains(@class,"quick-output-form")]')
#close = driver.find_elements_by_xpath('//div[contains(@class,"quickoutput-overlay-buttonset")]')
#close = driver.find_element_by_xpath('//a[contains(@class,"quickoutput-cancel-action") and contains(@href,"#")]')
#close.click()

print("Download availaible /home/nvaldebenito/Descargas/ savedrecs.xls")



