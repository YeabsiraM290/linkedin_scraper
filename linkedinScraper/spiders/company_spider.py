from time import sleep
import scrapy
from scrapy.selector import Selector

from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def login(driver):
    username = "yeabsira290@gmail.com"
    password = "hydra2019"

    sleep(3)
    username_field = driver.find_element_by_id("username")
    username_field.send_keys(username)

    sleep(1)
    password_field = driver.find_element_by_id("password")
    password_field.send_keys(password)

    sleep(2)
    button = driver.find_element_by_css_selector(
        "button.btn__primary--large.from__button--floating"
    )
    ActionChains(driver).click(button).perform()


def search(driver, page_no):
    sleep(5)
    driver.get(
        f"https://www.linkedin.com/search/results/COMPANIES/?companyHqGeo=%5B%22101620260%22%5D&keywords=it%20services%20and%20it%20consulting&page={page_no}"
    )

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "reusable-search__entity-result-list")
        )
    )
    return driver.page_source


class LinkedinCompanySpider(scrapy.Spider):
    name = "company_spider"

    def start_requests(self):
        url = "http://quotes.toscrape.com"
        yield scrapy.Request(url=url, callback=self.parse_company_urls)

    def parse_company_urls(self, response):
        # options = Options()
        # options.add_argument("window-size=1366,768")
        #chrome_options=options,
        driver = webdriver.Chrome(
            
            executable_path="/home/yeabsira/Programs/chrome_driver/chromedriver",
            keep_alive=True,
        )
        driver.get("https://www.linkedin.com/login")
        login(driver)
        driver.implicitly_wait(10)

        urls = []
        url = []

        driver.get(
            "https://www.linkedin.com/search/results/COMPANIES/?companyHqGeo=%5B%22101620260%22%5D&keywords=it%20services%20and%20it%20consulting"
        )

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "reusable-search__entity-result-list")
            )
        )

        # last_page_num = driver.find_element_by_css_selector(
        #     "ul.artdeco-pagination__pages.artdeco-pagination__pages--number span"
        # ).text

        # element = WebDriverWait(driver, 60).until(
        #     EC.presence_of_element_located(
        #         (By.CLASS_NAME, "artdeco-pagination__pages artdeco-pagination__pages--number")
        #     )
        # )

        sel = Selector(text=driver.page_source)
        url.append(sel.css("ul.reusable-search__entity-result-list li"))

        # last_page_num = Selector(pagination).css("button span ::text").getall()
        # print("*" * 100)
        # print(last_page_num)
        # [-1].css("span::text")

        for i in range(2, 57):
            sel = Selector(text=search(driver, i))

            for link in sel.css("ul.reusable-search__entity-result-list li"):
                for lin in link:
                    yield {
                        "urls": urls.append(lin.css("a.app-aware-link").attrib["href"])
                    }

    # for i, url in enumerate(urls):
