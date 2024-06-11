from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import requests
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

# --- Using Beautiful Soup to scrap data from website --- #
rental_url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(rental_url)
website = response.text
soup = BeautifulSoup(website, "html.parser")

links = []
prices = []
addresses = []

listing_links = soup.find_all(name="a", class_="property-card-link")
for item in listing_links:
    href = item.get('href')
    links.append(href)

listing_price = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
for item in listing_price:
    price = item.getText().split('+')[0].replace('/mo', '')
    prices.append(price)

listing_address = soup.find_all(name="a", attrs={'data-test': 'property-card-link'},
                                class_="StyledPropertyCardDataArea-anchor")
for item in listing_address:
    add = (item.text.strip().replace("|", "").replace(',', ''))
    addresses.append(add)

# --- Using Selenium to fill in google forms from scrapped data --- #
google_forms = ("https://docs.google.com/forms/d/e/1FAIpQLScI1HWcepDP5DBvzSt5LzrYgJlcSQLXbaJRW6vuKKZzmENf1A/viewform"
                "?usp=sf_link")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get(url=google_forms)
sleep(1)

for i in range(len(links)):
    address_qn = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div['
                                           '1]/input')
    price_qn = driver.find_element(By.XPATH,
                                   value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div['
                                         '1]/input')
    link_qn = driver.find_element(By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div['
                                        '1]/input')
    button = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    address_qn.send_keys(addresses[i])
    price_qn.send_keys(prices[i])
    link_qn.send_keys(links[i])
    button.click()
    sleep(1)
    another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    sleep(1)

driver.quit()
