import time
from selenium import webdriver
from time import sleep
import numpy as np
import pyautogui

website = "https://elgoog.im/t-rex/"
near = 140
region = (near, 615, 200, 85)
time_to_play = 50
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",  True)
driver = webdriver.Chrome(options=chrome_options)

# locate the website and search for the book
driver.get(website)
driver.maximize_window()
sleep(6)

pyautogui.press('space')
sleep(3)
dino_front = pyautogui.screenshot(region=region)
dino_front.save('dino_front.png')

game_start_time = time.time()
game = True
while game:
    sleep(0.01)
    region = (near, 615, 200, 85)
    dino_front_1 = pyautogui.screenshot(region=region)
    dino_front_1.save('dino_front_1.png')

    array_1 = np.array(dino_front)
    array_2 = np.array(dino_front_1)

    if np.array_equal(array_1, array_2):
        print('no difference')
    else:
        pyautogui.press('space')
        print("Difference detected")

    dino_front = dino_front_1
    dino_front.save('dino_front.png')

    near += 1
    print(region)

    if time.time() - game_start_time >= time_to_play:
        print('quitting')
        break

driver.quit()