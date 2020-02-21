#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd 
import numpy as np



#Scopus 
df_scopus = pd.read_csv("input_table/01_scopus.csv", sep=',', encoding='utf-8')
df_zotero = pd.read_csv("input_table/06_zotero.csv", sep=',', encoding='utf-8')

#df_zotero =pd.concat(frames,sort=False)
#Look for DOI to include to database intranet. 
df = pd.read_csv("input_table/00_cr2_articles.csv", sep=',', encoding='utf-8')
doi_input = df["DOI"]
print(len(doi_input))

#Filter by DOI
df_zotero=pd.merge(df,df_zotero, on=["DOI"])
#df_scopus= pd.merge(df,df_scopus, on=["DOI"])

#Look for columns on Zotero 
journal 	= df_zotero["Publication Title"]
doi_zotero	= df_zotero["DOI"]
url			= df_zotero["Url"]
issn 		= df_zotero["ISSN"]
line		= df_zotero["Manual Tags"]
title		= df_zotero["Title"]
year		= df_zotero["Publication Year"]
volume		= df_zotero["Volume"]
issue		= df_zotero["Issue"]
pages		= df_zotero["Pages"]
abstracts	= df_zotero["Abstract Note"]
authors_zotero 	= df_zotero["Author"]

df = pd.DataFrame( columns = [])

progress_report				= df['Progress report']
doi 						= df['DOI']
article_title				= df['Article Title_y']
journal_name				= df['Journal Name']
year_published				= df['Year Published']
name_of_reasearch_line 		= df['Name of Research Line']
file 						= df['File Attachments']
links						= df['Url']
authors 					= df['Authors']
cr2_authors					= df['CR2 Authors']
volume 						= df['VL']
first_page					= df['BP']
last_page 					= df['EP']
indexed_not_indexed			= 'ISI - Indexed'
regional 					= df['REGIONAL']
fondecyt 					= df['FONDECYT']
fondef 						= df['FONDEF']
pia 						= df['PIA']
fondap 						= df['FONDAP']
pai 						= df['PAI']
explora 					= df['EXPLORA']
international 				= df['International Cooperation']
astronomia 					= df['Astronomia']
becas 						= df['Becas (PCHA)']
icm							= df['ICM']
basal 						= df['BASAL']
other_funding 				= df['OTHER (specify)']
other_funding_obs 			= df['SPECIFY']


def change_line_name(line):
	if line == "Dimensión Humana":
		return 'Human Dimensions'
	elif line == "Servicios Ecosistémicos":
		return 'Ecosystem Services'
	elif line == "Modelación y Sistemas de Observación":
		return	 "Modeling and Observing Systems"
	elif line == "Biogeoquímica":
		return "Biogeochemistry"
	elif line == "Dinámica del Clima":
		return "Climate Dynamics"
	elif line == "Agua y Extremos":
		return "Water availability and extremes"
	elif line == "Gobernanza e Interfaz entre Ciencia y Política":
		return "Governance and policy-science interface"
	elif line == "Cambio de Uso de Suelo":
		return "Land use change"
	elif line == "Ciudades Resilientes":
		return "Cities in a changing climate"
	elif line == "Zonas Costeras":
		return "Coastal zones"
