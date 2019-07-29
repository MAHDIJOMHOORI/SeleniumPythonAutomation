from selenium import webdriver #Import a webdriver.
import time #To wait between commands.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By     #Locating Elements.
from selenium.webdriver.support.ui import WebDriverWait #For waiting.
from selenium.webdriver.support import expected_conditions as EC    #For waiting conditions to occur.

browser = webdriver.Firefox()

wait = WebDriverWait(browser,15)    #wait for max 15 seconds

browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

# em = browser.find_element_by_id("identifierId")
em = wait.until(EC.element_to_be_clickable((By.ID, 'identifierId')))    #As soon as the element is visible in DOM, execute the commands.
em.send_keys('testme7714@gmail.com')
time.sleep(1)
em.send_keys(Keys.RETURN)

# time.sleep(2)

# passw = browser.find_element_by_name("password")
passw = wait.until(EC.element_to_be_clickable((By.NAME,'password')))
passw.send_keys("Aditya123")
time.sleep(1)
passw.send_keys(Keys.RETURN)

# comp = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div").click()
comp = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div'))).click()

# to = browser.find_element_by_name("to")
to = wait.until(EC.element_to_be_clickable((By.NAME, 'to')))
to.send_keys('asaditya140@gmail.com')
time.sleep(1)

# sub = browser.find_element_by_name('subjectbox')
sub = wait.until(EC.element_to_be_clickable((By.NAME, 'subjectbox')))
sub.send_keys('HI')
time.sleep(1)

# body = browser.find_element_by_xpath('//*[@id=":97"]')
body = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":97"]')))
body.send_keys("hey addy!")
time.sleep(1)

body.send_keys(Keys.CONTROL + Keys.RETURN)

#MESSAGE SEND SUCCESS.

time.sleep(10)

browser.close()