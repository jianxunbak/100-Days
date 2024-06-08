from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class InternetSpeedTwitterBot:
    def __init__(self, up, down):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.promised_up = up
        self.promised_down = down

    def get_internet_speeed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(3)
        privacy = self.driver.find_element(By.CSS_SELECTOR, value="#onetrust-accept-btn-handler")
        privacy.click()
        sleep(1)
        go = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go.click()
        sleep(45)
        back_to_results = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div["
                                                                   "2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a")
        back_to_results.click()
        sleep(1)
        download = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div["
                                                            "3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div["
                                                            "1]/div/div[2]/span")
        upload = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div["
                                                          "3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div["
                                                          "2]/span")
        self.upload = float(upload.text)
        self.download = float(download.text)

    def tweet_at_provider(self, username, password):
        self.driver.get("https://x.com/i/flow/login")
        sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='username']"))).send_keys(username, Keys.ENTER)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='current-password']"))).send_keys(password,
                                                                                                           Keys.ENTER)
        sleep(5)

    def twitter_post(self):
        message = (f"Hey Internet Provider, why is my internet speed {self.download}down/{self.upload}up when i "
                   f"pay for {self.promised_down}down/{self.promised_up}up")
        if self.upload < self.promised_up and self.download < self.promised_down:
            post = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div["
                                                            "2]/main/div/div/div/div/div/div["
                                                            "3]/div/div[2]/div[1]/div/div/div[1]/div["
                                                            "2]/div/div/div/div/div/div/div/div/div/div/div/div/div["
                                                            "1]/div/div/div/div/div/div[2]/div/div/div/div")
            post_message = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                                    '2]/main/div/div/div/div/div/div[3]/div/div['
                                                                    '2]/div[1]/div/div/div/div[2]/div[2]/div['
                                                                    '2]/div/div/div/button')
            post.send_keys(message)
            post_message.click()
            sleep(5)
