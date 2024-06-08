import requests
from bs4 import BeautifulSoup
import smtplib
import os

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
to_email = "jianxunbak@yahoo.com.sg"
my_email = "jianxunbak@gmail.com"
password = os.environ.get("password")
gmail_email_server = "smtp.gmail.com"

response = requests.get(url=url, headers=headers)
website = response.text

soup = BeautifulSoup(website, "html.parser")
discount = soup.find(name="span", class_="a-size-large a-color-price savingPriceOverride aok-align-center "
                                         "reinventPriceSavingsPercentageMargin savingsPercentage")
dollar = soup.find(name="span", class_="a-price-whole")
cents = soup.find(name="span", class_="a-price-fraction")
price = float(f"{dollar.getText()}{cents.getText()}")

if price < 95.00:
    with smtplib.SMTP(gmail_email_server, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"subject:DISCOUNT!\n\nThere is a discount of {discount.getText()}.\nThe price is at ${price}.\nBuy now "
                f"at {url}!"
        )
