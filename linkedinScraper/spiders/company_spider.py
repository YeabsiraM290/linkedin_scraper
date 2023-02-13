from linkedinScraper.models.linkedin_company_model import LinkedinCompanyItem
from scrapy_playwright.page import PageMethod

import scrapy


class LinkedinCompanySpider(scrapy.Spider):
    name = "company_spider"

    def start_requests(self):
        url = "https://www.linkedin.com/login"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                errback=self.errback,
                playwright_page_methods=[
                    PageMethod(
                        "evaluate",
                        "window.scrollBy(0, document.body.scrollHeight)",
                    ),
                    PageMethod(
                        "wait_for_selector", "div.quote:nth-child(11)"
                    ),  # 10 per page
                ],
            ),
        )

    async def parse(self, response):
        return {"url": response.url}

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
