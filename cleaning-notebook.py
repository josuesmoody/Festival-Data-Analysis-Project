# Festival Data Analysis Project
# Part 1: Web Scraping and Data Cleaning

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from datetime import datetime
import time

# Function to scrape Rock Werchter historical data
def scrape_rock_werchter():
    """
    Scrapes historical lineup data from Rock Werchter festival.
    Returns a DataFrame with year, artist, and festival information.
    """
    base_url = "https://www.rockwerchter.be/en/history"
    
    # Initialize empty list to store data
    festival_data = []
    
    try:
        # Set up Selenium WebDriver (Chrome)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode
        driver = webdriver.Chrome(options=options)
        
        # Navigate to the page
        driver.get(base_url)
        
        # Wait for the content to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "history-list"))
        )
        
        # Get page source and parse with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Find all year sections
        year_sections = soup.find_all('div', class_='history-item')
        
        for section in year_sections:
            year = section.find('h2').text.strip()
            artists = section.find_all('li')
            
            for artist in artists:
                festival_data.append({
                    'festival': 'Rock Werchter',
                    'year': int(year),
                    'artist': artist.text.strip(),
                    'source': base_url
                })
                
    except Exception as e:
        print(f"Error scraping Rock Werchter: {str(e)}")
    
    finally:
        driver.quit()
    
    return pd.DataFrame(festival_data)

# Function to scrape Pukkelpop historical data
def scrape_pukkelpop():
    """
    Scrapes historical lineup data from Pukkelpop festival.
    Returns a DataFrame with year, artist, and festival information.
    """
    base_url = "https://www.pukkelpop.be/en/history"
    festival_data = []
    
    # Similar implementation as Rock Werchter...
    # (Implementation would follow similar pattern but adjusted for Pukkelpop's HTML structure)
    
    return pd.DataFrame(festival_data)

def clean_festival_data(df):
    """
    Cleans and standardizes festival data.
    Parameters:
        df (DataFrame): Raw festival data
    Returns:
        DataFrame: Cleaned festival data
    """
    # Create a copy to avoid modifying the original
    cleaned_df = df.copy()
    
    # Standardize artist names
    cleaned_df['artist'] = cleaned_df['artist'].apply(lambda x: x.strip().title())
    
    # Remove any special characters or extra whitespace
    cleaned_df['artist'] = cleaned_df['artist'].apply(lambda x: re.sub(r'[^\w\s-]', '', x))
    
    # Ensure year is integer
    cleaned_df['year'] = pd.to_numeric(cleaned_df['year'], errors='coerce').astype('Int64')
    
    # Remove duplicates
    cleaned_df = cleaned_df.drop_duplicates()
    
    # Sort by year and artist
    cleaned_df = cleaned_df.sort_values(['year', 'artist'])
    
    return cleaned_df

def main():
    # Scrape data from different festivals
    print("Scraping Rock Werchter data...")
    werchter_df = scrape_rock_werchter()
    
    print("Scraping Pukkelpop data...")
    pukkelpop_df = scrape_pukkelpop()
    
    # Combine all festival data
    all_festivals_df = pd.concat([werchter_df, pukkelpop_df], ignore_index=True)
    
    # Clean the combined dataset
    cleaned_df = clean_festival_data(all_festivals_df)
    
    # Save to CSV and JSON
    print("Saving cleaned data...")
    cleaned_df.to_csv('festival_data_clean.csv', index=False)
    cleaned_df.to_json('festival_data_clean.json', orient='records')
    
    print("Data collection and cleaning complete!")
    return cleaned_df

if __name__ == "__main__":
    festival_data = main()