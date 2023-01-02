#!/usr/bin/env python3
# coding: utf-8!

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
This script gets the product of the day of Digitec and extract 5 values: date, brand, name, oprice and nprice.

It checks in the precedent db record if the % of the db is < or > with the % of the day. Then, checks if the brand
of the day was already in the db. If so, return the date, oprice, nprice and mean value of %.  

Once that is done, it sends a mail with the data captured, the comparison and the old data of db, if existant.

26.12.2022 correction of the script (all var -> all2)
04.09.2022 huge rewriting of the script - bug correction

"""

# # getting the LiveShopping/81 page of digitec -> beautifulsoup
r=requests.get("https://www.digitec.ch/fr/LiveShopping/81")
c=r.content
soup=BeautifulSoup(c,"html.parser")
all = soup.get_text()

print("1/4 We are starting the regex part of the script.")

# aiming at a specific part, to capture a str that is the start point for oprice,nprice,brand and name
pattern = re.compile("Offre du jour")
matches = pattern.finditer(all)
for match in matches:
    span = match.span()
    vmin, vmax = span
    start = vmin 
    end = vmax + 300
text_to_extract = all[start:end] 

# part were we capture the infos for the 5th column (end_of_txt)
text_to_extract = text_to_extract.split("Jusqu")
text_to_extract = text_to_extract[0]
text_to_extract = text_to_extract.replace(",","")
text_to_extract = text_to_extract.split(")")
all_text = text_to_extract[0]

# here we try to capture the minimum so we can later work on a smaller portion of the full chain
# that we obtained up above (text_to_extract variable) -> working on the 4th elements I need
text_to_extract = str(text_to_extract)
text_to_extract = text_to_extract.split("Jusqu")
text_to_extract = text_to_extract[0]
text_to_extract = text_to_extract.split("pièces")
text_to_extract = text_to_extract[1]
small_text = text_to_extract[0:102]

#it's the join between my two scripts, my jupyter notebook test script and this script
test1 = small_text

# this splits the test1 string, using .- as ref. 
# this allows me to have a list and a str of the data, ready to be used for oprice and nprice 
# and also for the branch detection of "au lieu de" and "avant"
l_splitted = test1.split(".–")
str_splitted = l_splitted
str_splitted = str(str_splitted)

# we create a branch (Y). Some data has "au lieu" and some has "avant"
# still matters in 2022. 90% of data has "avant", rest is important though
avant_au_lieu = str_splitted.split(",")
try:
    avant_au_lieu = avant_au_lieu[1]
except:
    avant_au_lieu 

if "au lieu" in str_splitted:
    print("01 au lieu branch")
    # this is the branch
    # searching for words starting with letters in test1
    # gets the brand name

    def words():
        match = re.findall(r"[a-zA-Zéèàêîâ&Ø]+", test1)
        return(match)
    chain_of_words = words()
    chain_of_words = str(chain_of_words)
    chain_of_words = chain_of_words.replace("sur", "").replace("vendues", "").replace("avant", "")
    chain_of_words = chain_of_words.replace("au", "").replace("lieu", "").replace("de","")
    chain_of_words = chain_of_words.replace(",", "").replace("''", "").replace('""', "")
    chain_of_words = chain_of_words.split(" ")
    brand = chain_of_words[4]
    brand = brand.replace("'", "")

    # this is the brand detection part, with some exceptions and rules
    # this can also handle captital letters added to the brand. It's not so actual, but was at some point
    b_o = "B&O"
    Asus = "ASUS"
    AOC = "AOC"
    Sandisk = "Sandisk"
    LG = "LG"
    tp = "TP-Link"
    sam = "Samsung"
    crucial = "Crucial"
    wd = "WD"
    king = "Kingston"
    rod = "RØDE"
    pny = "PNY"
    hp = "HP"
    if Asus in brand:
        print("branch Asus")
        brand = Asus    
    elif tp in brand:
        print("branch TP-LINK")
        brand = tp    
    elif sam in brand:
        print("branch Samsung")
        brand = sam    
    elif LG in brand:
        print("branch LG")
        brand = LG    
    elif b_o in brand:
        print("branch B&O")
        brand = b_o    
    elif Sandisk in brand:
        print("branch Sandisk")
        brand = Sandisk    
    elif crucial in brand:
        print("branch Crucial")
        brand = crucial    
    elif wd in brand:
        print("branch wd")
        brand = wd    
    elif rod in brand:
        print("branch RØDE")
        brand = rod    
    elif king in brand:
        print("branch Kingston")
        brand = king    
    elif pny in brand:
        print("branch pny")
        brand = pny    
    elif hp in brand:
        print("branch HP")
        brand = hp
    elif brand.isupper():
        print("branch D")
        brand    
    elif brand[1].isupper() and brand[2].islower():
        print("branch B")
        brand = brand[1:]    
    elif len(brand) >= 1:
        print("branch A")
        brand = brand   
    else:
        print("branch C")
        brand = brand[0:]
    
    # searching for words starting with letters in test1
    # gets the detail name
    def words2():
        match2 = re.findall(r"[a-zA-Zéèàêîâ&Ø]+", test1)
        return(match2)
    chain_of_words2 = words2()
    chain_of_words2 = str(chain_of_words2)
    chain_of_words2 = chain_of_words2.replace("sur", "").replace("vendues", "").replace("avant", "").replace("au", "").replace("lieu", "").replace("de","").replace(",", "").replace("''", "").replace('""', "").replace("]", "")
    chain_of_words2 = chain_of_words2.split(" ")
    name = chain_of_words2[5]
    name = name.replace("'", "")
    if len(name) < 1:
        long_name = re.findall(r"[a-zA-Zéèàêîâ\d]+", l_splitted[1])
        name = long_name[3]
    if len(name) == 1:
        long_name = re.findall(r"[a-zA-Zéèàêîâ\d]+", l_splitted[2])
        name = long_name[1] 

#this is the branch part that works with 02 avant branch. This is the old code that has always been working fine
else:
    "avant" in str_splitted
    print("02 avant branch")
    # searching for words starting with letters in test1
    # gets the brand name
    def words():
        match = re.findall(r"[a-zA-Zéèàêîâ&Ø]+", test1)
        return(match)
    chain_of_words = words()
    chain_of_words = str(chain_of_words)
    chain_of_words = chain_of_words.replace("sur", "").replace("vendues", "").replace("avant", "")
    chain_of_words = chain_of_words.replace("au", "").replace("lieu", "").replace("de","")
    chain_of_words = chain_of_words.replace(",", "").replace("''", "").replace('""', "")
    chain_of_words = chain_of_words.split(" ")
    brand = chain_of_words[2]
    brand = brand.replace("'", "")

    # this is the brand detection part, with some exceptions and rules
    # this can also handle captital letters added to the brand. It's not so actual, but was at some point
    b_o = "B&O"
    Asus = "ASUS"
    AOC = "AOC"
    Sandisk = "Sandisk"
    LG = "LG"
    tp = "TP-Link"
    sam = "Samsung"
    crucial = "Crucial"
    wd = "WD"
    king = "Kingston"
    rod = "RØDE"
    pny = "PNY"
    hp = "HP"
    if Asus in brand:
        print("branch Asus")
        brand = Asus    
    elif tp in brand:
        print("branch TP-LINK")
        brand = tp    
    elif sam in brand:
        print("branch Samsung")
        brand = sam    
    elif LG in brand:
        print("branch LG")
        brand = LG    
    elif b_o in brand:
        print("branch B&O")
        brand = b_o    
    elif Sandisk in brand:
        print("branch Sandisk")
        brand = Sandisk    
    elif crucial in brand:
        print("branch Crucial")
        brand = crucial    
    elif wd in brand:
        print("branch wd")
        brand = wd    
    elif rod in brand:
        print("branch RØDE")
        brand = rod    
    elif king in brand:
        print("branch Kingston")
        brand = king    
    elif pny in brand:
        print("branch pny")
        brand = pny    
    elif hp in brand:
        print("branch HP")
        brand = hp
    elif brand.isupper():
        print("branch D")
        brand    
    elif brand[1].isupper() and brand[2].islower():
        print("branch B")
        brand = brand[1:]    
    elif len(brand) >= 1:
        print("branch A")
        brand = brand   
    else:
        print("branch C")
        brand = brand[0:]

    # searching for words starting with letters in test1
    # gets the detail name
    def words2():
        match2 = re.findall(r"[a-zA-Zéèàêîâ&Ø]+", test1)
        return(match2)
    chain_of_words2 = words2()
    chain_of_words2 = str(chain_of_words2)
    chain_of_words2 = chain_of_words2.replace("sur", "").replace("vendues", "").replace("avant", "").replace("au", "").replace("lieu", "").replace("de","").replace(",", "").replace("''", "").replace('""', "").replace("]", "")
    chain_of_words2 = chain_of_words2.split(" ")
    name = chain_of_words2[3]
    name = name.replace("'", "")
    if len(name) < 1:
        long_name = re.findall(r"[a-zA-Zéèàêîâ\d]+", l_splitted[1])
        name = long_name[3]
    if len(name) == 1:
        long_name = re.findall(r"[a-zA-Zéèàêîâ\d]+", l_splitted[2])
        name = long_name[1]  

# ugly way to remove the "sur xxx"
# create a dictionnary ? a rule that removes the 2 or 3 first caracters ? it's happening so since march-april 2022...
l_splitted[0] = l_splitted[0].replace("sur 1000", "").replace("sur 100", "").replace("sur 110", "").replace("sur 120", "").replace("sur 130", "").replace("sur 140", "").replace("sur 150", "").replace("sur 160", "").replace("sur 170", "").replace("sur 180", "").replace("sur 190", "").replace("sur 200", "").replace("sur 210", "").replace("sur 220", "").replace("sur 230", "").replace("sur 240", "").replace("sur 250", "").replace("sur 260", "").replace("sur 270", "").replace("sur 280", "").replace("sur 290", "").replace("sur 300", "").replace("sur 310", "").replace("sur 320", "").replace("sur 330", "").replace("sur 340", "").replace("sur 350", "").replace("sur 360", "").replace("sur 370", "").replace("sur 380", "").replace("sur 390", "").replace("sur 400", "").replace("sur 410", "").replace("sur 420", "").replace("sur 430", "").replace("sur 440", "").replace("sur 450", "").replace("sur 460", "").replace("sur 470", "").replace("sur 480", "").replace("sur 490", "").replace("sur 500", "").replace("sur 510", "").replace("sur 520", "").replace("sur 530", "").replace("sur 540", "").replace("sur 550", "").replace("sur 560", "").replace("sur 570", "").replace("sur 580", "").replace("sur 590", "").replace("sur 600", "").replace("sur 610", "").replace("sur 620", "").replace("sur 630", "").replace("sur 640", "").replace("sur 650", "").replace("sur 660", "").replace("sur 670", "").replace("sur 680", "").replace("sur 690", "").replace("sur 700", "").replace("sur 710", "").replace("sur 720", "").replace("sur 730", "").replace("sur 740", "").replace("sur 750", "").replace("sur 760", "").replace("sur 770", "").replace("sur 780", "").replace("sur 790", "").replace("sur 800", "").replace("sur 810", "").replace("sur 820", "").replace("sur 830", "").replace("sur 840", "").replace("sur 850", "").replace("sur 860", "").replace("sur 870", "").replace("sur 880", "").replace("sur 890", "").replace("sur 900", "").replace("sur 910", "").replace("sur 920", "").replace("sur 930", "").replace("sur 940", "").replace("sur 950", "").replace("sur 960", "").replace("sur 970", "").replace("sur 980", "").replace("sur 990", "").replace("sur 1000", "").replace("sur 10", "").replace("sur 15", "").replace("sur 20", "").replace("sur 25", "").replace("sur 30", "").replace("sur 35", "").replace("sur 40", "").replace("sur 45", "").replace("sur 50", "").replace("sur 55", "").replace("sur 60", "").replace("sur 65", "").replace("sur 70", "").replace("sur 75", "").replace("sur 80", "").replace("sur 85", "").replace("sur 90", "")
print(l_splitted[0])

# try - except to get the nprice based on the possible positions
# this captures numbers with decimal as well as regular configuration
if len(l_splitted) == 1:
    nprice = re.findall("[0-9]+", l_splitted[0]) 
    nprice = nprice[0]+"."+nprice[1]
    
else:
    nprice = re.findall("[0-9]+", l_splitted[0])
    nprice = str(nprice)
    nprice = nprice.replace("'", "").replace("[", "").replace("]", "")

# two ways, 01 if . in the list, 02 if simple number
# we get decimal number here as well (not originally implented)
if len(l_splitted) < 2:
    oprice = re.findall("[0-9]+", l_splitted[0]) 
else:
    oprice = re.findall("[0-9]+", l_splitted[1])
     
if len(oprice) > 1:
    try:
        oprice = re.findall("[0-9]*\.[0-9][0-9]", l_splitted[1])
        oprice = oprice[0:1]
    except IndexError:
        oprice = re.findall("[0-9]*\.[0-9][0-9]", l_splitted[0])
        oprice = oprice[1]      
else:
    oprice = re.findall("[0-9]+", l_splitted[1])
oprice = str(oprice)
oprice = oprice.replace("'", "").replace("[", "").replace("]", "")

# getting the time of the day variable, formatted the way I want.
def temps():
    temps = time.strftime("%d.%m.%Y")
    return(temps)
temps()

# 5th column
pos1=all_text.index(oprice) +5
long_text = all_text[pos1:]
long_text = long_text.replace("(","").replace(",", "")
pos2 = long_text.index(name)
length = len(name)
pos2 = pos2 + length
long_text = long_text[pos2:]
end_of_txt = long_text
end_of_txt = end_of_txt.strip()
end_of_txt2 = long_text
end_of_txt2 = end_of_txt2.split("plus que")


# the conlusion of the script, creation of the data formatted 
all = temps() + "," + str(brand) + "," + str(name) + "," + oprice + "," + nprice + "," + str(end_of_txt)
all = all.replace("'", "").replace('"', "").replace('"', "")
all2 = temps() + "," + str(brand) + "," + str(name) + "," + oprice + "," + nprice + "," + small_text

print("2/4 Values captured today: " + all2)

# we copy the data into a csv file
l = []
l.append(all2)
df=pd.DataFrame(l)
df.to_csv("Digitec.csv", index=False, header=None, encoding ="utf-8", mode="a")

print("3/4 Values were passed to the file properly.")

# this sets the pandas option to 2 decimals
pd.options.display.float_format = "{:,.2f}".format

# here we work on the difference between the oprice and the nprice
# calculation of the discount
object_discount = float(oprice) - float(nprice)
oprice = float(oprice)

# calculation of the %
max = oprice/100
object_discount_percentage = object_discount / max
object_discount_percentage = int(object_discount_percentage)

# now we collect the discounts of the db
df = pd.read_csv("Digitec.csv", encoding='latin-1', sep=",")
db_discount = df.old_price - df.new_price

# 1%
max = df.old_price/100 
db_discount_pourcentage = db_discount / max
db_discount_pourcentage.round(2)
df["discount"]= db_discount
df["%"]=db_discount_pourcentage.round(2)
db_result = df.mean()
db_result = db_result[3]
result_db = db_result.round(2)

# here we have the check in the db for the old value
value = all
# getting the brand to look for into the db
db_brand = value.split(",")
db_brand = db_brand[1]
db_brand = db_brand.strip()
# getting the name_product to look for into the db
db_name = value.split(",")
db_name = db_name[2]
db_name = db_name.strip()
# creating a str with the data of the day
db_query = db_brand + " " + db_name
db_query = str(db_query)
check_db = df["brand"] + " " + df["name_product"]
check_db = str(check_db)
df2 = df[df["brand"].str.count(db_brand)>0] 

df3 = df2[df2["name_product"].str.count(db_name)>0]
# check if df3 contains something, if not, special message
if len(df3) == 0:
    df3 = "there is no match"
else:
    df3 = df3

try:
    df3 = df3.drop(columns=["name_product", "discount", "brand","detail"])
except AttributeError as error:
    df3 = df2.drop(columns=["name_product", "discount", "brand","detail"])

# mean of the df3 chart
mean = df3["%"].mean()
mean = round(mean, 2)
    
# part for the mail sending report
# you need your data to send the mail...
gmailUser = 'XXXXXXXh@gmail.com'
gmailPassword = "XXXXXXX"
recipient = 'XXXXX@gmail.com'
nl = "\n"

message = f"""Today's script was able to collect this: {nl} {nl} {all2} {nl} {nl} % of the day is: {object_discount_percentage}% {nl} {nl} % of the db is: {result_db}% {nl}{nl} The mean value of the returned results is: {mean}% {nl}{nl} ancient entries in the db:{nl}{nl}{df3} {nl}{nl}"""

msg = MIMEMultipart()
msg['From'] = f'"VM K12" <{gmailUser}>'
msg['To'] = recipient
msg['Subject'] = f"digitec of the day"
msg.attach(MIMEText(message))

try:
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    print("a, smtplib ok...")
    mailServer.ehlo()
    print("b, ehlo ok...")
    mailServer.starttls()
    print("c, tls ok...")
    mailServer.ehlo()
    print("d, ehlo second time ok...")
    mailServer.login(gmailUser, gmailPassword)
    print("e, login ok...")
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    print("f, sendmail ok...")
    mailServer.close()
    print("g, closing...")
    print ('4/4 Email sent!')
except:
    print ('4/4 Something went wrong...')