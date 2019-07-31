from selenium import webdriver
import time 
import requests

input_url = str(input("Enter the website URL: "))

count = 0       # Keeps count of broken hyperlinks in website.
driver = webdriver.Firefox()    
driver.maximize_window()    # Maximizes the browser window.

# Example websites to test the code.
# No error: https://www.google.com/
# With errors: https://selenium-python.readthedocs.io/locating-elements.html

driver.get(input_url)       # Open the website.

links = driver.find_elements_by_tag_name('a')       # Find all elements that have anchor tags.
print("Total number of Hyperlinks found in webpage are: ",len(links))       # List total number of hyperlinks in the website.

for link in links:      # Run loop for all links.
    r = requests.get(link.get_attribute('href'))     # Send a "GET" request for each of the hyperlinks. (Hyperlink can be found using the 'href' attribute)
    if(r.status_code == 404):       # 404 indicates that the hyperlink is broken.
        count = count+1
        if(count == 1):
            print("The broken hyperlink(s) are:")
        print(link.get_attribute('href'))       # Print the broken hyperlink.
        

if count == 0:
    print("No broken Hyperlinks in the given webpage!")
else:
    print("The number of broken hyperlinks (HTTP status code: 404) in the given webpage are: ",count)
    
driver.close()   # Close the browser window.
