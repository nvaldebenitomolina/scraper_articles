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
df = pd.read_csv("input_table/00_cr2_articles.csv", sep=',', encoding='utf-8', error_bad_lines=False)
df.dropna()
DOI = df["DOI"]

#JOURNAL PROBLEMS#
#Is climate change framed as 'business as usual' or as a challenging issue? The practitioners' dilemma 
#10.1177/0263774X15614734
#Stakeholder participation in building resilience to disasters in a changing climate
#10.1080/17477891.2015.1134427
def delete_doi(doi_df,doi):
	for n in range(0,len(doi_df)):
		if doi_df[n] == doi:
			print(n)
			print(doi_df[n])
			doi_df= doi_df.drop(doi_df.index[n])

			

	doi_df.reset_index(drop=True)
	doi_df.index = pd.RangeIndex(len(doi_df.index))
	return doi_df

DOI=delete_doi(DOI,'10.1177/0263774X15614734')
DOI=delete_doi(DOI,'10.1080/17477891.2015.1134427')

#DOI.reset_index(drop=True)

#DOI.index = pd.RangeIndex(len(DOI.index))
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
user_webofs=os.environ["EMAIL"]
password_webofs=os.environ["PASSWORDWOS"]




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

#enter = driver.find_element_by_class_name('select2-selection__arrow')
#enter.click()

#save in other files format 
# enter = driver.find_elements_by_xpath('//div[contains(@style,"display:inline-block")]')
# enter = driver.find_elements_by_xpath('//span[contains(@class,"saveToButton")]')
# enter = driver.find_element_by_xpath('//select[contains(@aria-label,"Opciones de formato para guardar resultados")]')
# enter = driver.find_element_by_xpath('//option[contains(@title,"Guardar en otros formatos de archivo")]')
# enter.click()
#save or export files in csv format
enter = driver.find_element_by_xpath('//div[contains(@class,"selectedExportOption")]')
enter = driver.find_element_by_xpath('//button[contains(@id,"exportTypeName")]')
enter.click()
enter = driver.find_element_by_xpath('//span[contains(@class,"saveToButton")]')
enter = driver.find_element_by_xpath('//ul[contains(@class,"saveToMenu quickOutputSubnav subnav autoclose") and contains(@name,"saveToMenu")]')
#enter = driver.find_element_by_xpath('//li[contains(@class,"subnav-item")and contains(@onclick,"trackSnowplowEventSE("save-to-other-file-formats-click");")]')
enter = driver.find_element_by_xpath('//a[contains(@title, "Exportar los registros seleccionados a un archivo delimitado por tabulador, otro software de referencia, etc.")]')
enter.click()


#Click on the input type radio, where we're selecting all.
enter = driver.find_elements_by_xpath('//div[contains(@class, "quick-output-section-content")]')
enter = driver.find_elements_by_xpath('//div[contains(@id, "records-range-radio-button")]')
enter = driver.find_element_by_xpath('//input[contains(@type, "radio") and contains(@id,"numberOfRecordsRange") and contains(@onchange,"enableExportButton()")]')
enter.click()


#from number
enter = driver.find_element_by_id('markFrom')
#enter.send_keys(1)

#to number
enter = driver.find_element_by_id('markTo')
#enter.send_keys(number)

#option for register content
enter = driver.find_elements_by_xpath('//span[contains(@class, "select2") and contains(@class, "select2-container") and contains(@class, "select2-container--default") and contains(@class,"select2-container--focus")]')
enter = driver.find_elements_by_xpath('//span[contains(@class,"select2-selection") and contains(@class,"select2-selection--single")]')
enter = driver.find_element_by_xpath('//option[contains(@value,"HIGHLY_CITED HOT_PAPER OPEN_ACCESS PMID USAGEIND AUTHORSIDENTIFIERS ACCESSION_NUM FUNDING SUBJECT_CATEGORY JCR_CATEGORY LANG IDS PAGEC SABBR CITREFC ISSN PUBINFO KEYWORDS CITTIMES ADDRS CONFERENCE_SPONSORS DOCTYPE CITREF ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  ")]')
enter.click()

#option format file
enter = driver.find_elements_by_xpath('//span[contains(@class, "select2") and contains(@class, "select2-container") and contains(@class, "select2-container--default") and contains(@class,"select2-container--below") and contains(@class,"select2-container--focus") and contains(@class,"select2-container--open")]')
enter = driver.find_elements_by_xpath('//span[contains(@class,"select2-selection") and contains(@class,"select2-selection--single")]')
enter = driver.find_elements_by_xpath('//span[contains(@class,"select2-results__option select2-results__option--highlighted")]')
enter = driver.find_element_by_xpath('//option[contains(@value,"tabWinUTF8")]')
enter.click()

#download csv affiliations
enter = driver.find_element_by_xpath('//div[contains(@class,"quickoutput-overlay-buttonset")]')
enter = driver.find_element_by_xpath('//span[contains(@class,"quickoutput-action")]')
enter = driver.find_element_by_xpath('//button[contains(@class,"onload-primary-button") and contains(@id,"exportButton") and contains(@alt,"Enviar")]')
enter.click()

# delay =500 # seconds

# #close
# close = driver.find_elements_by_xpath('//div[contains(@class,"ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-dialog-quickoutput qoOther")]')
# close = driver.find_elements_by_xpath('//div[contains(@id,"ui-id-9") and contains(@class,"ui-dialog-content ui-widget-content")]')
# close = driver.find_elements_by_xpath('//form[contains(@class,"quick-output-form")]')
# close = driver.find_elements_by_xpath('//div[contains(@class,"quickoutput-overlay-buttonset")]')
# close = driver.find_element_by_xpath('//a[contains(@class,"quickoutput-cancel-action") and contains(@href,"#")]')
# close.click()

# print("Download availaible /home/nvaldebenito/Descargas/ savedrecs.txt")


# #id="view_citation_report_image_placeholder"
# #cites
# enter = driver.find_elements_by_xpath('//div[contains(@class,"l-content")]')
# enter = driver.find_elements_by_xpath('//div[contains(@class,"page-options-inner")]')
# enter = driver.find_elements_by_xpath('//div[contains(@class,"create-cite-report")]')
# enter = driver.find_element_by_id('view_citation_report_image_placeholder')
# enter = driver.find_elements_by_xpath('//div[contains(@class,"display:inline-block;whitespace:no-wrap;")]')
# enter = driver.find_element_by_xpath('//a[contains(@alt,"Ver informe de citas") and contains(@title,"Ver informe de citas") and contains(@class,"snowplow-citation-report citation-report-summary-link")]')
# enter.click()

# #save
# enter = driver.find_elements_by_xpath('//div[contains(@class,"l-content")]')
# enter = driver.find_elements_by_xpath('//div[contains(@class,"select-container")]')
# enter = driver.find_elements_by_xpath('//span[contains(@class,"cr_saveToButton")]')
# enter = driver.find_elements_by_xpath('//select[contains(@class,"saveToMenuBottom cr_saveToMenu select2-hidden-accessible")]')
# enter = driver.find_element_by_xpath('//option[contains(@selected,"selected") and contains(@value,"xls")]')
# enter.click()

# #from number
# enter = driver.find_element_by_id('markFrom')
# enter.send_keys(1)

# #to number
# enter = driver.find_element_by_id('markTo')
# enter.send_keys(number)


# #download csv citations
# enter = driver.find_element_by_xpath('//div[contains(@class,"quickoutput-overlay-buttonset")]')
# enter = driver.find_element_by_xpath('//span[contains(@class,"quickoutput-action")]')
# enter = driver.find_element_by_xpath('//button[contains(@class,"standard-button") and contains(@class,primary-button) and contains(@title,"Enviar")]')
# enter.click()

# #close
# #close = driver.find_elements_by_xpath('//div[contains(@class,"ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-dialog-quickoutput")]')
# #close = driver.find_element_by_id('ui-id-6')
# #close = driver.find_elements_by_xpath('//form[contains(@class,"quick-output-form")]')
# #close = driver.find_elements_by_xpath('//div[contains(@class,"quickoutput-overlay-buttonset")]')
# #close = driver.find_element_by_xpath('//a[contains(@class,"quickoutput-cancel-action") and contains(@href,"#")]')
# #close.click()

# print("Download availaible /home/nvaldebenito/Descargas/ savedrecs.xls")


