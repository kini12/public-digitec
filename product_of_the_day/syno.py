"""
This script will catpure the evolution of the price of Synology's Nas

14.12.2021 xpath changed...

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

# Request for the DS920+
page = requests.get('https://www.digitec.ch/fr/s1/product/synology-ds920-0to-serveurs-de-stockage-en-reseau-nas-13405988')
tree = html.fromstring(page.content)
article = tree.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/h1/span/text()')
price = tree.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
price = str(price)
price = price.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price = price.strip()
article = str(article)
article = article.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
article = article.strip()

print ('DS920+: ok!')  

# Request for the DS1621+
page2 = requests.get("https://www.digitec.ch/fr/s1/product/synology-ds1621-0to-serveurs-de-stockage-en-reseau-nas-14021736")
tree2 = html.fromstring(page2.content)
price2 = tree2.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
article2 = tree2.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/h1/span/text()')
price2 = str(price2)
price2 = price2.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price2 = price2.strip()
article2 = str(article2)
article2 = article2.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
article2 = article2.strip()

print ('DS1621+: ok!')  

# Request for the 110 inch screen
page3 = requests.get("https://www.digitec.ch/fr/s1/product/elite-screens-cadre-en-sable-bordure-fixe-110-169-ecrans-de-projection-8271837")
tree3 = html.fromstring(page3.content)
price3 = tree3.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
article3 = tree3.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/h1/strong/text()')
price3 = str(price3)
price3 = price3.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price3 = price3.strip()
article3 = str(article3)
article3 = article3.replace("'", "").replace(".–", "").replace("[", "").replace("]", "").replace(",", "")
article3 = article3.strip()

print("toile: ok!")

# Request for lamp
page5 = requests.get("https://www.digitec.ch/fr/s1/product/benq-lampe-benq-5jjhn05001-w1700-lampes-pour-projecteur-10923129")
tree5 = html.fromstring(page5.content)
price5 = tree5.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/div[1]/span/strong/text()')
article5 = tree5.xpath('//*[@id="pageContent"]/div/div[1]/div[2]/div/div[2]/div/h1/span/text()')
price5 = str(price5)
price5 = price5.replace("'", "").replace(".–", "").replace("[", "").replace("]", "")
price5= price5.strip()
article5 = str(article5)
article5 = article5.replace("'", "").replace(".–", "").replace("[", "").replace("]", "").replace(",", "")
article5 = article5.strip()

print("Lamp Beamer: ok!")

def temps():
    temps = time.strftime("%d.%m.%Y")
    return(temps)

# concatenation of the var we scrapped   

error = str(0)

try:
    syno1 = temps() + "," + article + "," + price
except:
    syno1 = temps() + "," + error + "," + error

try:
    syno2 = temps() + "," + article2 + "," + price2
except:
    syno2 = temps() + "," + error + "," + error

try:
    toile = temps() + "," + article3 + "," + price3
except:
    toile = temps() + "," + error + "," + error

try:
    lamp = temps() + "," + article5 + "," + price5
except:
    lamp = temps() + "," + error + "," + error

print("concatenation of data: ok!")


# copying the data to csv
text_file = open("DS920.csv", "a")
n = text_file.write(syno1 + "\n")
text_file.close()

print("DS920 into file!")

text_file2 = open("DS1621.csv", "a")
n2 = text_file2.write(syno2 + "\n")
text_file2.close()

print("DS1621 into file!")

text_file3 = open("toile.csv", "a")
n = text_file3.write(toile+ "\n")
text_file3.close()

print("toile into file!")

text_file5 = open("lamp.csv", "a")
n = text_file5.write(lamp+ "\n")
text_file5.close()

print("lamp into file!")

print ('Trying to read csv...') 

# reading csv's
A = pd.read_csv("DS920.csv")
B = pd.read_csv("DS1621.csv")
C = pd.read_csv("toile.csv")
E = pd.read_csv("lamp.csv", sep=",")

print("...done reading! Preparing for chart!")

# preparing for the chart
date_chart = A["date"]
product_chart = A["product"]
price_chart = A["price"]
date2_chart = B["date"]
product2_chart = B["product"]
price2_chart = B["price"]
date3_chart = C["date"]
product3_chart = C["product"]
price3_chart = C["price"]
date5_chart = E["date"]
product5_chart = E["product"]
price5_chart = E["price"]

# function that will create a specific marker (up, down, equal) based on the [-1] vs [-2]
p = price_chart.iloc[-2]
p = int(p)
p2 = price2_chart.iloc[-2]
p2 = int(p2)
p3 = price3_chart.iloc[-2]
p3 = int(p3)
p5 = price5_chart.iloc[-2]
p5 = int(p5)

comp = price_chart.iloc[-1]
comp2 = price2_chart.iloc[-1]
comp3 = price3_chart.iloc[-1]
comp5 = price5_chart.iloc[-1]

if p == comp:
    print("equal")
    m = "s"
elif p < comp:
    print("bigger")
    m = 6
elif p > comp:
    print("smaller")
    m = 7

if p2 == comp2:
    print("equal")
    m2 = "s"
elif p2 < comp2:
    print("bigger")
    m2 = 6
elif p2 > comp2:
    print("smaller")
    m2 = 7

if p3 == comp3:
    print("equal")
    m3 = "s"
elif p3 < comp3:
    print("bigger")
    m3 = 6
elif p3 > comp3:
    print("smaller")
    m3 = 7  

if p5 == comp5:
    print("equal")
    m5 = "s"
elif p5 < comp5:
    print("bigger")
    m5 = 6
elif p5 > comp5:
    print("smaller")
    m5 = 7


# chart...
plt.figure(figsize=(20,10))
plt.plot(date_chart.iloc[-20:], price_chart.iloc[-20:], color="red", linestyle= "-", label="DS920+", marker= m)
plt.plot(date2_chart.iloc[-20:], price2_chart.iloc[-20:], color="blue", linestyle= "-", label="DS1621+", marker= m2) 
plt.xticks(date_chart.iloc[-20:], rotation=25)
plt.legend(loc="center left")
plt.tight_layout()
plt.savefig("chart.png")
plt.close()

print ('chart created 1/3 !')  

# plt.plot(date4_chart, price4_chart, color="black", linestyle= "-", label="RTX 3060ti", marker= m4) 
plt.figure(figsize=(15,10))
plt.plot(date3_chart.iloc[-20:], price3_chart.iloc[-20:], color="green", linestyle= "-", label="Toile", marker= m3)
plt.xticks(date3_chart.iloc[-20:], rotation=25)
plt.legend(loc="center left")
plt.tight_layout()
plt.savefig("chart2.png")
plt.close()

print ('chart created 2/3 !')  

plt.figure(figsize=(20,10))
plt.plot(date5_chart.iloc[-20:], price5_chart.iloc[-20:], color="purple", linestyle= "-", label="lampe", marker= m5)
plt.xticks(date5_chart.iloc[-20:], rotation=25)
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("chart3.png")

print ('chart created 3/3 !')

# comparaison of last price vs price of the day
lastAprice = A["price"]
lastAprice = lastAprice.iloc[-2]
lastAprice = int(lastAprice)
lastBprice = B["price"]
lastBprice = lastBprice.iloc[-2]
lastBprice = int(lastBprice)
lastCprice = C["price"]
lastCprice = lastCprice.iloc[-2]
lastCprice = int(lastCprice)
lastEprice = E["price"]
lastEprice = lastEprice.iloc[-2]
lastEprice = int(lastEprice)

price = int(price)
price2 = int(price2)
price3 = int(price3)
price5 = int(price5)

result = price - int(lastAprice) 
result2 = price2 - int(lastBprice)
result3 = price3 - int(lastCprice)
result5 = price5 - int(lastEprice)
     
# part for the mail sending report
gmailUser = 'xxxxxxx@gmail.com'
gmailPassword = "xxxxxx"
recipient = 'xxxxxx@gmail.com'
nl = "\n"

message = f"""Price of the day for {article2} is : CHF {price2} {nl} {nl} Diff. with yesterday {result2} {nl} {nl} Price of the day for {article} is : CHF {price} {nl} {nl} Diff. with yesterday {result} {nl} {nl} Price of the day for {article3} is : CHF {price3} {nl} {nl} Diff. with yesterday {result3} {nl} {nl} Price of the day for {article5} is : CHF {price5} {nl} {nl} Diff. with yesterday {result5} """

msg = MIMEMultipart()
msg['From'] = f'"VM K12" <{gmailUser}>'
msg['To'] = recipient
msg['Subject'] = f"Product's price"
msg.attach(MIMEText(message))

img = "chart.png"
img_data = open(img, "rb").read()
image = MIMEImage(img_data, name = os.path.basename(img))
msg.attach(image)

img2 = "chart2.png"
img2_data = open(img2, "rb").read()
image2 = MIMEImage(img2_data, name = os.path.basename(img2))
msg.attach(image2)

img3 = "chart3.png"
img3_data = open(img3, "rb").read()
image3 = MIMEImage(img3_data, name = os.path.basename(img3))
msg.attach(image3)

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
