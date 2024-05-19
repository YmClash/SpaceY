import pandas as pd
from pathlib import Path
from urllib import  parse


def dataset_downloader(URL:str):
    dataset = pd.read_csv(URL)
    file_name = Path(URL).name
    save_path = Path(r'C:\Users\y_mc\PycharmProjects\SpaceY\DATASET\ '+file_name)
    dataset = pd.read_csv(URL)
    dataset.to_csv(save_path)
    dataset.head()
    print(f"dataset file saved in :{save_path.parent} ")
    print("Done")
    return

def date_time(table_cells:str):
    return [date_time.strip() for data_time in list(table_cells).strings][0:2]

def booster_version(table_cells):
    out=''.join([booster_version for i,booster_version in enumerate( table_cells.strings) if i%2==0][0:-1])
    return out

def landing_statis






