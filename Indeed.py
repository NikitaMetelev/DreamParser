import time
import random
import pandas as pd
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

driver = uc.Chrome()
job_data = []
driver = uc.Chrome()
try:
    for page in (0, 10):

        driver.get(
            f'https://uk.indeed.com/jobs?q=data+analyst&l=United+Kingdom&sc=0kf%3Aattr%28DSQF7%29%3B&fromage=1&start={page}')
        time.sleep(random.uniform(8.5, 10.9))

        jobs = driver.find_elements(By.XPATH, '//div[@class= "css-1m4cuuf e37uo190"]')

        for job in jobs:
            job.location_once_scrolled_into_view
            job.click()
            time.sleep(random.uniform(4.6, 6.9))

            job_title = driver.find_element(By.XPATH,
                                            '//h2[@class="icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title is-embedded"]').text.strip()
            title = job_title.split('\n')
            location = driver.find_element(By.XPATH, '//div[@class="css-6z8o9s eu4oa1w0"]').text.strip()
            loc = location.split('\n')
            job_description = driver.find_element(By.XPATH,
                                                  '//div[@class="jobsearch-JobComponent-description css-158wk25 eu4oa1w0"]').text.strip()
            company = driver.find_element(By.XPATH, "//div[@class='jobsearch-CompanyInfoContainer']").find_element(
                By.XPATH, "//div[@data-company-name]").text

            data = {'Job_Title': title[0], 'Company': company, 'Location': loc, 'Job_description': job_description}
            job_data.append(data)
            print("[*] Saving")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
df = pd.DataFrame(job_data)
df.to_csv('data_analyst_vacancies')