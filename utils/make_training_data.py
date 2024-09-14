import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open the website
driver.get("https://www.example.com")



#If there is no such folder, the script will create one automatically
folder_location = r'./irs_pdfs'
if not os.path.exists(folder_location):os.mkdir(folder_location)


for i in range(15):
    soup = BeautifulSoup(requests.get(f"https://www.irs.gov/forms-instructions-and-publications?find=&items_per_page=200&page={i}").text, "html.parser")  
    for link in soup.select("a[href$='.pdf']"):
        if link["href"].split("/")[-1][0] != "f":
            continue
        print(link)
        #Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            print(filename)
            f.write(requests.get(urljoin("https://www.irs.gov",link['href'])).content)