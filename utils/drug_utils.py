import pandas as pd

def load_data(csv_path="data/drug_dataset.csv"):
    df = pd.read_csv(csv_path)
    drug_dict = {}
    for _, row in df.iterrows():
        drug_dict[row['DrugName']] = {
            "used_for": row['UsedFor'],
            "side_effects": [s.strip() for s in row['SideEffects'].split(';')]
        }
    return drug_dict
