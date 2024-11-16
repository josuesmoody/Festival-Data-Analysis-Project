import json
import re

def clean_band_names(band_name):
    """
    Estandariza nombres de bandas eliminando espacios extra, caracteres especiales, etc.
    """
    band_name = band_name.strip()
    band_name = re.sub(r'\s+', ' ', band_name)  # Reemplaza múltiples espacios por uno solo
    band_name = band_name.replace('\xa0', ' ')  # Elimina espacios no rompibles
    return band_name

def clean_festival_data(input_file, output_file):
    """
    Limpia los datos de festivales y los guarda en un nuevo archivo JSON.
    """
    with open(input_file, 'r') as f:
        data = json.load(f)

    cleaned_data = {}
    for festival, years in data.items():
        cleaned_data[festival] = {}
        for year, bands in years.items():
            cleaned_bands = list(set(clean_band_names(band) for band in bands))
            cleaned_data[festival][year] = sorted(cleaned_bands)  # Ordenar alfabéticamente

    # Guardar datos limpios
    with open(output_file, 'w') as f:
        json.dump(cleaned_data, f, indent=4)

    print(f"Datos limpios guardados en '{output_file}'")

if __name__ == "__main__":
    input_file = "./data/festivals_data.json"
    output_file = "./data/cleaned_festivals_data.json"
    clean_festival_data(input_file, output_file)
