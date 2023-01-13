class Company:

    def __init__(self, name: str, location: str, logo: str):

        self.name = name
        self.location = location
        self.logo = logo

    def print(self):
        print("company name: " + self.name)
        print("comapny location: " + self.location)
        print("company logo: " + self.logo)


# class Job:

#     def __int__(self, job_title: str,):
#         pass


class JobPost():

    def __init__(self, job_title: str, company: Company, posted_date: str, description: str, extra_info: str,
                 applicant_amount: str, seniority_level: str, job_function: str, industries: str, employment_type: str, job_url: str):

        self.job_title = job_title
        self.company = company
        self.posted_date = posted_date
        self.description = description
        self.extra_info = extra_info
        self.applicant_amount = applicant_amount
        self.seniority_level = seniority_level
        self.job_function = job_function
        self.industries = industries
        self.employmet_type = employment_type
        self.job_url = job_url

    def print(self):
        print("*" * 40)
        print("job_title: " + self.job_title)
        self.company.print()
        print("posted_date: " + self.posted_date)
        print("description: " + self.description)
        print("extra_info: " + self.extra_info)
        print("applicant_amount: " + self.applicant_amount)
        print("seniority_level: " + self.seniority_level)
        print("job_function: " + self.job_function)
        print("industries: " + self.industries)
        print("employment_type: " + self.employmet_type)
        print("job_url: " + self.job_url)
