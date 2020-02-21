#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd 
import numpy as np



#Scopus 
df_scopus = pd.read_csv("input_table/01_scopus.csv", sep=',', encoding='utf-8')
doi_scopus = df_scopus["DOI"]

#Zotero
df_zotero = pd.read_csv("input_table/06_zotero.csv", sep=',', encoding='utf-8')

#Look for DOI to include to database intranet. 
df = pd.read_csv("input_table/00_cr2_articles.csv", sep=',', encoding='utf-8')
doi_input = df["DOI"]

# Input-Output
df_wordpress = pd.read_csv("input_table/wordpress.csv", sep=';',encoding='utf-8')
doi_wordpress = df_wordpress["DOI"]

#Filter by DOI
df_zotero=pd.merge(df,df_zotero, on=["DOI"])
df_scopus= pd.merge(df,df_scopus, on=["DOI"])

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

keywords1 	= df_scopus["Author Keywords"]	
keywords2	= df_scopus["Index Keywords"]

keyword = []
doi=[]
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
print("TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST")
for m in range(0,len(df_zotero)):	
	for n in range(0,len(df_scopus)):	
		keywords=[]
		dois=[]	
		if str(doi_scopus[n]) == doi_zotero[m]:		
			if str(keywords1[n]) == 'nan' and str(keywords2[n]) !='nan':
				for o in range(0,len(keywords2[n].lower().split("; "))):
					keywords.append(keywords2[n].lower().split("; ")[o])
				dois.append(doi_scopus[n])
			elif str(keywords2[n]) == 'nan' and str(keywords1[n]) != 'nan':
				for o in range(0,len(keywords1[n].lower().split("; "))):
					keywords.append(keywords1[n].lower().split("; ")[o])
				dois.append(doi_scopus[n])
			elif str(keywords1[n]) == 'nan' and str(keywords2[n]) == 'nan':
				keywords.append('-')
				dois.append(doi_scopus[n])
			else:
				total = keywords1[n].lower().split('; ')+keywords2[n].lower().split('; ')
				for o in range(0,len(total)):
					keywords.append(total[o])
				dois.append(doi_scopus[n])
			print(keywords)
			print(type(keywords))
			print(unique_list(keywords))
			keyword.append(str(unique_list(keywords)).replace("'","").replace("[","").replace("]",""))
			doi.append(str(dois).replace("'","").replace("[","").replace("]",""))

#print(keyword)
#print(doi)	
df4 = pd.DataFrame(columns=["DOI", "Key Words"])
df4["DOI"]=doi
df4["Key Words"]=keyword


df= pd.DataFrame( columns = ["N","Funding Year", "Línea de Investigación", "Research Lines",
	"Año", "Autores", "Título", "Revista", "Ficha de Publicación","DOI", "ISSN", "Abstract", "Acceso", "Páginas",
	"Volumen", "Index"])

	
#Add columns on new file Intranet
df["N"]					  		= ""
df["Línea de Investigación"]	= line
df["Funding Year"]				= "2020"
df["Research Lines"]			= ""
df["Año"]						= year
df["Autores"]					= authors_zotero
df["Título"]					= title
df["Revista"]					= journal
df["Ficha de Publicación"]		= ""
df["Volume"] 					= ["vol."+(str(v)) for v in volume]
df["Issue"]						= [" is."+(str(i)) for i in issue ]
df["DOI"]						= doi_zotero
df["ISSN"]						= issn
df["Abstract"] 					= abstracts
df["Acceso"]					= url
df["Páginas"]					= pages
df["Volumen"] 					= df["Volume"]+df["Issue"]
df["Index"]						= ""
df["Volumen"]					= [d.replace('nan','') for d in df["Volumen"]]
#print(df)

df2 = pd.merge(df, df4, on="DOI",  how='outer')

#print(df2)

#Create a new dataframe Wordpress
df_wordpress_created = pd.DataFrame(df2, columns = ["N","Funding Year", "Línea de Investigación", "Research Lines",
	"Año", "Autores", "Título", "Revista",  "Ficha de Publicación", "Key Words","DOI", "ISSN", "Abstract", "Acceso", "Páginas",
	"Volumen", "Index"])

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
