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


print('Exporting table from wordpress ...')
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
time.sleep(4)
driver.get('http://www.cr2.cl/wp-admin/admin.php?page=tablepress_export')
driver.find_element_by_xpath('//*[@id="tables-export"]/option[6]').click()

driver.find_element_by_xpath('//*[@id="postbox-container-2"]/p[3]/input').click()
print('Table wordpress downloaded ')