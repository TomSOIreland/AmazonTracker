import requests
from bs4 import BeautifulSoup
import time
import smtplib

url = 'https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452?ref_=ast_sto_dp'

HEADERS = {
    "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"}

emailto = 'tmalkiewicz@gmail.com'
emailfrom = 'tmalkiewicz@gmx.com'
ccemail = 'smalkiewicz@icloud.com'

page = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('span', {'id': 'productTitle'}).get_text().strip()
availability = soup.find('div', {'id': 'availability'}).find('span').get_text().strip()

def trackAvailability():
    availability = getAvailability()
    print(availability)
    if availability != 'Currently unavailable.':
        print('PS5 in now available')
    else:
        print('Still Nothing')
        sendMail()


def getAvailability():
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('span', {'id': 'productTitle'}).get_text().strip()
    availability = soup.find('div', {'id': 'availability'}).find('span').get_text().strip()
    print(title)
    return availability


def sendMail():
    subject = f'{title} Available!!! on Amazon\n'
    mailtext = subject + '\nThe Ps5 is now Available\n' + url
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(emailto, 'vojyzhkwcxwpuyzi')
    server.sendmail(emailto, emailfrom, mailtext)
    pass


if __name__ == "__main__":
    while True:
        trackAvailability()
        time.sleep(10)
