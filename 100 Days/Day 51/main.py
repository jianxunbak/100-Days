import os
from twitterbot import InternetSpeedTwitterBot

promised_down = 900.00
promised_up = 500.00
chrome_driver_path = "/Users/angela/Development/chromedriver"

bot = InternetSpeedTwitterBot(up=promised_up, down=promised_down)
bot.get_internet_speeed()
bot.tweet_at_provider(username=os.environ.get("twitter_email"), password=os.environ.get("twitter_password"))
bot.twitter_post()

bot.driver.quit()
