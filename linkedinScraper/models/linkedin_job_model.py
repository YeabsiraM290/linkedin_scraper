from linkedinScraper.models.linkedin_company_model import LinkedinCompany


class LinkedinJobPost:
    def __init__(
        self,
        job_title: str,
        company: LinkedinCompany,
        date_posted: str,
        description: str,
        application_info: str,
        seniority_level: str,
        job_function: str,
        industries: str,
        employment_type: str,
        job_url: str,
    ) -> None:
        self.job_title = job_title
        self.company = company
        self.date_posted = date_posted
        self.description = description
        self.application_info = application_info
        self.seniority_level = seniority_level
        self.job_function = job_function
        self.industries = industries
        self.employmet_type = employment_type
        self.job_url = job_url

    def print(self) -> None:
        print("*" * 100 + "\n")
        print(f"Job title: {self.job_title}")
        print(f"Posted on: {self.date_posted}")
        print(f"Company : {self.company.name}")
        print(f"Description: {self.description}")
        print(f"Applicantion Information: {self.application_info}")
        print(f"Seniority Level: {self.seniority_level}")
        print(f"Job Function: {self.job_function}")
        print(f"Industries: {self.industries}")
        print(f"Employment Type: {self.employmet_type}")
        print(f"Job URL: {self.job_url}")
        print("*" * 100 + "\n")
