from selenium import webdriver 
import time 
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import json

st = str(input("Enter the search Keyword:  "))
driver = webdriver.Firefox()
searchtext = st.replace(" ","%20")
url = "https://www.google.co.in/search?q="+searchtext+"&source=lnms&tbm=isch"
driver.get(url)

time.sleep(5)

links = driver.find_elements_by_tag_name('img')

x = st.split()
if len(x) > 2:
    top10links = links[2:]      #Single word searches generally do not have the tabs containing images.
else:
    top10links = links[31:]    #First 31 (0-30) pictures are of small tabs that appear just below the search bar. (Happens mostly in searches with more than 1 word)

top10 = list()
for link in top10links:
    top10.append(link.get_attribute('src'))
imname = st.replace(" ","_")
ff = 0
for i in top10:
    try:
        ff = ff+1
        fz = os.path.join("Images/",imname)
        if not os.path.exists(fz):
            os.mkdir(fz)
        fullfilename = os.path.join(fz,str(ff)+".png")
        urllib.request.urlretrieve(i,fullfilename)
    except:
        ff = ff-1
        pass
    if ff == 10:
        break
time.sleep(5)
driver.quit()

