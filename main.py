from scraper import scraper
from summarizer import summarize
from firebase import save_summary


url = "https://news.ycombinator.com/"

text = scraper(url)

summary = summarize(text)

print(f"**Summary:** {summary}")

save_summary(summary)
