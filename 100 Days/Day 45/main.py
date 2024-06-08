import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")
titles = soup.find_all(name="h3", class_="title")


all_titles = [item.getText() for item in titles]
movie_list = all_titles[::-1] # start, stop, step
with open("movies.txt", mode= "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")