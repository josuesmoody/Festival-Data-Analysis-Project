import requests
from bs4 import BeautifulSoup
import re
import json

# URLs base para festivales
FESTIVALS = {
    "rock_werchter": "https://www.rockwerchter.be/en/history",
    "pukkelpop": "https://www.pukkelpop.be/nl/geschiedenis",
}

def get_rock_werchter_data():
    """
    Scraping específico para Rock Werchter.
    """
    base_url = FESTIVALS["rock_werchter"]
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Obtener URLs de los años
    links = soup.find_all('a', href=re.compile(r'/en/history/rock-werchter-\d{4}'))
    year_urls = [f"https://www.rockwerchter.be{link['href']}" for link in links if 'href' in link.attrs]

    # Scraping de lineup por año
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
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer lineup del div específico
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
    Scraping específico para Pukkelpop.
    """
    base_url = FESTIVALS["pukkelpop"]
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Obtener URLs de los años
    links = soup.find_all('a', href=re.compile(r'/nl/geschiedenis/\d{4}'))
    year_urls = [f"https://www.pukkelpop.be{link['href']}" for link in links if 'href' in link.attrs]

    # Scraping de lineup por año
    data = {}
    for url in year_urls:
        year_match = re.search(r'geschiedenis/(\d{4})', url)
        if year_match:
            year = year_match.group(1)
            lineup = scrape_pukkelpop_lineup(url)
            if lineup:
                data[year] = lineup
    return data

def scrape_pukkelpop_lineup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ajusta el selector según la estructura del HTML de Pukkelpop
    lineup_div = soup.find('div', {'class': 'lineup-section'})
    bands = []

    if lineup_div:
        raw_text = lineup_div.get_text(separator=", ")
        bands = [re.sub(r'\s+', ' ', band.strip()) for band in raw_text.split(",") if band.strip()]
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

    # Guardar datos en un archivo JSON consolidado
    with open("./data/festivals_data.json", "w") as f:
        json.dump(all_festivals_data, f, indent=4)
    print("Datos guardados en 'data/festivals_data.json'")

if __name__ == "__main__":
    main()
