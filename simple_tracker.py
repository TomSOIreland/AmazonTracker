import time

from selenium.webdriver.common.keys import Keys

from amazon_config import (
    get_web_driver_options,
    get_chrome_web_driver,
    set_automation_as_head_less,
    set_ignore_certificate_error,
    set_browser_as_incognito,
    NAME,
    CURRENCY,
    FILTERS,
    BASE_URL,
    DIRECTORY
)

class GenerateReport():
    def __init__(self):
        pass


class AmazonAPI:
    def __init__(self, search_term, filters, base_url, currency):
        self.base_url = base_url
        self.search_term = search_term
        options = get_web_driver_options()
        set_ignore_certificate_error(options)
        set_browser_as_incognito(options)
        self.driver = get_chrome_web_driver(options)
        self.currency = currency
        self.price_filter = f"&rh=p_36%3A{filters['min']}-{filters['max']}"

    def run(self):
        print('Starting Script.....')
        print(f"Looking for {self.search_term} products....")
        links = self.get_product_links()
        time.sleep(5)
        self.driver.quit()

    def get_product_links(self):
        self.driver.get(self.base_url)
        element = self.driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
        element.send_keys(self.search_term)
        element.send_keys(Keys.ENTER)
        time.sleep(2)  # wait to load
        self.driver.get(f'{self.driver.current_url}{self.price_filter}')


if __name__ == '__main__':
    print('WORKS')
    amazon = AmazonAPI(NAME, FILTERS, BASE_URL, CURRENCY)
    amazon.run()
