import pandas as pd

def clean_data(festival_data_df):
    """
    Limpia los datos eliminando entradas vacías y duplicados.
    """
    festival_data_df.dropna(inplace=True)
    festival_data_df.drop_duplicates(inplace=True)
    return festival_data_df
