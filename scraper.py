#importing process
#the request module allows to send HTTP requests to python
import requests
from bs4 import BeautifulSoup
import smtplib # enables you to send emails
import ssl



URL = 'https://www.amazon.com/Grand-Theft-Auto-V-PlayStation-4/dp/B00KVSQ848/ref=sr_1_1?crid=1093X4RFGGT8M&dchild=1&keywords=gta+5&qid=1589200932&sprefix=gta+%2Caps%2C400&sr=8-1'



headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    #originally, the code was:  soup = BeautifulSoup(page.content, 'html.parser') [lxml]---> works
    # But it gave the output of "None"
    soup = BeautifulSoup(page.content, 'lxml') 

    # the webscrape algorithm
    title = soup.find(id = "productTitle").get_text()
    str_price = soup.find(id = "priceblock_ourprice").get_text()


    # converting the price into a number  
    converted_price = float(str_price[1:6])

    #input price that you would buy the product for
    str_enter_price = input ("Enter the price that you would buy this product for:")
    enter_price = float(str_enter_price)
    if (converted_price < enter_price):
        send_mail()
    else: 
        print("Price has not dropped yet")


    print(title.strip())
    print (converted_price)
    print(enter_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', port = 587)
    server.ehlo()
    server.starttls #encrypts the connection
    server.ehlo()
    server.login('sathwikapps@gmail.com', 'Jaybeatx')

    

    text = 'The price has dropped!'

    server.sendmail(
        'sathwikapp@gmail.com',
        'sathwikhack@gmail.com',
        text

    )

    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()


    
        
        








    