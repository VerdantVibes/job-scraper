from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Firefox()
driver.get("https://www.indeed.com/")

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
