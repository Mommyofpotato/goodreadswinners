import requests
from bs4 import BeautifulSoup
import array

years=[2022,2021,2020,2019,2018,2017,2016,2015];
print("Goodreads Winners")
for year in years:
    URL = f"https://www.goodreads.com/choiceawards/best-books-{year}"
    page = requests.get(URL)
    print(year)
    soup = BeautifulSoup(page.content, "html.parser")
    for img in soup.find_all('img', alt=True,class_="category__winnerImage"):
        print(img['alt'])


