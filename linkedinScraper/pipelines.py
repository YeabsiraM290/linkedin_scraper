# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


from linkedinScraper.settings import XLSX_PATH


class LinkedinscraperPipeline:
    def process_item(self, item, spider):
        return item


FIELDNAMES = [
    "Job Title",
    "Date",
    "Company Name",
    "Company Location",
    "Company URL",
    "Seniority Level",
    "Employment Type",
    "Job Function",
    "Industries",
]


class XLSXPipeline(object):
    wb = None
    ws = None

    def open_spider(self, spider):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active

        self.ws.append(FIELDNAMES)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        self.ws.append(
            [
                adapter.get("job_title"),
                adapter.get("date"),
                adapter.get("company_name"),
                adapter.get("company_location"),
                adapter.get("company_url"),
                adapter.get("seniority_level"),
                adapter.get("employment_type"),
                adapter.get("job_function"),
                adapter.get("industries"),
            ]
        )

        return item

    def close_spider(self, spider):
        self.wb.save(XLSX_PATH)


# date
# company_name
# company_location
# company_url
# seniority_level
# employment_type
# job_function
# industries
