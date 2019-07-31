from selenium import webdriver 
import time 
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import json

query = str(input("Enter the search Keyword:  "))
driver = webdriver.Firefox()        # Open the browser window.
searchtext = query.replace(" ","%20")   # Replace the spaces the query with %20.
url = "https://www.google.co.in/search?q="+searchtext+"&source=lnms&tbm=isch"   # Open this link to get redirected to Google Images.
driver.get(url)
driver.maximize_window()        # Maximize the browser window.

time.sleep(5)       # Wait for 5 seconds.

links = driver.find_elements_by_tag_name('img')     # Find all the elements in the webpage having "img" tag.

# The code below is to find from where to start donwloading the "top" 10 images.
x = query.split()
if len(x) > 2:
    top10links = links[2:]      # Single word searches generally do not have the tabs containing images.
else:
    top10links = links[31:]    # First 31 (0-30) pictures are of small tabs that appear just below the search bar. (Happens mostly in searches with more than 1 word)

top10 = list()      # Create an empty list.
for link in top10links:
    top10.append(link.get_attribute('src'))     # Append the "src" attribute to the list.
directory_name = query.replace(" ","_")     # Replace spaces with "_" to form the directory name, all the images will be stored under this directory.
count = 0       # Keeps count of images being downloaded.
for i in top10:
    try:
        count = count+1
        download_directory = os.path.join("Images/",directory_name)     
        if not os.path.exists(download_directory):
            os.mkdir(download_directory)        # Create a directory if it does not exist.
        fullfilename = os.path.join(download_directory,str(count)+".png")       # Name the images and add them to the directory.
        urllib.request.urlretrieve(i,fullfilename)      # Retrieve the image given by the 'src' link of the image.
    except:
        count = count-1
        pass
    if count == 10:     # Stop after 10 images are downloaded.
        break

time.sleep(5)       # Wait for 5 seconds.

driver.close()       # Quit browser window.

