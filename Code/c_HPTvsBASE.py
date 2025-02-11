import pandas as pd

# Load the Excel file
file_path = 'HPTvsBASE.xlsx'  # Adjust the file path if needed
df = pd.read_excel(file_path)

# Check the column names to ensure 'B' and 'C' are correct
print(df.columns)

high = -9
low = -7

# Define the classification function
def classify(value):
    if value >= low:
        return 'Low'
    elif high <= value < low:
        return 'Medium'
    else:
        return 'High'

# Assuming the columns are named correctly (e.g., 'B' and 'C'), apply classification
df['Part B Classified'] = df['ACTUAL BA'].apply(classify)
df['Part C Classified'] = df['Predicted For Without HPT'].apply(classify)

# Create a confusion matrix-like table for Part B vs Part C classifications
result = pd.crosstab(df['Part B Classified'], df['Part C Classified'], rownames=['Part B'], colnames=['Part C'])

# Save the classified results to a new Excel file
output_file_path = 'temp.xlsx'
result.to_excel(output_file_path)

print("Classified summary Excel file created successfully!")