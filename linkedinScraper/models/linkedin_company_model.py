from scrapy import Item, Field


class LinkedinCompanyItem(Item):
    name = Field()
    location = Field()
    logo = Field()
