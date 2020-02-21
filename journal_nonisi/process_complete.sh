#!/bin/bash 
echo "First you have to export the table of Zotero,  normally you have to use cr2_2020_nonisi for the year corresponding & you must export it like 06_zotero.csv. Into 00_cr2_articles.csv you must add all DOI's for looking for them in the process ... but all the files have to be into input_table "

echo "Processing... environmental variables ..."

#source .bashrc
echo "Downloading master list of scopus..."
python 01_process_scopus.py

sleep 10

l=$(pwd)

echo "Moving files from Download to input_table"
mv /home/nvaldebenito/Descargas/scopus.csv $l/input_table/01_scopus.csv
echo "Import table manually, into masterlist  "

echo "Creating table for intranet"
python 06_process_intranet.py

echo "Exporting table on wordpress"
python 07_export_from_wordpress.py

echo "Moving table wordpress exported"
mv /home/nvaldebenito/Descargas/13-*.csv $l/input_table/wordpress.csv

echo "Creating table for wordpress"
python 07_process_wordpress.py


echo "Creating table for masterlist"
python 08_process_cr2articles.py
echo "Import table manually, please "

#echo "Creating table for conicyt"
#python 09_process_conicyt.py

echo "Importing table on intranet"
python 06_import_to_intranet.py

echo "Importing table on wordpress"
python 07_import_to_wordpress.py

#echo "Importing table on conicyt"
#python 09_import_to_conicyt.py
