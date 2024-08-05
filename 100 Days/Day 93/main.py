from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv

from selenium.webdriver.support.wait import WebDriverWait

website = "https://www.audible.com/search?keywords=book&node=18573211011"
search = "Harry potter"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# locate the website and search for the book
driver.get(website)
search_bar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-search"]')))
search_bar.clear()
sleep(1)
search_bar.send_keys(search)
search_bar.submit()

# get all details for all results
book_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.productListItem')))

all_books = []

for book in book_elements:
    title = book.find_element(By.CSS_SELECTOR, '.bc-pub-break-word > a').text
    author = book.find_element(By.CSS_SELECTOR, '.authorLabel > span > a').text
    narrated_by = book.find_element(By.CSS_SELECTOR, '.narratorLabel > span > a').text
    audio_length = book.find_element(By.CSS_SELECTOR, '.runtimeLabel > span').text
    release_date = book.find_element(By.CSS_SELECTOR, '.releaseDateLabel > span').text
    language = book.find_element(By.CSS_SELECTOR, '.languageLabel > span').text
    rating = book.find_element(By.CSS_SELECTOR, '.ratingsLabel > span').text
    num_rating = book.find_element(By.CSS_SELECTOR, '.ratingsLabel > span.bc-text:nth-of-type(2)').text
    regular_price = book.find_element(By.CSS_SELECTOR, '.buybox-regular-price  > span.bc-text:nth-of-type(2)').text
    try_price = book.find_element(By.CSS_SELECTOR, '.bc-spacing-top-micro  > span > a > span').text
    link = book.find_element(By.CSS_SELECTOR, '.bc-pub-break-word > a').get_attribute('href')
    img = book.find_element(By.CSS_SELECTOR, '.bc-image-inset-border').get_attribute('src')

    # append scraped information into a list
    book_info = {
        'Title': title,
        'Author': author,
        'Narrated by': narrated_by,
        'Audio Length': audio_length,
        'Release date': release_date,
        'Language': language,
        'Rating': rating,
        'Number of Ratings': num_rating,
        'Regular price': regular_price,
        'Try price': try_price,
        'Link': link,
        'Image URL': img
    }
    all_books.append(book_info)

# convert list into csv file
file_name = 'books.csv'
headers = all_books[0].keys()
print(headers)
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for books in all_books:
        row = []
        for header in headers:
            row.append(books[header])
        writer.writerow(row)
    print(row)

driver.quit()
