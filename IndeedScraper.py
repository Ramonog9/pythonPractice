from bs4 import BeautifulSoup
import pandas as pd
import time
import requests

#function to scrape indeed jobs
def get_indeed_jobs(query="Cloud Engineer", Location =''):
    base_url = "https://www.indeed.com/jobs"
    params = {
        'q': query,
        'l': Location,
        'start': 0,
        'fromage': 1,  # jobs from last 24 hours
        'sort': 'date'
    }
    #set header to seem like a real person browsing site
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    #add a list to store job details
    list_jobs = []
    #loop through first 3 pages
    for page in range(0,3):
        print(f"Scraping page {page + 1}")
        params['start'] = page * 10  # Listings per page
        response = requests.get(base_url, params=params, headers=headers)
        #Check if request was successful to either stop or continue
        if response.status_code != 200:
            print(f"Failed to retrieve page {page + 1}")
            break
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("div", class_="job_seen_beacon")

            for job in results:
                title = job.find("h2", class_="jobTitle")
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                summary = job.find("div", class_="job-snippet")
                date = job.find("span", class_="date")
                salary = job.find("div", class_="salary-snippet")
                job_url = job.find("a", class_="jcs-JobTitle")['href'] if job.find("a", class_="jcs-JobTitle") else None

                list_jobs.append({
                    'Title': title.get_text(strip=True) if title else None,
                    'Company': company.get_text(strip=True) if company else None,
                    'Location': location.get_text(strip=True) if location else None,
                    'Summary': summary.get_text(strip=True) if summary else None,
                    'Date Posted': date.get_text(strip=True) if date else None,
                    'Salary': salary.get_text(strip=True) if salary else 'Not Provided',
                    'Job URL': f"https://www.indeed.com{job_url}" if job_url else None
                })

        time.sleep(1)  #Add delay to avoid overwhelming server

    return pd.DataFrame(list_jobs)

if __name__ == "__main__":
    jobs = get_indeed_jobs("Cloud Engineer", "")
    print(jobs)
    jobs.to_csv("indeed_jobs.csv", index=False) # Save to CSV
    print(f"Saved {len(jobs)} jobs to indeed_jobs.csv")


