#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd 
import numpy as np



#Scopus 
#df_scopus = pd.read_csv("input_table/01_scopus.csv", sep=',', encoding='utf-8')

df_zotero = pd.read_csv("input_table/06_zotero.csv", sep=',', encoding='utf-8')
#Look for DOI to include to database intranet. 
df = pd.read_csv("input_table/00_cr2_articles.csv", sep=',', encoding='utf-8')
title_input = df["Title"]

# Input-Output
df_intranet = pd.read_csv("input_table/wordpress.csv", sep=';',encoding='utf-8')
#doi_intranet = df_intranet["DOI [f_682:default]"]
df_users = pd.read_csv("input_table/07_users_Investigadores.csv", sep=',', encoding='utf-8')

#Filter by title or chapter title
df_zotero=pd.merge(df,df_zotero, on=["Title"])
#df_scopus= pd.merge(df,df_scopus, on=["Title"])

#Look for columns on Zotero 
item_type 	= df_zotero["Item Type"]
authors_zotero 	= df_zotero["Author"]
year		= df_zotero["Publication Year"]
title		= df_zotero["Title"]
title_book 	= df_zotero["Publication Title"]
isbn 		= df_zotero["ISBN"]
issn 		= df_zotero["ISSN"]
doi_zotero	= df_zotero["DOI"]
url			= df_zotero["Url"]
abstracts	= df_zotero["Abstract Note"]
pages		= df_zotero["Pages"]
npages		= df_zotero["Num Pages"]
volume		= df_zotero["Volume"]
issue		= df_zotero["Issue"]
publisher 	= df_zotero["Publisher"]
place 		= df_zotero["Place"]
language 	= df_zotero["Language"]
file 		= df_zotero["File Attachments"]
line		= df_zotero["Manual Tags"]
editors 	= df_zotero["Editor"]


#OUTPUT



def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
print("TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST")


df= pd.DataFrame( columns = ["N","Funding Year","Línea de Investigación","Research Lines","Año","Autores","Libro","Título Capítulo","Ficha de Publicación",
"ISSN","DOI","Abstract","Acceso","Páginas","Editores","Editorial","Ciudad/País","Idioma"])

df["N"] 		= ""
df["Línea de Investigación"] = line
df["Funding Year"] = '2020'
df["Research Lines"] = ""
df["Año"] 		= year
df["Autores"]	= authors_zotero
df["Libro"]		= title_book
df["Título Capítulo"] 		= title
df["Ficha de Publicación"]	= ""
df["ISSN"]		= issn
df["DOI"]		= doi_zotero
df["Abstract"]	= abstracts
df["Acceso"]	= url
df["Páginas"]	= pages
df["Editores"]	= editors
df["Editorial"]	= publisher
df["Ciudad/País"]	= place
df["Idioma"]	= language
	


#print(df2)

#Create a new dataframe Wordpress
df_wordpress_created = pd.DataFrame(df, columns = ["N","Funding Year","Línea de Investigación","Research Lines","Año","Autores","Libro","Título Capítulo","Ficha de Publicación",
"ISSN","DOI","Abstract","Acceso","Páginas","Editores","Editorial","Ciudad/País","Idioma"])

#Save dataframe in a new csv file
df_wordpress_created.to_csv(str("output_table/wordpress.csv"), sep=';', encoding='utf-8')

#Open and read dataframes, table wordpress original on web and table wordpress created
df_wordpress = pd.read_csv("input_table/wordpress.csv", sep=';',encoding='utf-8')
df_wordpress_created = pd.read_csv("output_table/wordpress.csv", sep=';',encoding='utf-8')

#print(df_wordpress)
#print(df_wordpress_created)
frames =[df_wordpress,df_wordpress_created]
result =pd.concat(frames,sort=False)
#print(result)

result=result.drop('Unnamed: 0', 1)

#print(result)
#Dataframes concatenated in a new file modified
result.to_csv(str("output_table/wordpress_modified.csv"), sep=';', encoding='utf-8', index=False)
