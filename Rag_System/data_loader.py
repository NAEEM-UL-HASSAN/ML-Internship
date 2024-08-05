import pandas as pd

def load_data(file_path):
    df = pd.read_excel(file_path, sheet_name=None)
    data = df[list(df.keys())[0]]
    data.columns = ['Disease Name', 'Symptoms', 'Specialist Doctor']
    return data
