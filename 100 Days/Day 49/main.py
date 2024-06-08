from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

url = ("https://www.linkedin.com/jobs/search/?currentJobId=3924223523&f_LF=f_AL&geoId=102257491&keywords=python"
       "%20developer&location=London%2C%20England%2C%20United%20Kingdom")
username = "yoz889@hotmail.com"
password = os.environ.get("password")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

sign_in = driver.find_element(By.CSS_SELECTOR, value=".btn-secondary-emphasis")
sign_in.click()
user = driver.find_element(By.CSS_SELECTOR, value="#username")
pw = driver.find_element(By.CSS_SELECTOR, value="#password")
button = driver.find_element(By.CLASS_NAME, value="login__form_action_container")
user.send_keys(username)
sleep(2)
pw.send_keys(password)
sleep(2)
button.click()
sleep(5)

# select first job on list
first_job = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
first_job.click()
sleep(1)
hide_chat = driver.find_element(By.ID,value="ember42")
hide_chat.click()
sleep(1)
element = driver.find_element(By.CSS_SELECTOR, value=".follow.artdeco-button.artdeco-button--secondary.ml5")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
follow = driver.find_element(By.CLASS_NAME, value="follow.artdeco-button.artdeco-button--secondary.ml5")
follow.click()

