import smtplib
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = 'https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259'

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)

sender = 'tmalkiewicz@gmail.com'
receiver = 'tmalkiewicz@gmx.com,tmalkiewicz@gmail.com'


def trackAvailability():
    availability = str(get_availability())
    str1 = availability[:3]
    print(availability)
    print(str1)
    if str1 != "Out":
        print(f"{get_title()} is {availability}, {str1}")
        sendMail()

    else:
        print(f"{get_title()} is {availability}")



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

def run():
    driver.get(BASE_URL)
    time.sleep(2)
    driver.quit()


def sendMail():
    subject = f'{get_title()} - Smyths Status'
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
