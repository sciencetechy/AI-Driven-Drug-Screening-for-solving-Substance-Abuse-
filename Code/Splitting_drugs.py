import pandas as pd

# Load the new_drugs.xlsx file
df = pd.read_excel("filtered_drugs.xlsx")

# Keep only the SMILES column
df_smiles = df[['SMILES']]

# Number of rows per CSV file
rows_per_file = 1000

# Split the DataFrame into chunks and save each as a CSV file
num_chunks = len(df_smiles) // rows_per_file + (1 if len(df_smiles) % rows_per_file != 0 else 0)

for i in range(num_chunks):
    start_row = i * rows_per_file
    end_row = (i + 1) * rows_per_file
    chunk = df_smiles[start_row:end_row]
    file_name = f"S{i+1}.csv"
    chunk.to_csv(file_name, index=False)
    print(f"Saved {file_name}")