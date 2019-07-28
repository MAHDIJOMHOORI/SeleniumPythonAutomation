from selenium import webdriver #Import a webdriver.
import time #To wait between commands.
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
em = browser.find_element_by_id("identifierId")
em.send_keys('ss.sakshisingh02@gmail.com')
em.send_keys(Keys.RETURN)
time.sleep(2)
passw = browser.find_element_by_name("password")
passw.send_keys("ishuaditya02")
passw.send_keys(Keys.RETURN)

#LOGIN SUCCESS
time.sleep(5)

comp = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div").click()

#COMPOSE SUCCESS

time.sleep(5)

to = browser.find_element_by_name("to")
to.send_keys('asaditya140@gmail.com')
time.sleep(1)

sub = browser.find_element_by_name('subjectbox')
sub.send_keys('HI')
time.sleep(1)

body = browser.find_element_by_xpath('//*[@id=":bt"]')
body.send_keys("hey addy!")
time.sleep(1)

body.send_keys(Keys.CONTROL + Keys.RETURN)

#MESSAGE SEND SUCCESS.

time.sleep(10)

browser.close()