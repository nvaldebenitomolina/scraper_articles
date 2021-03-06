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
import time

#open dataframe DOI
df = pd.read_csv("input_table/00_cr2_articles.csv", sep=',', encoding='utf-8', error_bad_lines=False)
df.dropna()
DOI = df["DOI"]



DOI_SCOPUS=[]


#write string
for i in range(0,len(DOI)):
#for i in range(0,3):
	DOI_SCOPUS.append(str(" DOI(")+DOI[i]+str(")"))

#DOI list
DOI_SCOPUS=" OR".join(DOI_SCOPUS)
print(DOI_SCOPUS)

#open webdriver
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get("http://www.scopus.com")


#user and password
user_scopus=os.environ["EMAIL"]
password_scopus=os.environ["PASSWORDSCOPUS"]

driver.maximize_window()
#wait
#delay = 50 # seconds
#WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "btn btn-secondary pull-right GuideButton  _pendo-guide-aa-conversion") and contains(@pendo-id,"Login")]')))


##login
#login = driver.find_element_by_xpath('//a[contains(@class, "btn btn-link dropdown-toggle") and contains(@title,"Sign in to Scopus")]')
#login.click()

#click item add user and password
enter = driver.find_elements_by_xpath('//div[contains(@class, "col-md-12") and contains(@class,"globalNavigation")]')
enter = driver.find_elements_by_xpath('//nav[contains(@class,"navbar col-md-11 globalNavigation")]')
enter = driver.find_elements_by_xpath('//ul[contains(@class, "globalLinks") and contains(@class,"nav navbar-nav navbar-right verticalAlign")]')
enter = driver.find_elements_by_xpath('//li[contains(@id, "usernameList")]')
enter = driver.find_elements_by_xpath('//div[contains(@id, "signin") and contains(@class,"loggedIn dropdownGroup pull-left")]')
#enter = driver.find_element_by_xpath('//a[contains(@title, "Iniciar sesión") and contains(@class,"nav-link") and contains(@id,"signin")]')
enter = driver.find_element_by_xpath('//a[contains(@id, "signin_link_move")]')
enter.click()


#username
user = driver.find_element_by_id('bdd-email')
user = driver.find_element_by_xpath('//input[contains(@type,"text") and contains(@name,"pf.username") and contains(@id,"bdd-email")]')
user.send_keys(user_scopus)

button = driver.find_element_by_id('bdd-elsPrimaryBtn')
button.click()

#password
password = driver.find_element_by_id('bdd-password')
password = driver.find_element_by_xpath('//input[contains(@type,"password") and contains(@name,"password") and contains(@id,"bdd-password")]')
password.send_keys(password_scopus)

button = driver.find_element_by_id('bdd-elsPrimaryBtn')
button.click()

#login
#enter = driver.find_element_by_id('login_submit_btn')
#enter = driver.find_element_by_xpath('//input[contains(@type,"submit") and contains(@title,"Login") and contains(@value,"Login")]')
#enter.click()

#advanced
#search = driver.find_element_by_id('internalTabs')
search = driver.find_element_by_id('advanceSearchLink')
search = driver.find_element_by_link_text("Advanced")
search.click()

#add DOI
search = driver.find_element_by_id('SCAdvSearchInputBox')
search.click()
search = driver.find_element_by_id('searchfield')
search.send_keys(DOI_SCOPUS)
#wait
delay = 1000 # seconds

#enter
enter = driver.find_element_by_xpath('//button[contains(@type,"submit") and contains(@id,"advSearch") and contains(@class,"btn btn-primary")]')
enter.click()

#Select button
select = driver.find_elements_by_xpath('//div[contains(@id,"selectAllOrPage") and contains(@class,"dropdownGroup")]')
select = driver.find_elements_by_xpath('//button[contains(@type,"button") and contains(@id,"showAllPageBubble") and contains(@class,"btn btn-link dropdown-toggle color")]')
select = driver.find_element_by_id('allPageSelectedValue')
select.click()

#All button 
select_all = driver.find_elements_by_xpath('//ul[contains(@class,"list-unstyled")]')
select_all = driver.find_elements_by_xpath('//li[contains(@class,"selectedChkBoxTxt")]')
select_all = driver.find_element_by_xpath('//label[contains(@for,"selectAllTop") and contains(@class,"checkbox-label") and contains(@title,"Select all results")]')
select_all.click()

#csv export
export = driver.find_elements_by_xpath('//span[contains(@class,"docHeaderLinks lnkEnabled")]')
export = driver.find_elements_by_xpath('//span[contains(@id,"chunkExport")]')
export = driver.find_element_by_xpath('//button[contains(@type,"button") and contains(@id,"export_results") and contains(@data-type,"exportLink")]')
export.click()


#wait
delay = 50 # seconds
WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@type,"button") and contains(@class,"btn btn-primary btn-sm") and contains(@title,"Export") and contains(@id,"exportTrigger") and contains(@name,"ExportPopUp")]')))

#button export
button = driver.find_elements_by_xpath('//div[contains(@class,"modal-content")]')
button = driver.find_elements_by_xpath('//div[contains(@class,"modal-footer noBorder")]')
button = driver.find_elements_by_xpath('//div[contains(@class,"pull-right form-inline")]')
button = driver.find_element_by_xpath('//button[contains(@type,"button") and contains(@class,"btn btn-primary btn-sm") and contains(@title,"Export") and contains(@id,"exportTrigger") and contains(@name,"ExportPopUp")]').click()

print("Download availaible /home/nvaldebenito/Descargas/ scopus.csv")
