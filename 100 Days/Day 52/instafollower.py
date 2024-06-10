from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

from selenium.webdriver.support.wait import WebDriverWait


class InstaFollower:
    def __init__(self, url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get(url)
        sleep(2)

    def log_in(self, username, pw):
        username_link = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        pw_link = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        username_link.send_keys(username)
        pw_link.send_keys(pw, Keys.ENTER)
        sleep(5)

    def dismiss_pop_ups(self):
        not_now = self.driver.find_element(By.CSS_SELECTOR, value="._ac8f div")
        not_now.click()
        sleep(2)
        no_noti = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div["
                                                           "2]/div/div/div[3]/button[2]")
        no_noti.click()
        sleep(2)

    def find_followers(self, insta_url, acc):
        self.driver.get(insta_url)
        sleep(2)
        follower_button = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div["
                                                                   "1]/div[2]/div/div["
                                                                   "2]/section/main/div/header/section[3]/ul/li["
                                                                   "2]/div/a")
        sleep(3)
        follower_button.click()
        sleep(5)

        scr1 = self.driver.find_element(By.XPATH, "//div[@role='dialog']//div[contains(@class, 'xyi19xy')]")
        sleep(3)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            sleep(2)

    def follow(self):
        profiles = self.driver.find_elements(By.XPATH, value="//div[@role='dialog']//div[contains(@class, "
                                                             "'xyi19xy')]//div[contains(@class, 'x1dm5mii')]")

        for button in profiles:
            follow_button = self.driver.find_element(By.XPATH, value="//div[@role='dialog']//div[contains(@class, "
                                                                     "'xyi19xy')]//div[contains(@class, "
                                                                     "'x1dm5mii')]//button")
            try:
                follow_button.click()
                sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


