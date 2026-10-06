import requests
from bs4 import BeautifulSoup


def scraper(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    all_text = soup.get_text(separator=" ", strip=True)

    return all_text
