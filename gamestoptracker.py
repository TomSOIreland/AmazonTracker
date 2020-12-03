import smtplib
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://www.gamestop.ie/PlayStation%205/Games/72504/playstation-5-console'

class GSTracker:
    def __init__(self, url):
        self.url = url
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome('./chromedriver.exe', options=options)

    def get_title(self):
        self.driver.get(self.url)
        try:
            return self.driver.find_element_by_class_name('prodTitle').text
        except Exception as e:
            print(e)
            return None
        
    def get_availability(self):
        self.driver.get(self.url)
        element = self.driver.find_element_by_class_name('megaButton')
        try:
            return element.text
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    print('Scraping...')
    gs = GSTracker(url)
    title = gs.get_title()
    availability = gs.get_availability()
    print(title)
    print(availability)
