# ⭐ Indeed Job Scraper for Data Analysts in New York, NY

Welcome to the **Indeed Job Scraper**! This Python project helps you automatically scrape job postings for data analyst positions in New York, NY from Indeed.com and sends the results via email. 📧

## 🌟 Features

- 🚀 **Automated Scraping:** Scrape job listings from Indeed.
- 📊 **Structured Data:** Extract crucial details like job title, company, location, salary, and date posted.
- 💾 **Data Storage:** Save the extracted data in a CSV file.
- 📬 **Email Notification:** Send an email with the CSV file as an attachment.

## 📝 Prerequisites

Make sure you have the following dependencies installed:

- `selenium`
- `beautifulsoup4`
- `pandas`
- `lxml`
- `smtplib`

You can install these dependencies using pip:

```sh
pip install selenium beautifulsoup4 pandas lxml
```
## ⚙️ Setup
### 1. Geckodriver
Download and install Geckodriver to enable Selenium to work with Firefox. [Geckodriver Downloads](https://github.com/mozilla/geckodriver/releases).

### 2. Email Configuration
Make sure you have access to a valid email account for sending the scraped data through SMTP.

## 📌 Usage
#### **1. Run the Script:**

Save the provided code to a file (e.g., `main.py`) and execute it:

    python main.py
#### **2. Email Configuration:**

Replace the sender, receiver, and email credentials with your actual email account details in the script.

    sender = 'your_email@gmail.com'
    receiver = 'receiver_email@gmail.com'
    password = 'your_email_password'
#### **3. CSV File Path:**

Adjust the file paths in the script accordingly:

    df.to_csv('path/to/your/directory/indeed_scraped_data.csv')

    # Attachment file path
    part.set_payload(open('path/to/your/directory/indeed_scraped_data.csv', 'rb').read())
## 🚀 Quick Overview
The script does the following:

1. Uses Selenium to navigate to Indeed.com and perform a search for data analyst jobs in New York, NY.
2. Extracts job details using BeautifulSoup.
3. Organizes the extracted data into a pandas DataFrame and saves it as a CSV file.
4. Sends the CSV file via email using smtplib.

## 📚 Additional Notes
- Ensure Geckodriver is in your system's PATH or update the script with the correct path to Geckodriver.
- Make sure your email account settings allow less secure apps or generate an app-specific password if using two-factor authentication.

Thank you for using the **Indeed Job Scraper**! 
#### Happy scraping! 🎉

