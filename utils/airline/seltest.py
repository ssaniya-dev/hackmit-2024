# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# # Provide the full path to chromedriver
# service = Service(executable_path='/Users/neilteje/Desktop/chromedriver.exe')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

# # Test by opening Google
# driver.get('https://www.google.com')

# # Print the title of the page
# print(driver.title)

# # Close the browser
# driver.quit()

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.quit()
