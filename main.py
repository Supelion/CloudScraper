import random
import os

try:
    import cloudscraper
except ImportError:
    os.system("pip3 install cloudscraper")
    import cloudscraper

# Clearing out the screen
os.system("cls")

# Asking for the user's input on what URL to scrape
url = input("\n\nEnter a URL to scrape: ")

# Random browser choice between chrome and firefox
browser = random.choice(["chrome", "firefox"])

# Random platform choice
platform = random.choice(['linux', 'windows', 'darwin', 'android', 'ios'])

scraperInfo = {
    'browser': browser,
    'platform': platform
}

scraper = cloudscraper.create_scraper(scraperInfo)

try:
    print(f"Getting data... Browser: {browser}, Platform: {platform}")
    data = scraper.get(url).text

    with open("data.txt", "w", encoding = "utf-8") as f:
        f.write(data)

    print("Done! Saved the data to data.txt!")

except Exception as e:
    print(e)