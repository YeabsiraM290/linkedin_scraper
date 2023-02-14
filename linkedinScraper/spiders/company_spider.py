## spider.py
from ast import arg
import scrapy
from time import sleep

from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains



def login(driver):
    username_field = driver.find_element_by_id("username")

    username_field.send_keys("yeabsira290@gmail.com")

    password_field = driver.find_element_by_id("password")
    password_field.send_keys("hydra2019")

    button = driver.find_element_by_css_selector(
        "button.btn__primary--large.from__button--floating"
    )
    ActionChains(driver).click(button).perform()


class LinkedinCompanySpider(scrapy.Spider):
    name = "company_spider"

    def start_requests(self):
        url = "https://www.linkedin.com/login"
        yield SeleniumRequest(
            url=url,
            callback=self.parse,
            wait_time=0,
            wait_until=login,
        )
        sleep(30)
        

    def parse(self, response):
        return
        # page = response.meta["playwright_page"]

        # page.fill("#username", "yeabsira290@gmail.com")
        # page.fill("#password", "hydra2019")

        # page.click("button[type='submit']")

        # page.wait_for_selector(".oe_database_information")
