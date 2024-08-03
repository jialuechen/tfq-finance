import pandas as pd

def load_csv(filepath):
    return pd.read_csv(filepath)

def load_excel(filepath):
    return pd.read_excel(filepath)

def load_json(filepath):
    return pd.read_json(filepath)

if __name__ == "__main__":
    filepath_csv = 'example.csv'
    filepath_excel = 'example.xlsx'
    filepath_json = 'example.json'

    # Replace with actual file paths
    # data_csv = load_csv(filepath_csv)
    # data_excel = load_excel(filepath_excel)
    # data_json = load_json(filepath_json)
    
    # print(data_csv.head())
    # print(data_excel.head())
    # print(data_json.head())