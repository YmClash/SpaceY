import pandas as pd
from pathlib import Path
from urllib import  parse
import unicodedata

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

# on vas d'abord extraire

def date_time(table_cells:str):
    return [date_time.strip() for data_time in list(table_cells).strings][0:2]

def booster_version(table_cells):

    out=''.join([booster_version for i,booster_version in enumerate( table_cells.strings) if i%2==0][0:-1])
    return out

def landing_status(table_cells):

    out=[i for i in table_cells.strings][0]
    return out


def get_mass(table_cells):
    mass=unicodedata.normalize("NFKD", table_cells.text).strip()
    if mass:
        mass.find("kg")
        new_mass=mass[0:mass.find("kg")+2]
    else:
        new_mass=0
    return new_mass


def extract_column_from_header(row):
    """
    This function returns the landing status from the HTML table cell
    Input: the  element of a table data cell extracts extra row
        """
    if (row.br):
        row.br.extract()
    if row.a:
        row.a.extract()
    if row.sup:
        row.sup.extract()

    colunm_name = ' '.join(row.contents)

    # Filter the digit and empty names
    if not (colunm_name.strip().isdigit()):
        colunm_name = colunm_name.strip()
        return colunm_name





