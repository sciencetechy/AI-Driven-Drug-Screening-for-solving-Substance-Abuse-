import pandas as pd

# Define classification thresholds
high = -9
low = -7
model_names = ["AVPR2", "ADRB2", "AKT1", "CNR1", "CXCR1", "CXCR2", "CXCR4", 
               "MC1R", "S1PR1", "SMO", "SRC", "MOR", "hERG"]

# Define the classification function
def classify(value):
    if value >= low:
        return 'Low'
    elif high <= value < low:
        return 'Medium'
    else:
        return 'High'

# Load the Excel file (replace 'file.xlsx' with your actual file path)
file_path = 'Final_Trial_grid.xlsx'  # Update with your Excel file path
df = pd.read_excel(file_path)

for i in model_names:
    # Replace 'Binding Affinity' with the actual column name in your file
    ba_column = i  # Update with your BA column name

    # Apply the classification function
    df[i] = df[i].apply(classify)


# Save the updated DataFrame to a new Excel file
output_path = 'categorized_final.xlsx'  # Update with your desired output file path
df.to_excel(output_path, index=False)

print("Binding affinities categorized and saved to", output_path)