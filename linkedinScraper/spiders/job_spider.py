from email.policy import default
import scrapy


class LinkedinJobSpider(scrapy.Spider):
    name = "job_scraper"

    start_urls = [
        "https://www.linkedin.com/jobs/search?keywords=Information%20Technology%20Specialist"
    ]

    def parse(self, response):
        job_page_links = response.css(
            "ul.jobs-search__results-list li a.base-card__full-link"
        )
        yield from response.follow_all(job_page_links, self.parse_job)

        # pagination_links = response.css("li.next a")
        # yield from response.follow_all(pagination_links, self.parse)

    def parse_job(self, response):
        try:

            def extract_with_css(query: str) -> str:
                return response.css(query + "::text").get(default="").strip()

            def extrat_link_address(query: str) -> str:
                return response.css(query).attrib["href"]

            def extrat_img_src(query: str) -> str:
                return response.xpath("//img/@src").extract()

            job_criteria = response.css(
                "span.description__job-criteria-text.description__job-criteria-text--criteria::text"
            ).getall()

            yield {
                "jobs": [
                    {
                        "job_title": extract_with_css("h1.top-card-layout__title"),
                        "date": extract_with_css(
                            "span.posted-time-ago__text.topcard__flavor--metadata"
                        ),
                        "company_name": extract_with_css(
                            "a.topcard__org-name-link.topcard__flavor--black-link"
                        ),
                        "company_location": extract_with_css(
                            "span.topcard__flavor.topcard__flavor--bullet"
                        ),
                        "company_logo": extrat_img_src(
                            "img.artdeco-entity-image.artdeco-entity-image--square-4.lazy-loaded"
                        ),
                        "company_url": extrat_link_address(
                            "a.topcard__org-name-link.topcard__flavor--black-link"
                        ),
                        "seniority_level": job_criteria[0].strip(),
                        "employment_type": job_criteria[1].strip(),
                        "job_function": job_criteria[2].strip(),
                        "industries": job_criteria[3].strip(),
                        "extra_info": extract_with_css(
                            "span.num-applicants__caption topcard__flavor--metadata.topcard__flavor--bullet"
                        ),
                        "job_description": extract_with_css(
                            "div.show-more-less-html__markup"
                        ),
                    }
                ]
            }
        except:
            pass
