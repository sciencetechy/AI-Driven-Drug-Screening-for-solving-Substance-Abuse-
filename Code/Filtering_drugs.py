import pandas as pd

# Load the Excel file
file_name = "Drugs.xlsx"  # Update with the actual file extension if different
df = pd.read_excel(file_name)

# Remove rows where the SMILES column is empty
filtered_df = df[df['SMILES'].notna()]

# Save the filtered DataFrame to a new Excel file
new_file_name = "new_drugs.xlsx"
filtered_df.to_excel(new_file_name, index=False)

print(f"Filtered data has been saved to {new_file_name}")