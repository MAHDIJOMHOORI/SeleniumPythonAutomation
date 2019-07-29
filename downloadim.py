from selenium import webdriver 
import time 
from selenium.webdriver.common.keys import Keys
import urllib

driver = webdriver.Firefox()

driver.get('https://www.google.com/imghp?hl=en')    #Get google images.
query = driver.find_element_by_name("q")
query.send_keys("call of duty")
query.send_keys(Keys.RETURN)

"""
links = list()
for i in range (10):
    link = driver.find_element_by_tag_name('img')
    links.append(link.get_attribute('src'))

"""

time.sleep(5)

links = driver.find_elements_by_tag_name('img')

top10links = links[31:41]    #First 31 (0-30) pictures are of small tabs that appear just below the search bar.

top10 = list()
for link in top10links:
    top10.append(link.get_attribute('src'))

print(len(top10))
driver.get(top10[9])


#FOUND THE TOP 10 IMAGE LINKS AND STORED IT INTO "top10" now just use the URLLIB to donwload.