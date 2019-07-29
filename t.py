from selenium import webdriver #Import a webdriver.
import time #To wait between commands.
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox() #New Driver for Firefox. The gekodriver is in PATH folder of python executable.
browser.get('https://www.google.com/') #Open this website.
x = browser.find_element_by_name("q") #Find search bar.
x.send_keys("gmail")        #Send "gmail" as the search criteria.
x.send_keys(Keys.RETURN)    #Emulates pressing of enter key after we type the search keyword.

browser.maximize_window()
browser.refresh()

time.sleep(4) #Wait for 4 seconds.
browser.quit() #To close the connection.
