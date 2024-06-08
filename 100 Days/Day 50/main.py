from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

email = "jt316192@gmail.com"
password = os.environ.get("password")
url = "https://tinder.com/"

# click log in button
driver.get(url)
sleep(2)
login_button = driver.find_element(By.XPATH,
                                   value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
sleep(2)

# click facebook button
login_fb = driver.find_element(By.XPATH,
                               value="/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button")
login_fb.click()
sleep(2)

# Switch to log in window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# log in through facebook
name = driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
pw = driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
name.send_keys(email)
pw.send_keys(password)
pw.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
sleep(5)

# after log in buttons
decline_button = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/button")
decline_button.click()
allow_location = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]")
allow_location.click()
miss_noti = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[2]")
miss_noti.click()
sleep(5)

# swipe dislike

for n in range(100):
    # put 1 sec between every dislike clicks
    sleep(1)

    # click dislike
    try:
        dislike = driver.find_element(
            By.XPATH,
            value="/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div["
                  "3]/div/div[2]/button"
        )
        dislike.click()

    # catch cases when dislike button not loaded yet
    except NoSuchElementException:
        print("loading dislike button")
        sleep(2)

driver.quit()
