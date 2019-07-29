from selenium import webdriver
import time 
import requests

count = 0
driver = webdriver.Firefox()

driver.get("https://selenium-python.readthedocs.io/locating-elements.html#locating-elements-by-tag-name")

print("The broken weblinks (HTTP status code: 404) inthe the given page are:")
links = driver.find_elements_by_tag_name('a')
for link in links:
    r = requests.head(link.get_attribute('href'))
    if(r.status_code == 404):
        print(link.get_attribute('href'))
        count = count+1

if count == 0:
    print("No broken Hyperlinks in the given webpage!")
    

driver.quit()
