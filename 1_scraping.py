import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

jobs = []

for page in range(0, 5):
    url = f"https://in.indeed.com/jobs?q=data+analyst&start={page*10}"
    driver.get(url)
    time.sleep(4)

    cards = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")

    for card in cards:
        try:
            title = card.find_element(By.CSS_SELECTOR, "h2 span").text
            company = card.find_element(By.CLASS_NAME, "companyName").text
            location = card.find_element(By.CLASS_NAME, "companyLocation").text

            try:
                salary = card.find_element(By.CLASS_NAME, "salary-snippet").text
            except:
                salary = ""

            jobs.append([title, company, location, salary])
        except:
            pass

driver.quit()

df = pd.DataFrame(jobs, columns=["job_title", "company", "location", "salary"])

df.to_csv("../data/raw_jobs.csv", index=False)

print("CSV file created with data!")
