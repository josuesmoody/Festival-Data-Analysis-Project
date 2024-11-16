import requests
from bs4 import BeautifulSoup
import re
import json

# Base URLs for festivals
FESTIVALS = {
    "rock_werchter": "https://www.rockwerchter.be/en/history",
    "pukkelpop": "https://www.pukkelpop.be/en/history",
}

def get_rock_werchter_data():
    """
    Specific scraping for Rock Werchter.
    """
    base_url = FESTIVALS["rock_werchter"]
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract year URLs
    links = soup.find_all('a', href=re.compile(r'/en/history/rock-werchter-\d{4}'))
    year_urls = [f"https://www.rockwerchter.be{link['href']}" for link in links if 'href' in link.attrs]

    # Scrape lineup for each year
    data = {}
    for url in year_urls:
        year_match = re.search(r'rock-werchter-(\d{4})', url)
        if year_match:
            year = year_match.group(1)
            lineup = scrape_rock_werchter_lineup(url)
            if lineup:
                data[year] = lineup
    return data

def scrape_rock_werchter_lineup(url):
    """
    Scrape the lineup for a specific year of Rock Werchter.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract lineup from the specific div
    lineup_div = soup.find('div', {'data-component': 'oembed/oembed'})
    bands = []

    if lineup_div:
        paragraphs = lineup_div.find_all('p')
        for paragraph in paragraphs:
            text = paragraph.get_text()
            if ':' in text:
                bands_text = text.split(':', 1)[1]
                bands.extend([band.strip() for band in bands_text.split(',')])
    return bands

def get_pukkelpop_data():
    """
    Specific scraping for Pukkelpop.
    """
    base_url = "https://www.pukkelpop.be/en/history/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract year URLs
    links = soup.find_all('a', href=re.compile(r'/en/history/\d{4}'))
    year_urls = [f"https://www.pukkelpop.be{link['href']}" for link in links if 'href' in link.attrs]

    # Scrape lineup for each year
    data = {}
    for url in year_urls:
        year_match = re.search(r'/en/history/(\d{4})', url)
        if year_match:
            year = year_match.group(1)
            lineup = scrape_pukkelpop_lineup(url)
            if lineup:
                data[year] = lineup
    return data

def scrape_pukkelpop_lineup(url):
    """
    Scrape the lineup for a specific year of Pukkelpop.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract lineup from the specific list
    lineup_list = soup.select('ul.act-edition-detail__acts > li')
    bands = []

    for item in lineup_list:
        # Some elements may be plain text, others links
        if item.find('a'):
            band = item.find('a').get_text(strip=True)
        else:
            band = item.get_text(strip=True)
        bands.append(band)

    return bands

def main():
    all_festivals_data = {}

    # Scraping Rock Werchter
    print("Scraping Rock Werchter...")
    rock_werchter_data = get_rock_werchter_data()
    all_festivals_data["rock_werchter"] = rock_werchter_data

    # Scraping Pukkelpop
    print("Scraping Pukkelpop...")
    pukkelpop_data = get_pukkelpop_data()
    all_festivals_data["pukkelpop"] = pukkelpop_data

    # Save data to a consolidated JSON file
    with open("./data/festivals_data.json", "w") as f:
        json.dump(all_festivals_data, f, indent=4)
    print("Data saved to 'data/festivals_data.json'")

if __name__ == "__main__":
    main()
