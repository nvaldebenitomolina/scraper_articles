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



answer = input("Do you want to import wordpress_modified.csv to wordpress? y/n ")

if answer =='n':
	print('Thank you for answer')
elif answer =='y':
	print('Importing table to wordpress ...')
	#open webdriver
	driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
	print('user: cr2dgf password:wpcr2')
	driver.get("http://cr2.cl/wp-admin")
	

	#user and password
	user=os.environ["USER_WORDPRESS"]
	password=os.environ["PASSWORDWORDPRESS"]

	time.sleep(4)
	#username
	username = driver.find_element_by_xpath('//*[@id="user_login"]')
	username.send_keys(user)

	#password
	userpassword = driver.find_element_by_xpath('//*[@id="user_pass"]')
	userpassword.send_keys(password)

	button = driver.find_element_by_xpath('//*[@id="wp-submit"]')
	button.click()
	driver.maximize_window()
	

	driver.get('http://www.cr2.cl/wp-admin/admin.php?page=tablepress_import')
	time.sleep(4)
	driver.find_element_by_xpath('//*[@id="tables-import-file-upload"]').send_keys(os.getcwd()+'/output_table/wordpress_modified.csv')
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="tables-import-type-replace"]').click()
	driver.find_element_by_xpath('//*[@id="tables-import-existing-table"]/option[7]').click()
	driver.find_element_by_xpath('//*[@id="tablepress_import-import-form"]/div/table/tbody/tr[9]/td[2]/input').click()
	driver.find_element_by_xpath('//*[@id="postbox-container-2"]/p[3]/input[1]').click()
	print('wordpress_modified.csv was uploaded to wordpress')

	driver.get("http://cr2.cl/eng/wp-admin")
	

	#user and password
	user=os.environ["USER_WORDPRESS"]
	password=os.environ["PASSWORDWORDPRESS"]

	time.sleep(4)
	#username
	username = driver.find_element_by_xpath('//*[@id="user_login"]')
	username.send_keys(user)

	#password
	userpassword = driver.find_element_by_xpath('//*[@id="user_pass"]')
	userpassword.send_keys(password)

	button = driver.find_element_by_xpath('//*[@id="wp-submit"]')
	button.click()
	driver.maximize_window()
	

	driver.get('http://www.cr2.cl/eng/wp-admin/admin.php?page=tablepress_import')
	time.sleep(4)
	driver.find_element_by_xpath('//*[@id="tables-import-file-upload"]').send_keys(os.getcwd()+'/output_table/wordpress_modified.csv')
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="tables-import-type-replace"]').click()
	driver.find_element_by_xpath('//*[@id="tables-import-existing-table"]/option[7]').click()
	driver.find_element_by_xpath('//*[@id="tablepress_import-import-form"]/div/table/tbody/tr[9]/td[2]/input').click()
	driver.find_element_by_xpath('//*[@id="postbox-container-2"]/p[3]/input[1]').click()
	print('wordpress_modified.csv was uploaded to wordpress')

else:
	print('This answer is not available (y/n)')