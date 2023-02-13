from scrapy import Item, Field


class LinkedinCompanyItem(Item):
    name = Field()
    website = Field()
    head_quarters = Field()
    logo = Field()
    phone_no = Field()
    email = Field()
    overview = Field()
    company_size = Field()
    founded = Field()
    specialties = Field()
    industry = Field()
