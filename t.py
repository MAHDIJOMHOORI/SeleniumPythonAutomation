from selenium import webdriver #Import a webdriver.
import time #To wait between commands.
from selenium.webdriver.common.keys import Keys
"""
browser = webdriver.Firefox() #New Driver for Firefox. The gekodriver is in PATH folder of python executable.
browser.get('https://www.google.com/') #Open this website.
x = browser.find_element_by_name("q") #Find search bar.
x.send_keys("gmail")        #Send "gmail" as the search criteria.
x.send_keys(Keys.RETURN)    #Emulates pressing of enter key after we type the search keyword.

browser.maximize_window()
browser.refresh()

time.sleep(4) #Wait for 4 seconds.
browser.quit() #To close the connection.
"""
import re
x = "https://www.google.com/url?q=https%3A%2F%2Fwww.facebook.com%2Fnot&sa=D&sntz=1&usg=AFQjCNEQN9GNd5XCxtLuKhYYnZ3F48UKbQ"
z = x.split("=")
print(z[1])
new = z[1]
n = new[:-3]
sn = str(n)
ss = sn.replace("%2F","/").replace("%3A",":")
print(ss)
# sz = ss.replace("%3A",":")
# print(sz)
browser = webdriver.Firefox() #New Driver for Firefox. The gekodriver is in PATH folder of python executable.
browser.get(ss) #Open this website.
# new = re.findall(r'\S*q',x)