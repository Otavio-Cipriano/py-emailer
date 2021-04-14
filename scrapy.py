from bs4 import BeautifulSoup
import requests
from datetime import datetime
from job import Job

def find_jobs():
    html_text = requests.get('https://github.com/frontendbr/vagas/issues?q=is%3Aissue+is%3Aopen+label%3A+%22Junior%22').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.findAll('div', class_ ='js-issue-row')
    all_jobs = []
    for job in jobs:
        now = datetime.now()
        month = now.strftime("%B")[:3]
        published_date = job.find('relative-time').text

        if month in published_date:
            job_title = job.find('a', class_ ='h4').text
            tags = job.find('span', class_='labels').text.strip().replace('\n', ' - ')
            more_details = 'https://github.com/' + job.find('a', class_='h4')['href']

            one_job = Job(job_title, tags, more_details, published_date)
            all_jobs.append(one_job)

            # print(all_jobs[0].job_title)
            # print(f"Tags: {tags}")
            # print(f"Published: {published_date}")
            # print(f"More details: {more_details}")
            # print('\n')

    return all_jobs