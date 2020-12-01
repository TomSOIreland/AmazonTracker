import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from amazon_config import (
    get_web_driver_options,
    get_chrome_web_driver,
    set_ignore_certificate_error,
    set_browser_as_incognito,
    BASE_URL
)


class AmazonAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        options = get_web_driver_options()
        set_ignore_certificate_error(options)
        set_browser_as_incognito(options)
        self.driver = get_chrome_web_driver(options)

    def run(self):
        self.driver.get(self.base_url)
        info = self.get_info()
        time.sleep(1)
        self.driver.quit()
        return info

    def get_info(self):
        title = self.get_title()
        availability = self.get_availability()
        if title and availability:
            ps5_info = {
                'title': title,
                'availability': availability
            }
            return ps5_info
        
    def get_availability(self):
        try:
            return self.driver.find_element_by_id('availability').text
        except Exception as e:
            print(e)
            print('Couldn\'t find availability info')
            return None

    def get_title(self):
        try:
            return self.driver.find_element_by_id('productTitle').text
        except Exception as e:
            print(e)
            print('Couldn\'t find title')
            return None


if __name__ == '__main__':
    print('WORKING....')
    amazon = AmazonAPI(BASE_URL)
    data = amazon.run()
    print(data)


