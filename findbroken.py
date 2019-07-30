from selenium import webdriver
import time 
import requests

count = 0
driver = webdriver.Firefox()

# Example websites to test the code.
# No error: https://www.google.com/
# With errors: https://selenium-python.readthedocs.io/locating-elements.html

driver.get("https://selenium-python.readthedocs.io/locating-elements.html")

links = driver.find_elements_by_tag_name('a')
print("Total number of Hyperlinks found in webpage are: ",len(links))

for link in links:
    r = requests.head(link.get_attribute('href'), allow_redirects=True)
    if(r.status_code >= 400):
        print(link.get_attribute('href'))
        count = count+1

if count == 0:
    print("No broken Hyperlinks in the given webpage!")
else:
    print("The broken hyperlinks (HTTP status code: 404) in the given webpage are: ",count)
    
driver.quit()
