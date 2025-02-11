import pickle
import numpy as np
import pandas as pd
import joblib

# File paths
fingerprints_file = "MOR.npy"
binding_affinities_file = "MOR.csv"
smiles_file = "MOR.smi"
base_model_file = "MOR_Model.pkl"
hpt_model_file = "HPT_CV_Model_MOR.joblib"

# Load data
fingerprints = np.load(fingerprints_file)  # Molecular fingerprints
binding_affinities_df = pd.read_csv(binding_affinities_file)  # Actual binding affinities

with open(smiles_file, 'r') as f:
    smiles_list = [line.strip() for line in f]  # SMILES strings

# Load models
base_model = joblib.load(base_model_file)
hpt_model = joblib.load(hpt_model_file)    # Load HPT model

# Predict binding affinities
predicted_base = base_model.predict(fingerprints)
predicted_hpt = hpt_model.predict(fingerprints)

# Combine data into a DataFrame
result_df = pd.DataFrame({
    "SMILES": smiles_list,
    "ACTUAL BA": binding_affinities_df['Binding Affinities'],  # Adjust column name if needed
    "PREDICTED FOR MODEL 1": predicted_base,
    "PREDICTED FOR MODEL 2": predicted_hpt
})

# Sort by actual binding affinity (ascending)
result_df = result_df.sort_values(by="ACTUAL BA")

# Export to Excel
excel_file = "binding_affinities.xlsx"
result_df.to_excel(excel_file, index=False, engine="openpyxl")

print(f"Excel sheet '{excel_file}' created successfully.")