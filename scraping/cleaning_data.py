import json
import re

def clean_band_names(band_name):
    """
    Standardizes band names by removing extra spaces, special characters, etc.
    """
    band_name = band_name.strip()
    band_name = re.sub(r'\s+', ' ', band_name)  # Replaces multiple spaces with a single space
    band_name = band_name.replace('\xa0', ' ')  # Removes non-breaking spaces
    return band_name

def clean_festival_data(input_file, output_file):
    """
    Cleans festival data and saves it to a new JSON file.
    """
    with open(input_file, 'r') as f:
        data = json.load(f)

    cleaned_data = {}
    for festival, years in data.items():
        cleaned_data[festival] = {}
        for year, bands in years.items():
            cleaned_bands = list(set(clean_band_names(band) for band in bands))
            cleaned_data[festival][year] = sorted(cleaned_bands)  # Sort alphabetically

    # Save cleaned data
    with open(output_file, 'w') as f:
        json.dump(cleaned_data, f, indent=4)

    print(f"Cleaned data saved to '{output_file}'")

if __name__ == "__main__":
    input_file = "./data/festivals_data.json"
    output_file = "./data/cleaned_festivals_data.json"
    clean_festival_data(input_file, output_file)
