#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Importing libraries
import pandas as pd 
import numpy as np

#Zotero 
df_zotero = pd.read_csv("input_table/06_zotero.csv", sep=',', encoding='utf-8')

#Look for DOI  for including to cr2articles database. 
df = pd.read_csv("input_table/00_cr2_articles.csv", sep=',', encoding='utf-8' )
title_input = df["Title"]
#print(len(df))

# Input-Output 
df_master = pd.read_csv("input_table/cr2_articles.csv", sep=',',encoding='utf-8')


#Filter by DOI
df_zotero=pd.merge(df,df_zotero, on=["Title"])

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

#Create a new dataframe



df= pd.DataFrame(columns = ["N","Funding Year","Progress report","Name of Research Line","Research Lines","Publication Year",
"Authors original","CR2 Authors","Author","Chapter	Book","Title","ISBN","ISSN","DOI","Url","Abstract Note","Pages","First page",
"Last page","Num Pages","Issue","Volume","Publisher","Place","Language","Editor Clean","File"])

#Add columns on new file cr2_articles
df["N"] 			= ""
df["Name of Research Line"]	= line
df["Funding Year"] 	= "2020"
df["Progress report"] 		= "8" 
df["Research Lines"]= ""
df["Publication Year"]		= year
df["Authors original"]		= authors_zotero
df["Author"]		= authors_zotero
df["Chapter"]		= title
df["Book Title"]	= title_book
df["ISBN"] 			= isbn
df["ISSN"] 			= issn
df["DOI"] 			= doi_zotero
df["Url"]			= url
df["Abstract Note"] = abstracts
df["Pages"]			= pages
df["First page"]	= pages
df["Last page"] 	= pages
df["Num Pages"] 	= npages
df["Issue"] 		= issue
df["Volume"] 		= volume
df["Publisher"] 	= publisher
df["Place"] 		= place
df["Language"] 		= language
df["Editor Clean"] 	= editors
df["File"] 			= file


users_all=[]
for n in range(0,len(authors_zotero)):
	users=[]
	if 'Gonzalez, A.' in authors_zotero[n] or 'Gonzalez-Reyes, A' in authors_zotero[n] or 'González-Reyes, Álvaro' in authors_zotero[n] or 'Gonzalez-Reyes, Alvaro' in authors_zotero[n] or ' González-Reyes, A.' in authors_zotero[n] or 'Gonzalez-Reyes, Á.' in authors_zotero[n]:
		users.append('Alvaro González')
	if 'Lara, A' in  authors_zotero[n] or 'Lara, Antonio' in  authors_zotero[n] or 'LARA, A' in authors_zotero[n]:
		users.append('Antonio Lara Aguilar')
	if 'Maillet, A' in  authors_zotero[n] or 'Maillet, Antoine' in  authors_zotero[n]:
		users.append('Antoine Maillet')
	if 'Miranda, A' in  authors_zotero[n] or 'Miranda, Alejandro' in  authors_zotero[n]:
		users.append('Alejandro Miranda')
	if 'Muñoz, A' in  authors_zotero[n] or 'Munoz, Ariel A' in  authors_zotero[n] or 'Munoz, AA' in  authors_zotero[n] or 'Munoz, A' in  authors_zotero[n] or 'Munoz, Ariel' in  authors_zotero[n]:
		users.append('Ariel Andrés Muñoz Navarro')		
	if 'Osses, A' in  authors_zotero[n]:
		users.append('Axel Esteban Osses Alvarado')	
	if 'Sepulveda, A' in  authors_zotero[n] or 'Sepulveda-Jauregui, A' in  authors_zotero[n]:
		users.append('Armando Sepúlveda Jáuregui')
	if 'Urquiza, A' in  authors_zotero[n]:
		users.append('Anahi Veronica Urquiza Gómez')	
	if 'Diez, B' in  authors_zotero[n] or 'Díez, Beatriz' in  authors_zotero[n] or 'Diez, B' in  authors_zotero[n] or 'Díez, B' in authors_zotero[n]:
		users.append('Beatriz Eugenia Diez Moreno')
	if 'Aguirre, C' in  authors_zotero[n]:
		users.append('Maria Catalina Aguirre Galaz')
	if 'Alvarez-Garreton, C' in authors_zotero[n]:
		users.append('Camila Alvarez')
	if 'Ibarra, C' in  authors_zotero[n]:
		users.append('Cecilia Ibarra Patricia Mendoza')
	if 'Little, C' in  authors_zotero[n]:
		users.append('CHRISTIAN LEONARDO LITTLE CARDENAS')	
	if 'Christina Ridley' in  authors_zotero[n]:
		users.append('Christina Ridley')
	if 'Tejo, C' in authors_zotero[n] or 'Tejo, CF' in authors_zotero[n] or 'Tejo, Camila' in authors_zotero[n]:
		users.append('Camila Francisca Tejo Haristoy')
	if 'Zamorano, C' in  authors_zotero[n] or 'Zamorano-Elgueta, C' in authors_zotero[n]:
		users.append('Carlos Patricio Zamorano Elgueta')
	if 'Bozkurt, D' in  authors_zotero[n] or 'Bozkurt, Deniz' in  authors_zotero[n]:
		users.append('Deniz Bozkurt')
	if 'Christie, D' in  authors_zotero[n] or 'Christie, DA' in  authors_zotero[n]:
		users.append('Duncan Andrés Christie Browne')
	if 'Herve, D' in  authors_zotero[n] or 'Hervé, D' in  authors_zotero[n]:
		users.append('Dominique Marie Hervé Espejo')
	if 'Aliste, E' in  authors_zotero[n] or 'Aliste, Enrique' in  authors_zotero[n]:
		users.append('Enrique Patricio Aliste Almuna')
	if 'Gayo, E' in  authors_zotero[n]:
		users.append('Eugenia Monserrat Gayo Hernandez')
	if 'Lambert, F' in  authors_zotero[n]:
		users.append('Fabrice - Lambert')
	if 'Vasquez, F' in  authors_zotero[n] or 'Vasquez, Felipe' in  authors_zotero[n] or 'Vasquez, FV' in  authors_zotero[n] or 'Vasquez-Lavin, F' in authors_zotero[n] or 'Lavin, FAV' in authors_zotero[n] or 'Lavin, FV' in authors_zotero[n]:
		users.append('Felipe Antonio Vásquez Lavín')			
	if 'Blanco, G' in  authors_zotero[n] or 'Blanco Wells, G' in  authors_zotero[n] or 'Blanco-Wells, G' in authors_zotero[n] or 'Wells, GB' in authors_zotero[n]:
		users.append('Gustavo Emilio Blanco Wells')	
	if 'Zambrano, M' in  authors_zotero[n] or 'Zambrano-Bigiarini, M' in  authors_zotero[n] or 'Zambrano‐Bigiarini, Mauricio' in authors_zotero[n]:
		users.append('Mauricio Zambrano-Bigiarini')		
	if 'Masotti, I' in  authors_zotero[n]:
		users.append('Italo Masotti Muzzio')
	if 'Boisier, J' in  authors_zotero[n]:
		users.append('Juan Pablo Boisier')
	if 'Hoyos, J' in  authors_zotero[n] or 'Hoyos-Santillan, Jorge' in  authors_zotero[n] or 'Hoyos-Santillan, J' in  authors_zotero[n]:
		users.append('Jorge Hoyos')
	if 'Labraña, J' in authors_zotero[n]:
		users.append('Julio Labraña')
	if 'Cordero, L' in  authors_zotero[n]:
		users.append('Luis Alberto Cordero Vega')
	if 'Farías, L' in  authors_zotero[n] or 'Farias, L' in  authors_zotero[n] or 'Ferias, L' in  authors_zotero[n]:
		users.append('Laura Farias')
	if 'Gallardo, L' in  authors_zotero[n] or 'Klenner, LG' in authors_zotero[n]:
		users.append('Laura Gallardo Klenner')
	if 'Alcamán, M.E.' in authors_zotero[n] or 'Alcaman-Arias, ME' in authors_zotero[n] or 'Alcaman, ME' in authors_zotero[n] or ' Alcamán-Arias, M. E.' in authors_zotero[n]:
		users.append('María Estrella Alcamán')
	if 'Galleguillos, M' in  authors_zotero[n]:
		users.append('Mauricio Humberto Galleguillos Torres')
	if 'Gonzalez, M' in  authors_zotero[n] or 'GONZALEZ, M' in authors_zotero[n]:
		users.append('Mauro Esteban González Cangas')
	if 'Jacques, M' in  authors_zotero[n] or 'Jacques‐Coper, Martín' in  authors_zotero[n] or 'Jacques-Coper, M' in authors_zotero[n]:
		users.append('Martin Sebastian Jacques Coper')
	if 'Mena, M' in  authors_zotero[n] or 'Mena, Marcelo' in  authors_zotero[n] or 'Mena-Carrasco, M' in authors_zotero[n]:
		users.append('Marcelo Mena')
	if 'Munizaga, M' in  authors_zotero[n]:
		users.append('Marcela Adriana Munizaga Muñoz')
	if 'Osses, M' in  authors_zotero[n]:
		users.append('Mauricio Osses Alvarado')
	if 'Rojas, M' in  authors_zotero[n]:
		users.append('Heloisa Rojas Corradi')
	if 'Hitschfeld, N' in  authors_zotero[n] or  'Hitschfeld-Kahler, N' in authors_zotero[n] or 'HITSCHFELD, N' in authors_zotero[n] or 'Hitschfeld‐Kahler, N' in authors_zotero[n]:
		users.append('Nancy Viola Hitschfeld Kahler')
	if 'Huneeus, N' in  authors_zotero[n]:
		users.append('Nicolas Jorge Huneeus Lagos')
	if 'Aldunce, P' in  authors_zotero[n]:
		users.append('Paulina Aldunce')
	if 'Moraga, P' in  authors_zotero[n] or 'Sariego, PM' in authors_zotero[n]:
		users.append('Pilar Moraga Sariego')
	if 'Moreno, P' in  authors_zotero[n] or 'MORENO, PI' in authors_zotero[n]:
		users.append('Patricio Iván Moreno Moncada')
	if 'Smith, P' in  authors_zotero[n]:
		users.append('Pamela Smith Guerra')
	if 'Arriagada, R' in  authors_zotero[n]:
		users.append('Rodrigo Antonio Arriagada Cisternas')
	if 'Borquez, R' in authors_zotero[n]:
		users.append('Roxana Borquez')
	if 'De Polz-Holz, R' in  authors_zotero[n] or 'de Polz-Holz, R' in  authors_zotero[n] or 'De Pol-Holz, R' in  authors_zotero[n] or 'de Pol-Holz, R' in authors_zotero[n] or 'De Pot-Holz, R' in authors_zotero[n] or 'Holz, RD' in authors_zotero[n] or 'DePol-Holz, R' in authors_zotero[n] or 'ORyan, RE' in authors_zotero[n]:
		users.append('Ricardo De Pol Holz')
	if 'Garreaud, R' in  authors_zotero[n] or 'GARREAUD, R' in authors_zotero[n]:
		users.append('Rene Garreaud Salazar')
	if 'O´Ryan, R'  in  authors_zotero[n] or "O’Ryan, Raúl" in authors_zotero[n] or "O'Ryan, R" in  authors_zotero[n] or 'O"Ryan, R' in authors_zotero[n] or "O''Ryan, R" in authors_zotero[n] or "O''Ryan, R" in authors_zotero[n]:
		users.append("Raúl O Ryan Gallardo")
	if 'Pozo, RA' in authors_zotero[n]:
		users.append('Rocio Pozo')
	if 'Rondanelli, R' in  authors_zotero[n]:
		users.append('Roberto F Rondanelli Rondanelli')
	if 'Sapiains, R' in  authors_zotero[n] or 'Sapiains A.' in authors_zotero[n]:
		users.append('Rodolfo sapiains')
	if 'Seguel, R' in  authors_zotero[n]:
		users.append('Rodrigo José Seguel Albornoz')
	if 'Valenzuela, R' in authors_zotero[n] or 'Valenzuela, RA' in authors_zotero[n]:
		users.append('Raúl Valenzuela')
	if 'Urrutia, R' in  authors_zotero[n] or 'Urrutia-Jalabert, R' in  authors_zotero[n]:
		users.append('Rocio Beatriz Urrutia Jalabert')
	if 'Crespo, S' in authors_zotero[n]:
		users.append('Sebastian Crespo')
	if 'Gomez, S' in  authors_zotero[n] or 'Gómez, S' in  authors_zotero[n] or 'Gomez-Gonzalez, S' in authors_zotero[n] or 'Gómez‐González, Susana' in authors_zotero[n]:
		users.append('Susana Gómez González')
	if 'Tolvett, S' in authors_zotero[n]:
		users.append('Sebastian Andrés Tolvett Caro')
	if 'Delgado, V' in  authors_zotero[n]:
		users.append('Verónica Pía Delgado Schneider')
	if 'Fleming, Z' in  authors_zotero[n]:
		users.append('Zoe Louise Fleming')
	#if 'Mazzeo, A' in  authors_zotero[n] or 'Mazzeo, Andrea' in  authors_zotero[n]:
	#	users.append('Mazzeo, A.')
	#if 'Barraza, F' in authors_zotero[n]:
	#	users.append('Barraza, F')
	#if 'Barichivich, J' in authors_zotero[n]:
	#	users.append('Barichivich, J.')
	#if 'Veliz, K' in authors_zotero[n]:
	#	users.append('Veliz, K.')
	#if 'Belmar, L' in authors_zotero[n]:
	#	users.append('Belmar, L.')
	#if 'Nahuelhual, L' in authors_zotero[n]:
	#	users.append('Nahuelhual, L')
	#if 'Yevenes, M' in authors_zotero[n] or 'Yevenes, Mariela A.' in authors_zotero[n] or 'Yevenes, MA.' in authors_zotero[n]:
	#	users.append('Yevenes, M.')	
	#if 'Lemaire, V' in authors_zotero[n]:
	#	users.append('Lemaire, V.')
	#if 'Villaseñor, T' in authors_zotero[n] or 'Villasenor, T' in authors_zotero[n]:
	#	users.append('Villaseñor, T.')
	if 'Bustos-Salazar, A' in authors_zotero[n]:
		users.append('Angela Bustos Salazar')
	if 'Ugarte, Ana M' in authors_zotero[n]: #estudiante
		users.append('Ana Maria Ugarte')	
	if 'Amigo, C' in authors_zotero[n]: #estudiante
		users.append('Catalina Amigo')
	if 'Billi, M' in authors_zotero[n]:
		users.append('Marco Billi')
	if 'Troncoso, M' in authors_zotero[n]:
		users.append('Macarena Troncoso')
	if 'Aparicio-Rizzo, P' in authors_zotero[n]: #estudiante
		users.append('Pilar Aparicio')
	if 'Calvo, R' in authors_zotero[n]:
		users.append('Rubén Calvo')
	if 'Ruiz Pereira, Sebastian Felipe' in authors_zotero[n]: #estudiante
		users.append('Sebastian Ruiz')
	if 'Del Hoyo, M' in authors_zotero[n]: #estudiante
		users.append('Mirko del Hoyo')
	if 'Rudloff, V' in authors_zotero[n]:
		users.append('Valeria Rudloff')
	users_all.append(str(users).replace("'","").replace("[","").replace("]",""))

print(len(title))
print(len(users_all))

df["CR2 Authors"]				= users_all


#Create a new dataframe


df.to_csv(str("output_table/cr2_articles.csv"), sep=';', encoding='utf-8')

df_master = pd.read_csv("input_table/cr2_articles.csv", sep=',',encoding='utf-8')
df_master_created = pd.read_csv("output_table/cr2_articles.csv", sep=';',encoding='utf-8')

print(df_master)
print(df_master_created)
frames =[df_master,df_master_created]
result =pd.concat(frames,sort=False)
print(result)

result=result.drop('Unnamed: 0', 1)

print(result)
result.to_csv(str("output_table/cr2_articles_modified.csv"), sep=';', encoding='utf-8', index=False)


