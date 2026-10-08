from src.scraper import scraper
url = "https://news.ycombinator.com/"
def test_scraper():
    result = scraper(url)
    assert result is not None