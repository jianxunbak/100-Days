from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
total_money = 0
cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

five_sec = time() + 5
five_min = time() + 300

# get ids of upgrades
upgrade = driver.find_elements(By.CSS_SELECTOR, value="#store div")
all_id = [items.get_attribute("id") for items in upgrade]

# get the prices of upgrades
upgrade = driver.find_elements(By.CSS_SELECTOR, value="#store b")
all_prices = []
for item in upgrade:
    cost = item.text.strip()
    if cost != "":
        item_price = int(item.text.split('-')[1].replace(',', '').strip())
        all_prices.append(item_price)

# make a dict of price and id
price_id = dict(zip(all_prices, all_id))

while True:
    cookie.click()

    if time() > five_sec:

        # get the current cookie count
        money = driver.find_element(By.CSS_SELECTOR, value="#money").text
        if "," in money:
            money = money.replace(',', '')
        total_money = int(money)
        print(total_money)

        # get affordable upgrade
        affordable_upgrades = {}
        for cost, id in price_id.items():
            if total_money > cost:
                affordable_upgrades[cost] = id
        print(affordable_upgrades)

        # purchase max upgrade
        max_upgrade = max(affordable_upgrades)
        print(max_upgrade)
        purchase_id = affordable_upgrades[max_upgrade]
        print(purchase_id)
        driver.find_element(by=By.ID, value=purchase_id).click()

        five_sec = time() + 5

    # stop after 5 minutes
    if time() > five_min:
        cps = driver.find_element(By.ID, value="cps").text
        print(cps)
        break
