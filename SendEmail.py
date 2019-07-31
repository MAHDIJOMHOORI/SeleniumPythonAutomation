from selenium import webdriver      # Import a webdriver.
import time     # To wait between commands.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By     # Locating Elements.
from selenium.webdriver.support.ui import WebDriverWait     
from selenium.webdriver.support import expected_conditions as EC  

def login():
    login_em = wait.until(EC.element_to_be_clickable((By.ID, 'identifierId')))    # As soon as the element is visible in DOM, execute the commands.
    login_em.send_keys('testme7714@gmail.com')      # Login email ID.
    time.sleep(1)
    login_em.send_keys(Keys.RETURN)         # Emulates pressing of "Enter" key.

    login_pass = wait.until(EC.element_to_be_clickable((By.NAME,'password')))
    login_pass.send_keys("Aditya123")       # Login password.
    time.sleep(1)
    login_pass.send_keys(Keys.RETURN)       # Emulates pressing of "Enter" key.

to_em = str(input("Enter the Email ID of reciever: "))
to_sub = str(input("Enter the subject: "))
to_body = str(input("Enter the body of message: "))

browser = webdriver.Firefox()
wait = WebDriverWait(browser,15)    #wait for max 15 seconds

browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')    # Get Gmail signin page.
browser.maximize_window()       # Maximize the browser window.

login()     # Use the login credentials to login.

compose_element = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div'))).click()      # CLick on "Compose" button.

time.sleep(1)
em = wait.until(EC.element_to_be_clickable((By.NAME, 'to')))        # Select the "to" field, send the respective Email ID.
em.send_keys(to_em)
time.sleep(2)

sub = wait.until(EC.element_to_be_clickable((By.NAME, 'subjectbox')))   # Pass the subject into the "Subject" field.
sub.send_keys(to_sub)
time.sleep(2)

body = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":97"]')))     # Locate the "body" and send in the respective string.
body.send_keys(to_body)
time.sleep(2)

body.send_keys(Keys.CONTROL + Keys.RETURN)      # Emulates pressing of CTRL + ENTER key. (Used to send Email.)

time.sleep(7)      # Wait for 7 seconds.
browser.close()     # Close the browser window.
