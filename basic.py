from selenium.webdriver.common.proxy import Proxy, ProxyType
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import csv
import os
import time
import undetected_chromedriver as uc

links = []
## Set up Selenium and Chrome options
s = Service(executable_path="D:/programing_stuff/chrome_drivers/chromedriver_win32/chromedriver.exe")

driver = uc.Chrome(service=s)

time.sleep(1)
driver.get("https://www.instagram.com/")
time.sleep(25)

username = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input""")
username.send_keys("ganni_studio")

password = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input""")
password.send_keys("7_june2006%")
password.send_keys(Keys.ENTER)


time.sleep(20)


while len(links) < 173:
    all_posts = driver.find_elements(By.XPATH, '//a[contains(@href,"/reel/")]')

    for post in all_posts:
        link = post.get_attribute('href')
        if link not in links:
            links.append(link)
            print(link)
        if len(links) >= 173:
            break
        

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

csv_file = "D:/programing_stuff/AI stuff/instabot-selenium/data/post.csv"
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the links as separate rows in the CSV file (without sorting)
    for link in links:
        writer.writerow([link])

