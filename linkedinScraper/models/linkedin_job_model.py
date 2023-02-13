from scrapy import Item, Field

class LinkedinJobItem(Item):
    job_title = Field()
    date = Field()
    company_name = Field()
    company_location = Field()
    company_url = Field()
    seniority_level = Field()
    employment_type = Field()
    job_function = Field()
    industries = Field()