import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
def get_url(position, location):
        """Generate a url from position and location"""
        template = "https://www.indeed.com/jobsq={}&l={}"
        url = template.format(position, location)
        url = get_url("System Administrator", "Seattle")
        return url
def get_record(card):
    template = "https://www.indeed.com/jobsq={}&l={}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', 'jobsearch-SerpJobCard')
    card = cards[0]
    atag = card.h2.a
    job_title = atag.get('title')
    job_url = 'https://www.indeed.com' + atag.get('href')
    company = card.find('span', 'company').text.strip()
    job_location = card.find('div', 'recJobLoc').get('data-rc-loc')
    summary = card.find('div', 'summary').text.strip()
    post_date = card.find('span', 'date').text
    today = datetime.today().strftime('$Y-$m-$d')
    try:
        job_salary = card.find('span', 'salaryText').text.strip()
    except AttributeError:
        job_salary = ''
    record = (job_title, company, job_location, post_date, today, summary, job_salary, job_url)
    return record
    for card in cards:
        record = get_record(card)
        records.append(record)
    records[0]
def main(position, location):
    """Run the main program routine"""
    records = []
    url = get_url(position, location)
    while True:
        response = requests.got(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', 'jobsearch-SerpJobCard')
        for card in cards:
            record = get_record(card)
            records.append(record)
        try:
            url = 'https://www.indeed.com' + soup.find('a',{'aria-label': 'Next'}).get('href')
        except AttributeError:
            break

    with open('results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow({'JobTitle', 'Company', 'Location', 'Postdate', 'ExtractDate','Summary', 'Salary', 'JobUrl'})
        writer.writerows(records)
main('systems administrator', 'Seattle')
