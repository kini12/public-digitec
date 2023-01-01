"""
This script will catpure the evolution of the price of HD seagate ironwolf and wd red 

13.02.2022

v.0.2

"""

from lxml import html
import requests
import time
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from matplotlib import pyplot as plt
from email.mime.image import MIMEImage
import os

# Request for Seagate ironwolf 4 tb
capacity1 = "4"
product1 = f"IronWolf"
page1 = requests.get('https://www.digitec.ch/fr/s1/product/seagate-ironwolf-4-to-35-cmr-disques-durs-5961176?supplier=406802')
tree1 = html.fromstring(page1.content)
price1 = tree1.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price1 = str(price1)
price1 = price1.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price1 = price1.strip()
#print (f'{product1}: price of the day {price1}')  

# Request for Seagate ironwolf 6 tb
capacity2 = "6"
product2 = f"IronWolf"
page2 = requests.get('https://www.digitec.ch/fr/s1/product/seagate-ironwolf-6-to-35-cmr-disques-durs-12559857')
tree2 = html.fromstring(page2.content)
price2 = tree2.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price2 = str(price2)
price2 = price2.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price2 = price2.strip()
#print (f'{product2}: price of the day {price2}') 

# Request for Seagate ironwolf 8 tb
capacity3 = "8"
product3 = f"IronWolf"
page3 = requests.get('https://www.digitec.ch/fr/s1/product/seagate-ironwolf-8-to-35-cmr-disques-durs-12243540')
tree3 = html.fromstring(page3.content)
price3 = tree3.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price3 = str(price3)
price3 = price3.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price3 = price3.strip()
#print (f'{product3}: price of the day {price3}') 

# Request for Seagate ironwolf 10 tb
capacity4 = "10"
product4 = f"IronWolf"
page4 = requests.get('https://www.digitec.ch/fr/s1/product/seagate-ironwolf-10-to-35-cmr-disques-durs-12243539')
tree4 = html.fromstring(page4.content)
price4 = tree4.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price4 = str(price4)
price4 = price4.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price4 = price4.strip()
#print (f'{product4}: price of the day {price4}') 

# Request for Seagate ironwolf 12 tb
capacity5 = "12"
product5 = f"IronWolf"
page5 = requests.get('https://www.digitec.ch/fr/s1/product/seagate-ironwolf-12-to-35-cmr-disques-durs-11697489')
tree5 = html.fromstring(page5.content)
price5 = tree5.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price5 = str(price5)
price5 = price5.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price5 = price5.strip()
#print (f'{product5}: price of the day {price5}') 

# Request for Seagate ironwolf 16 tb
capacity6 = "16"
product6 = f"IronWolf"
page6 = requests.get('https://www.digitec.ch/fr/s1/product/seagate-ironwolf-16-to-35-cmr-disques-durs-11205773')
tree6 = html.fromstring(page6.content)
price6 = tree6.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price6 = str(price6)
price6 = price6.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price6 = price6.strip()
#print (f'{product6}: price of the day {price6}') 


# Request for Western Digital Red Plus 4 TO
capacity7 = "4"
product7 = f"Red Plus"
page7 = requests.get('https://www.digitec.ch/fr/s1/product/wd-red-plus-4-to-35-cmr-disques-durs-14726161')
tree7 = html.fromstring(page7.content)
price7 = tree7.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price7 = str(price7)
price7 = price7.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price7 = price7.strip()
#print (f'{product7}: price of the day {price7}') 

# Request for Western Digital Red Plus 6 TO
capacity8 = "6"
product8 = f"Red Plus"
page8 = requests.get('https://www.digitec.ch/fr/s1/product/wd-red-plus-6-to-35-cmr-disques-durs-14726160')
tree8 = html.fromstring(page8.content)
price8 = tree8.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price8 = str(price8)
price8 = price8.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price8 = price8.strip()
#print (f'{product8}: price of the day {price8}') 

# Request for Western Digital Red Plus 8 TO
capacity9 = "8"
product9 = f"Red Plus"
page9 = requests.get('https://www.digitec.ch/fr/s1/product/wd-red-plus-8-to-35-cmr-disques-durs-18807934')
tree9 = html.fromstring(page9.content)
price9 = tree9.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price9 = str(price9)
price9 = price9.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price9 = price9.strip()
#print (f'{product9}: price of the day {price9}') 

# Request for Western Digital Red Plus 10 TO
capacity10 = "10"
product10 = f"Red Plus"
page10 = requests.get('https://www.digitec.ch/fr/s1/product/wd-red-plus-10-to-35-cmr-disques-durs-14726158')
tree10 = html.fromstring(page10.content)
price10 = tree10.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price10 = str(price10)
price10 = price10.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price10 = price10.strip()
#print (f'{product10}: price of the day {price10}') 

# Request for Western Digital Red Plus 12 TO
capacity11 = "12"
product11 = f"Red Plus"
page11 = requests.get('https://www.digitec.ch/fr/s1/product/wd-red-plus-12-to-35-cmr-disques-durs-14726157')
tree11 = html.fromstring(page11.content)
price11 = tree11.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price11 = str(price11)
price11 = price11.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price11 = price11.strip()
#print (f'{product11}: price of the day {price11}') 

# Request for Western Digital Red Plus 14 TO
capacity12 = "14"
product12 = f"Red Plus"
page12 = requests.get('https://www.digitec.ch/fr/s1/product/wd-red-plus-14-to-35-cmr-disques-durs-14726156')
tree12 = html.fromstring(page12.content)
price12 = tree12.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price12 = str(price12)
price12 = price12.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price12 = price12.strip()
#print (f'{product12}: price of the day {price12}') 

print("Scrapping done...")

def temps():
    temps = time.strftime("%d.%m.%Y")
    return(temps)

# concatenation of the var we scrapped  

prod1 = temps() + "," + capacity1 + "," + price1 + "," + product1
prod2 = temps() + "," + capacity2 + "," + price2 + "," + product2
prod3 = temps() + "," + capacity3 + "," + price3 + "," + product3
prod4 = temps() + "," + capacity4 + "," + price4 + "," + product4
prod5 = temps() + "," + capacity5 + "," + price5 + "," + product5
prod6 = temps() + "," + capacity6 + "," + price6 + "," + product6
prod7 = temps() + "," + capacity7 + "," + price7 + "," + product7
prod8 = temps() + "," + capacity8 + "," + price8 + "," + product8
prod9 = temps() + "," + capacity9 + "," + price9 + "," + product9
prod10 = temps() + "," + capacity10 + "," + price10 + "," + product10
prod11 = temps() + "," + capacity11 + "," + price11 + "," + product11
prod12 = temps() + "," + capacity12 + "," + price12 + "," + product12

print("Concatenation done...")

# copying the data to csv
text_file = open("HD.csv", "a")
n = text_file.write(prod1 + "\n" + prod2 + "\n" + prod3 + "\n" + prod4 + "\n" + prod5 + "\n" + prod6 + "\n" + prod7 + "\n" + prod8 + "\n" + prod9 + "\n" + prod10+ "\n" + prod11 + "\n" + prod12 + "\n")
text_file.close()

print("Data copied to the file...")

     
# part for the mail sending report
# need to update this part with your data...
gmailUser = 'xxxxxxxxxh@gmail.com'
gmailPassword = "xxxxxxxxx"
recipient = 'xxxxxxx@gmail.com'
nl = "\n"

message = f""" today's script was able to get this: {nl} {nl} {prod1} {nl} {prod2} {nl} {prod3} {nl} {prod4} {nl} {prod5} {nl} {prod6} {nl} {nl} {prod7} {nl} {prod8} {nl} {prod9} {nl} {prod10} {nl} {prod11} {nl} {prod12}"""

msg = MIMEMultipart()
msg['From'] = f'"VM K12 HD price" <{gmailUser}>'
msg['To'] = recipient
msg['Subject'] = f"HD's price"
msg.attach(MIMEText(message))

try:
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmailUser, gmailPassword)
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    mailServer.close()
    print ('Email sent!')
except:
    print ('Something went wrong...')  

  