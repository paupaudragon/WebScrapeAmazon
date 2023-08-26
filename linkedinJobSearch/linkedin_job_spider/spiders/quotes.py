import scrapy 

class LinkedinJobsSpider(scrapy.Spider):
    name = 'linkedin_jobs'

    api_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=software%2Bintern&location=United%2BStates&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&start='
    
    def start_requests(self):
        first_job_on_page=0 
        first_url = self.api_url + str(first_job_on_page)
        yield scrapy.Request(url=first_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})


    def parse_job(self, response):
        first_job_on_page = response.meta['first_job_on_page']

        job_item = {}
        jobs = response.css("li")

        nums_jobs_returned = len(jobs)
        print("-------Nums of Jobs returned-------")
        print(nums_jobs_returned)
        print("----------")

        for job in jobs: 
            job_item['job_title'] = job.css("h3::text").get(default='not-found').strip()
            job_item['job_detail_url'] = job.css(".base-card__full-link::attr(href)").get(default='not-found').strip()
            job_item['job_listed_time'] = job.css("time::text").get(default='not-found').strip()

            job_item['company_name'] = job.css("h4 a::text").get(default='not-found').strip()
            job_item['company_location'] = job.css(".job-search-card__location::text").get(default='not-found').strip()
            job_item['company_link'] = job.css("h4 a::attr(href)").get(default='not-found').strip()
            yield job_item
