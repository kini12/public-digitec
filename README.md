# public-digitec

Product_of_the_day

The product_of_the_day.py script allows to capture the product of the day on the www.digitec.ch website. Everyday, a product has a discount and is pushed on the first page of the website.

This script is not functional during Black Friday, Cyber Monday, or period of time when more than one product are offered with a discount.

This script captures the date, brand, name of product, old price, new price, rest of the informations about the daily product (see csv file for exemple). 

This also checks into the db Digitec.csv if the brand was already offering a discount in the past. This can be found in a comparison to the message that can be sent with the script

The data_read.ipynb allows to read data from the Digitec.csv file. From there, you can export the data into output.csv file.

The read_output_csv.ipynb allows to read the output.csv file and obtain the top 5 product (best discount) for 2022, 2021 and 2020

Should you have any querys, don't hesitate to reach me ! 
