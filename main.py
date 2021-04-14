from scrapy import find_jobs
from time import sleep
from datetime import datetime
from scrapy import find_jobs
from emailer import send_email

if __name__ == '__main__':
    while True:
        time_to_wait = '21:00'
        current_time =str(datetime.utcnow().time())[:5]
        message = ''
        
        if current_time == '05:24':

            jobs = find_jobs()
        

            for job in jobs:
                job_string = f"Job Title: {job.job_title}\nTags: {job.tags}\nPublished: {job.published_date}\nMore details: {job.more_details}\n\n\n"
                message+=job_string 
        
            send_email(message)
            print(f'Waiting to {time_to_wait}...')
            sleep(60 * 60 * 24)