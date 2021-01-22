from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all(name="h3", class_="title")
movie_titles = [article.getText() for article in articles]
# for n in range(len(movie_titles) -1, -1, -1):
#     print(movie_titles[n])
movies = movie_titles[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")



# movie = []
# for n in movie_titles:
#     str1 = n
#     str2 = ''
#     for c in str1:
#         if c not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',')'):
#             str2 = str2 + c
#     movie.append(str2)
# movie.reverse()
#
# num_movie = [f"{num+1}) {item}" for num, item in movie]
#
#
# with open("movies.txt", "w", encoding="ISO-8859-1") as file:
#     file.write(str(num_movie))
