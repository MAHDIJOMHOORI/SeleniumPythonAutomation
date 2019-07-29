from selenium import webdriver #Import a webdriver.
import time #To wait between commands.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By     #Locating Elements.
from selenium.webdriver.support.ui import WebDriverWait #For waiting.
from selenium.webdriver.support import expected_conditions as EC    #For waiting conditions to occur.

"""
200 = working
404 = not found
403 = forbidden
302 = redirect
303 = redirect after http post performed.
"""

driver = webdriver.Firefox()

wait = WebDriverWait(driver,15)

driver.get("https://selenium-python.readthedocs.io/locating-elements.html#locating-elements-by-tag-name")

link = driver.find_element_by_tag_name('a')
print(type(link))
print(link)
time.sleep(5)
driver.quit()
