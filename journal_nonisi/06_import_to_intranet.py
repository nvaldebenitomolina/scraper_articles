#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import re
import operator
import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains



answer = input("Do you want to import tracker_36_modified.csv to intranet? y/n ")

if answer =='n':
	print('Thank you for answer')
elif answer =='y':
	print('Importing table to intranet ...')
	#open webdriver
	driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
	driver.get("http://intranet.cr2.cl")

	#user and password
	user=os.environ["USER_INTRANET"]
	password=os.environ["PASSWORDINTRANET"]
	time.sleep(3)
	#username
	username = driver.find_element_by_xpath('//*[@id="login-user_1"]')
	username.send_keys(user)

	#password
	userpassword = driver.find_element_by_xpath('//*[@id="login-pass_1"]')
	userpassword.send_keys(password)

	button = driver.find_element_by_xpath('//*[@id="loginbox-1"]/fieldset/div[4]/button')
	button.click()
	driver.get("http://intranet.cr2.cl/tiki-tabular-list?tabularId=11");
	driver.maximize_window()

	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="col1"]/div[3]/div/a[3]').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="inputFile"]').send_keys(os.getcwd()+'/output_table/tracker_36_modified.csv')

	driver.find_element_by_xpath('//*[@id="bootstrap-modal"]/div/div/div[3]/button[2]').click()
	print('tracker_36_modified.csv was uploaded to intranet')

else:
	print('This answer is not available (y/n)')