from instafollower import InstaFollower
import os
from time import sleep

email = os.environ.get("email")
password = os.environ.get("password")
url = "https://www.instagram.com/accounts/login/"
insta = "cats_of_instagram"
insta_acc_followers = f"https://www.instagram.com/{insta}/"

bot = InstaFollower(url=url)
bot.log_in(username=email, pw=password)
bot.dismiss_pop_ups()
bot.find_followers(insta_url=insta_acc_followers, acc=insta)
bot.follow()
sleep(5)
bot.driver.quit()