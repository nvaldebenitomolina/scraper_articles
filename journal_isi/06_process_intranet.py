#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd 
import numpy as np



#Scopus 
df_scopus = pd.read_csv("input_table/01_scopus.csv", sep=',', encoding='utf-8')
df_zotero = pd.read_csv("input_table/06_zotero.csv", sep=',', encoding='utf-8')

#Look for DOI to include to database intranet. 
df = pd.read_csv("input_table/00_cr2_articles.csv", sep=',', encoding='utf-8')
doi_input = df["DOI"]
print(len(doi_input))

# Input-Output
df_intranet = pd.read_csv("input_table/tracker_38.csv", sep=',',encoding='utf-8')
doi_intranet = df_intranet["DOI [f_746:default]"]
df_users = pd.read_csv("input_table/07_users_Investigadores.csv", sep=',', encoding='utf-8')

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

df = pd.DataFrame( columns = ["Item ID [*itemId:id]","Status [status:system]","Usuario [f_739:username]", "Reconocimiento o Afiliacion (CR)2 [f_751:code]", "Estado [f_741:code]",
	 "Título [f_742:default]", "Autores [f_743:default]", "Lineas Involucradas [f_745:code]", "DOI [f_746:default]" ,"Código ISSN / ISBN [f_747:default]",
	  "Nombre Journal [f_748:default]","Ubicación en Línea [f_749:default]","Año de Publicación [f_750:default]", "PARTICIPACION [f_753:code]",
	  "% aportado por REGIONAL [publicacionesjournalIsiApo_rREGIONAL:default]",
	  "% aportado por FONDECYT [f_756:default]",
	  "% aportado por FONDEF [f_757:default]",
	  "% aportado por PIA [publicacionesjournalIsiApo_adoPorPIA:default]",
	  "% aportado por FONDAP [f_755:default]",
	  "% aportado por PAI [publicacionesjournalIsiApo_adoPorPAI:default]",
	  "% aportado por EXPLORA [publicacionesjournalIsiApo_orEXPLORA:default]",
	  "% aportado por colaboración Internacional [publicacionesjournalIsiApo_rnacional:default]",
	  "% aportado por Astronomia [publicacionesjournalIsiApo_stronomia:default]",
	  "% aportado por Becas (PCHA) [publicacionesjournalIsiApo_BecasPCHA:default]",
	  "% aportado por Otro (indicar) [f_760:default]",
	  "Adjunta la Publicación [f_763:default]",
	  "Abstract", "Revisión INTERNA [f_738:code]","Periodo [f_752:code]","Líneas Involucradas antiguas [f_744:code]"])
#Add columns on new file Intranet
df["Item ID [*itemId:id]"]					= ""
df["Status [status:system]"]					= ""

df["Título [f_742:default]"]				= title
df["Autores [f_743:default]"]			= authors_zotero
df["Código ISSN / ISBN [f_747:default]"]	= issn
df["DOI [f_746:default]"]				= doi_zotero
df["Lineas Involucradas [f_745:code]"]= line
df["Nombre Journal [f_748:default]"]		= journal
df["Ubicación en Línea [f_749:default]"]	= url
df["Año de Publicación [f_750:default]"]	= year
df["PARTICIPACION [f_753:code]"]		= ""
df["Reconocimiento o Afiliacion (CR)2 [f_751:code]"] = "SI"
df["Estado [f_741:code]"]				= "Publicadas"
df["% aportado por REGIONAL [publicacionesjournalIsiApo_rREGIONAL:default]"] = "A COMPLETAR"
df["% aportado por FONDECYT [f_756:default]"] = "A COMPLETAR"
df["% aportado por FONDEF [f_757:default]"] = "A COMPLETAR"
df["% aportado por PIA [publicacionesjournalIsiApo_adoPorPIA:default]"] = "A COMPLETAR"
df["% aportado por FONDAP [f_755:default]"] = "A COMPLETAR"
df["% aportado por PAI [publicacionesjournalIsiApo_adoPorPAI:default]"] = "A COMPLETAR"
df["% aportado por EXPLORA [publicacionesjournalIsiApo_orEXPLORA:default]"] = "A COMPLETAR"
df["% aportado por colaboración Internacional [publicacionesjournalIsiApo_rnacional:default]"] = "A COMPLETAR"
df["% aportado por Astronomia [publicacionesjournalIsiApo_stronomia:default]"] = "A COMPLETAR"
df["% aportado por Becas (PCHA) [publicacionesjournalIsiApo_BecasPCHA:default]"] = "A COMPLETAR"
df["% aportado por Otro (indicar) [f_760:default]"] = "A COMPLETAR"
df["Adjunta la Publicación [f_763:default]"] = ""
df["Abstract"] = abstracts
df["Revisión INTERNA [f_738:code]"] = "en zotero"
df["Periodo [f_752:code]"] = "A REPORTAR 2020"
df["Líneas Involucradas antiguas [f_744:code]"] = ""

#Process like replace lines
df["Lineas Involucradas [f_745:code]"]=[str(d).replace('Ciudades Resilientes',':Cities') for d in df["Lineas Involucradas [f_745:code]"]]
df["Lineas Involucradas [f_745:code]"]=[d.replace('Cambio de Uso de Suelo',':Land Use Change') for d in df["Lineas Involucradas [f_745:code]"]]
df["Lineas Involucradas [f_745:code]"]=[d.replace('Zonas Costeras',':Coastal Zones') for d in df["Lineas Involucradas [f_745:code]"]]
df["Lineas Involucradas [f_745:code]"]=[d.replace('Agua y Extremos',':Water extremes') for d in df["Lineas Involucradas [f_745:code]"]]
df["Lineas Involucradas [f_745:code]"]=[str(d).replace('Gobernanza e Interfaz Ciencia y Política',':Governance') for d in df["Lineas Involucradas [f_745:code]"]]
df["Lineas Involucradas [f_745:code]"]=[d.replace('Transversal',':Transversal') for d in df["Lineas Involucradas [f_745:code]"]]
df["Lineas Involucradas [f_745:code]"]=[d.replace(';',',') for d in df["Lineas Involucradas [f_745:code]"]]


print(authors_zotero)
users_all=[]
for n in range(0,len(authors_zotero)):
	users=[]
	if 'Gonzalez, A.' in authors_zotero[n] or 'Gonzalez-Reyes, A' in authors_zotero[n] or 'González-Reyes, Álvaro' in authors_zotero[n] or 'Gonzalez-Reyes, Alvaro' in authors_zotero[n]:
		users.append('agonzalezr')
	if 'Lara, A' in  authors_zotero[n] or 'Lara, Antonio' in  authors_zotero[n] or 'LARA, A' in authors_zotero[n]:
		users.append('alara')
	if 'Maillet, A' in  authors_zotero[n] or 'Maillet, Antoine' in  authors_zotero[n]:
		users.append('amaillet')
	if 'Mazzeo, A' in  authors_zotero[n] or 'Mazzeo, Andrea' in  authors_zotero[n]:
		users.append('amazzeo')
	if 'Miranda, A' in  authors_zotero[n] or 'Miranda, Alejandro' in  authors_zotero[n]:
		users.append('amiranda')
	if 'Muñoz, A' in  authors_zotero[n] or 'Munoz, Ariel A' in  authors_zotero[n] or 'Munoz, AA' in  authors_zotero[n] or 'Munoz, A' in  authors_zotero[n] or 'Munoz, Ariel' in  authors_zotero[n]:
		users.append('amunoz')		
	if 'Osses, A' in  authors_zotero[n]:
		users.append('aosses')	
	if 'Sepulveda, A' in  authors_zotero[n] or 'Sepulveda-Jauregui, A' in  authors_zotero[n]:
		users.append('asepulveda')
	if 'Urquiza, A' in  authors_zotero[n]:
		users.append('aurquiza')	
	if 'Diez, B' in  authors_zotero[n] or 'Díez, Beatriz' in  authors_zotero[n] or 'Diez, B' in  authors_zotero[n] or 'Díez, B' in authors_zotero[n]:
		users.append('bdiez')
	if 'Aguirre, C' in  authors_zotero[n]:
		users.append('caguirre')
	if 'Alvarez-Garreton, C' in authors_zotero[n]:
		users.append('calvarez')
	if 'Ibarra, C' in  authors_zotero[n]:
		users.append('cibarra')
	if 'Little, C' in  authors_zotero[n]:
		users.append('clittle')	
	if 'Ridley, C' in  authors_zotero[n]:
		users.append('cridley')
	if 'Tejo, C' in authors_zotero[n] or 'Tejo, CF' in authors_zotero[n] or 'Tejo, Camila' in authors_zotero[n]:
		users.append('ctejo')
	if 'Zamorano, C' in  authors_zotero[n] or 'Zamorano-Elgueta, C' in authors_zotero[n]:
		users.append('czamorano')
	if 'Bozkurt, D' in  authors_zotero[n] or 'Bozkurt, Deniz' in  authors_zotero[n]:
		users.append('dbozkurt')
	if 'Christie, D' in  authors_zotero[n] or 'Christie, DA' in  authors_zotero[n]:
		users.append('dchristie')
	if 'Herve, D' in  authors_zotero[n] or 'Hervé, D' in  authors_zotero[n]:
		users.append('dherve')
	if 'Aliste, E' in  authors_zotero[n] or 'Aliste, Enrique' in  authors_zotero[n]:
		users.append('ealiste')
	if 'Gayo, E' in  authors_zotero[n]:
		users.append('egayo')
	if 'Barraza, F' in authors_zotero[n]:
		users.append('fbarraza')
	if 'Lambert, F' in  authors_zotero[n]:
		users.append('flambert')
	if 'Vasquez, F' in  authors_zotero[n] or 'Vasquez, Felipe' in  authors_zotero[n] or 'Vasquez, FV' in  authors_zotero[n] or 'Vasquez-Lavin, F' in authors_zotero[n] or 'Lavin, FAV' in authors_zotero[n] or 'Lavin, FV' in authors_zotero[n]:
		users.append('fvasquez')			
	if 'Blanco, G' in  authors_zotero[n] or 'Blanco Wells, G' in  authors_zotero[n] or 'Blanco-Wells, G' in authors_zotero[n] or 'Wells, GB' in authors_zotero[n]:
		users.append('gblanco')	
	if 'Zambrano, M' in  authors_zotero[n] or 'Zambrano-Bigiarini, M' in  authors_zotero[n] or 'Zambrano‐Bigiarini, Mauricio' in authors_zotero[n]:
		users.append('hzambrano')		
	if 'Masotti, I' in  authors_zotero[n]:
		users.append('imasotti')
	if 'Barichivich, J' in authors_zotero[n]:
		users.append('jbarichivich')
	if 'Boisier, J' in  authors_zotero[n]:
		users.append('jboisier')
	if 'Hoyos, J' in  authors_zotero[n] or 'Hoyos-Santillan, Jorge' in  authors_zotero[n] or 'Hoyos-Santillan, J' in  authors_zotero[n]:
		users.append('jhoyos')
	if 'Labraña, J' in authors_zotero[n]:
		users.append('jlabrana')
	if 'Veliz, K' in authors_zotero[n]:
		users.append('kveliz')
	if 'Belmar, L' in authors_zotero[n]:
		users.append('lbelmar')
	if 'Cordero, L' in  authors_zotero[n]:
		users.append('lcordero')
	if 'Farías, L' in  authors_zotero[n] or 'Farias, L' in  authors_zotero[n] or 'Ferias, L' in  authors_zotero[n]:
		users.append('lfarias')
	if 'Gallardo, L' in  authors_zotero[n] or 'Klenner, LG' in authors_zotero[n]:
		users.append('lgallardo')
	if 'Nahuelhual, L' in authors_zotero[n]:
		users.append('lnahuelhual')
	if 'Alcamán, M.E.' in authors_zotero[n] or 'Alcaman-Arias, ME' in authors_zotero[n] or 'Alcaman, ME' in authors_zotero[n]:
		users.append('malcaman')
	if 'Del Hoyo, M.' in authors_zotero[n]:
		users.append('mdelhoyo')
	if 'Galleguillos, M' in  authors_zotero[n]:
		users.append('mgalleguillos')
	if 'Gonzalez, M' in  authors_zotero[n] or 'GONZALEZ, M' in authors_zotero[n]:
		users.append('mgonzalez')
	if 'Jacques, M' in  authors_zotero[n] or 'Jacques‐Coper, Martín' in  authors_zotero[n] or 'Jacques-Coper, M' in authors_zotero[n]:
		users.append('mjacques')
	if 'Mena, M' in  authors_zotero[n] or 'Mena, Marcelo' in  authors_zotero[n] or 'Mena-Carrasco, M' in authors_zotero[n]:
		users.append('mmena')
	if 'Munizaga, M' in  authors_zotero[n]:
		users.append('mmunizaga')
	if 'Osses, M' in  authors_zotero[n]:
		users.append('mosses')
	if 'Rojas, M' in  authors_zotero[n]:
		users.append('mrojas')
	if 'Yevenes, M' in authors_zotero[n] or 'Yevenes, Mariela A.' in authors_zotero[n] or 'Yevenes, MA.' in authors_zotero[n]:
		users.append('myevenes')	
	if 'Hitschfeld, N' in  authors_zotero[n] or  'Hitschfeld-Kahler, N' in authors_zotero[n] or 'HITSCHFELD, N' in authors_zotero[n] or 'Hitschfeld‐Kahler, N' in authors_zotero[n]:
		users.append('nhitschfeld')
	if 'Huneeus, N' in  authors_zotero[n]:
		users.append('nhuneeus')
	if 'Aldunce, P' in  authors_zotero[n]:
		users.append('paldunce')
	if 'Moraga, P' in  authors_zotero[n] or 'Sariego, PM' in authors_zotero[n]:
		users.append('pmoraga')
	if 'Moreno, P' in  authors_zotero[n] or 'MORENO, PI' in authors_zotero[n]:
		users.append('pmoreno')
	if 'Smith, P' in  authors_zotero[n]:
		users.append('psmith')
	if 'Arriagada, R' in  authors_zotero[n]:
		users.append('rarriagada')
	if 'Borquez, R' in authors_zotero[n]:
		users.append('rborquez')
	if 'De Polz-Holz, R' in  authors_zotero[n] or 'de Polz-Holz, R' in  authors_zotero[n] or 'De Pol-Holz, R' in  authors_zotero[n] or 'de Pol-Holz, R' in authors_zotero[n] or 'De Pot-Holz, R' in authors_zotero[n] or 'Holz, RD' in authors_zotero[n] or 'DePol-Holz, R' in authors_zotero[n] or 'ORyan, RE' in authors_zotero[n]:
		users.append('rdepol')
	if 'Garreaud, R' in  authors_zotero[n] or 'GARREAUD, R' in authors_zotero[n]:
		users.append('rgarreaud')
	if 'O´Ryan, R'  in  authors_zotero[n] or "O’Ryan, Raúl" in authors_zotero[n] or "O'Ryan, R" in  authors_zotero[n] or 'O"Ryan, R' in authors_zotero[n] or "O''Ryan, R" in authors_zotero[n] or "O''Ryan, R" in authors_zotero[n]:
		users.append('roryan')
	if 'Pozo, RA' in authors_zotero[n]:
		users.append('rpozo')
	if 'Rondanelli, R' in  authors_zotero[n]:
		users.append('rrondanelli')
	if 'Sapiains, R' in  authors_zotero[n] or 'Sapiains A.' in authors_zotero[n]:
		users.append('rsapiains')
	if 'Seguel, R' in  authors_zotero[n]:
		users.append('rseguel')
	if 'Valenzuela, R' in authors_zotero[n] or 'Valenzuela, RA' in authors_zotero[n]:
		users.append('rvalenzuela')
	if 'Urrutia, R' in  authors_zotero[n] or 'Urrutia-Jalabert, R' in  authors_zotero[n]:
		users.append('rurrutia')
	if 'Crespo, S' in authors_zotero[n]:
		users.append('screspo')
	if 'Gomez, S' in  authors_zotero[n] or 'Gómez, S' in  authors_zotero[n] or 'Gomez-Gonzalez, S' in authors_zotero[n] or ' Gómez‐González, Susana' in authors_zotero[n]:
		users.append('sgomez')
	if 'Ruiz Pereira, Sebastian Felipe' in authors_zotero[n]:
		users.append('sruiz')
	if 'Tolvett, S' in authors_zotero[n]:
		users.append('stolvett')
	if 'Villaseñor, T' in authors_zotero[n] or 'Villasenor, T' in authors_zotero[n]:
		users.append('tvillasenor')
	if 'Delgado, V' in  authors_zotero[n]:
		users.append('vdelgado')
	if 'Lemaire, V' in authors_zotero[n]:
		users.append('vlemaire')
	if 'Fleming, Z' in  authors_zotero[n]:
		users.append('zfleming')

	#print(users)
	#print(authors_zotero[n])
	users_all.append(users)

print(len(df["Item ID [*itemId:id]"]))
#print(users_all)
print(df["Periodo [f_752:code]"])
print(users_all)

df["Usuario [f_739:username]"] = users_all
df["Usuario [f_739:username]"] = [str(d).replace("'","").replace('[','').replace(']','').replace("''","") for d in df["Usuario [f_739:username]"]]
#print(df["Usuraio -- 739"])
#Create a new dataframe
df_intranet_created = pd.DataFrame(df, columns = ["Item ID [*itemId:id]","Status [status:system]","Usuario [f_739:username]", "Reconocimiento o Afiliacion (CR)2 [f_751:code]", "Estado [f_741:code]",
	 "Título [f_742:default]", "Autores [f_743:default]", "Lineas Involucradas [f_745:code]", "DOI [f_746:default]" ,"Código ISSN / ISBN [f_747:default]",
	  "Nombre Journal [f_748:default]","Ubicación en Línea [f_749:default]","Año de Publicación [f_750:default]", "PARTICIPACION [f_753:code]",
	  "% aportado por REGIONAL [publicacionesjournalIsiApo_rREGIONAL:default]",
	  "% aportado por FONDECYT [f_756:default]",
	  "% aportado por FONDEF [f_757:default]",
	  "% aportado por PIA [publicacionesjournalIsiApo_adoPorPIA:default]",
	  "% aportado por FONDAP [f_755:default]",
	  "% aportado por PAI [publicacionesjournalIsiApo_adoPorPAI:default]",
	  "% aportado por EXPLORA [publicacionesjournalIsiApo_orEXPLORA:default]",
	  "% aportado por colaboración Internacional [publicacionesjournalIsiApo_rnacional:default]",
	  "% aportado por Astronomia [publicacionesjournalIsiApo_stronomia:default]",
	  "% aportado por Becas (PCHA) [publicacionesjournalIsiApo_BecasPCHA:default]",
	  "% aportado por Otro (indicar) [f_760:default]",
	  "Adjunta la Publicación [f_763:default]",
	  "Abstract", "Revisión INTERNA [f_738:code]","Periodo [f_752:code]","Líneas Involucradas antiguas [f_744:code]"])

df_intranet_created.to_csv(str("output_table/intranet.csv"), sep=',', encoding='utf-8')

df_intranet = pd.read_csv("input_table/tracker_38.csv", sep=',',encoding='utf-8')
df_intranet_created = pd.read_csv("output_table/intranet.csv", sep=',',encoding='utf-8')

print(df_intranet)
print(df_intranet_created)
frames =[df_intranet,df_intranet_created]
result =pd.concat(frames,sort=False)
print(result)

result=result.drop('Unnamed: 0', 1)

print(result)
result.to_csv(str("output_table/tracker_38_modified.csv"), sep=',', encoding='utf-8', index=False)

#df_zotero.to_csv(str("test_zotero.csv"), sep=',', encoding='utf-8')
#df_intranet.to_csv(str("test_intranet.csv"), sep=',', encoding='utf-8')
