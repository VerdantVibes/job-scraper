from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Firefox()
# driver.get("https://www.indeed.com/")

input_job_name = driver.find_element_by_xpath('//*[@id="text-input-what"]')
input_job_name.send_keys("data analyst")

input_location = driver.find_element_by_xpath('//*[@id="text-input-where"]')
input_location.send_keys("New York, NY")
time.sleep(5)
find_job = driver.find_element_by_xpath(
    "/html/body/div/div[2]/div[3]/div[1]/div/div/div/form/div[3]"
).click()

# Creates a dataframe
df = pd.DataFrame(
    {
        "Link": [""],
        "Job Title": [""],
        "Company": [""],
        "Location": [""],
        "Salary": [""],
        "Date": [""],
    }
)

while True:
    # Imports the HTML of the current page into python
    soup = BeautifulSoup(driver.page_source, "lxml")

    # Grabs the HTML of each posting
    postings = soup.find_all(
        "div", class_="jobsearch-SerpJobCard unifiedRow row result clickcard"
    )

    # grabs all the details for each posting and adds it as a row to the dataframe
    for post in postings:
        link = post.find("a", class_="jobtitle turnstileLink").get("href")
        link_full = "https://www.indeed.com/" + link
        name = post.find("h2", class_="title").text.strip()
        company = post.find("span", class_="company").text.strip()
        try:
            location = post.find(
                "div", class_="location accessible-contrast-color-location"
            ).text.strip()
        except:
            location = "N/A"
        try:
            salary = post.find("span", class_="salaryText").text.strip()
        except:
            salary = "N/A"
