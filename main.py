from bs4 import BeautifulSoup

from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse

from models import Company, JobPost


def open_url(url, header):
    try:
        req = Request(
            url,
            data=None,
            headers=header

        )
        html_content = urlopen(req)
        return html_content

    except HTTPError as e:
        print(e)
        return None

    except URLError as e:
        print('The server could not be found!')
        return None


def get_results(search_result):

    try:
        bs = BeautifulSoup(search_result.read(), 'html.parser')
        data = []
        results = bs.find(
            'ul', {'class': 'jobs-search__results-list'}).find_all('li')

        for result in results:

            # job attributes

            # title
            job_title = result.find(
                'h3', {'class': 'base-search-card__title'}).get_text()

            # date in d-m-y fromat
            posted_date = result.find(
                'time', {'class', 'job-search-card__listdate'}).attrs['datetime']

            # date in text format (1 week ago,....)
            posted_date_text_representation = result.find(
                'time', {'class', 'job-search-card__listdate'}).get_text()

            # extra information about the job (Be an early applicant)
            extra_info = ""

            # check in job have extra info
            try:
                extra_info = result.find('div', {'class': 'job-search-card__benefits'}).find(
                    'span', {'class': 'result-benefits__text'}).get_text()
            except AttributeError as e:
                extra_info = ""

            # job post linkedin url
            job_url = result.find(
                'a', {'class': 'base-card__full-link'}).attrs['href']

            # company attribute
            name = result.find(
                'h4', {'class': 'base-search-card__subtitle'}).find('a').get_text()
            location = result.find('div', {'class': 'base-search-card__metadata'}).find(
                'span', {'class': 'job-search-card__location'}).get_text()
            # logo = result.find(
            #     'div', {'class', 'search-entity-media'}).find('img').attrs['src']

            logo = ""

            more_job_info = get_job_info(job_url)

            description = more_job_info["description"]
            seniority_level = more_job_info["seniority_level"]
            job_function = more_job_info["job_function"]
            industries = more_job_info["industries"]
            employment_type = more_job_info["employment_type"]
            applicant_amount = ""

            # create company object
            company = Company(name=name, location=location, logo=logo)

            # create job post object
            job_post = JobPost(job_title=job_title, company=company, posted_date=posted_date, description=description, extra_info=extra_info, applicant_amount=applicant_amount,
                               seniority_level=seniority_level, job_function=job_function, industries=industries, employment_type=employment_type, job_url=job_url)
            job_post.print()
            data.append(job_post)

        return data

    except AttributeError as e:
        return None


def get_job_info(url):
    header = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"}
    job_info = open_url(url, header)

    if (job_info):
        try:
            bs = BeautifulSoup(job_info.read(), 'html.parser')
            job_result = bs.find(
                'div', {'class': 'decorated-job-posting__details'})

            descriprion = job_result.find('div', {'class': 'description__text description__text--rich'}).find(
                'section', {'class': 'show-more-less-html show-more-less-html--more'}).get_text()

            criterias = job_result.find(
                'ul', {'class': 'description__job-criteria-list'}).find_all('li')

            seniority_level = criterias[0].find('span').get_text()
            employment_type = criterias[1].find('span').get_text()
            job_function = criterias[2].find('span').get_text()
            industries = criterias[3].find('span').get_text()

            return {
                "description": descriprion,
                "seniority_level": seniority_level,
                "job_function": job_function,
                "industries": industries,
                "employment_type": employment_type}

        except AttributeError as e:
            return {
                "description": "",
                "seniority_level": "",
                "job_function": "",
                "industries": "",
                "employment_type": ""}

    else:
        return {
            "description": "",
            "seniority_level": "",
            "job_function": "",
            "industries": "",
            "employment_type": ""}


url = "https://www.linkedin.com/jobs/search?keywords=Information%20Technology%20Specialist"
header = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"}
html = open_url(url, header)

if html:
    get_results(html)
