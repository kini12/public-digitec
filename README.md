# public-digitec

This repository contains 3 Python scripts.


1) HD's Price

The py script allows to capture the prize of some Ironwolf and WD Red Plus HD on the website www.digitec.ch

Captures the data and paste it into a csv file.

The data_reader_HD.ipynb allows to read the data of the csv file and the obtain a chart of the prize evolution.


2) Product's Price

The py script allows to capture the prize of some product (Synology DS920 / DS923 / DS1621 and a lamp for Benq W1720 Beamer, as well as a technical canvas for home teater) on the website www.digitec.ch

The syno_price.ipynb allows to read the data of the different csv files, in order to obtain a chart of the evolution of the prize.

-------------

For 1) and 2), you need to put the Xpath of the value you want to save into the db (Xpath of the product name + Xpath of the prize of the product) into the py script.

-------------


3) Product_of_the_day

The py script allows to capture the product of the day on the www.digitec.ch website. Everyday, a product has a discount and is pushed on the first page of the website.
This script captures the date, name of product, brand, old price, new price, rest of the informations about the daily product (see csv file for exemple). Script also 
check into the db if the brand was already offering a discount in the past. A comparison is then made into the message

The data_read.ipynb allows to read data from the Digitec.csv file. From there, you can export the data into output.csv file.

The read_output_csv.ipynb allows to read the output.csv file and obtain the top 5 product (best discount) for 2022, 2021 and 2020

Should you have any querys, don't hesitate to reach me ! 

I'm still a padawan about Python, but open to suggestions !





