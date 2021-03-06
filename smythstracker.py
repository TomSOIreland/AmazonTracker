import smtplib
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = 'https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259'


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=chrome_options)
sender = 'tmalkiewicz@gmail.com'
receiver = 'tmalkiewicz@gmx.com,tmalkiewicz@gmail.com'


def trackAvailability():
    availability = str(get_availability())
    str1 = availability[:3]
    print(availability)
    print(str1)
    if str1 != "Out":
        print(f"{get_title()} is {availability}, {str1}")
        sendMailYes()

    else:
        print(f"{get_title()} is {availability}")
        sendMailNo()


def get_availability():
    driver.get(BASE_URL)
    try:
        return str(driver.find_element_by_class_name('stockStatusMessage').text)
    except Exception as e:
        print(e)
        print('Can not find this element')
        return None


def get_title():
    driver.get(BASE_URL)
    try:
        return driver.find_element_by_css_selector('h1').text
    except Exception as e:
        print(e)
        return None


def sendMailYes():
    subject = f'{get_availability()} - {get_title()} - Smyths Status'
    message = f"""From: {sender}
To: {receiver}
MIME-Version: 1.0
Content-type: text/html
Subject: {get_title()} - Smyths Status'


<b>{get_title()}</b> is {get_availability()}
<p>{BASE_URL}</p>
"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, 'vojyzhkwcxwpuyzi')
    server.sendmail(sender, receiver, message)
    pass


def sendMailNo():
    subject = f'{get_availability()} - {get_title()} - Smyths Status'
    message = f"""From: {sender}
To: {receiver}
MIME-Version: 1.0
Content-type: text/html
Subject: {get_title()} - Smyths Status'


<b>{get_title()}</b> is {get_availability()}
<p>{BASE_URL}</p>
"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, 'vojyzhkwcxwpuyzi')
    server.sendmail(sender, receiver, message)
    pass


if __name__ == '__main__':
    while True:
        trackAvailability()
        time.sleep(300)
