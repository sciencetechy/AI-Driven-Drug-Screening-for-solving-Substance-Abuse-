import numpy as np
import pandas as pd
import joblib

# List of models
model_names = ["AVPR2", "ADRB2", "AKT1", "CNR1", "CXCR1", "CXCR2", "CXCR4", 
               "MC1R", "S1PR1", "SMO", "SRC", "MOR", "hERG"]


for j in range(2, 13):
    # Load molecular fingerprints (2D array)
    drug_fingerprints = np.load(f"S{j}.npy")  # Shape (15, N), where N is the fingerprint length

    # Create drug identifiers (e.g., Drug_1, Drug_2, ...)
    drug_names = [f"Drug_{i+1}" for i in range(drug_fingerprints.shape[0])]

    # Initialize an empty DataFrame for results
    results_df = pd.DataFrame(index=drug_names, columns=model_names)

    # Load each model and predict binding affinities
    for model_name in model_names:
        # Load the model
        model = joblib.load(f"{model_name}_model.pkl")
        
        # Predict binding affinities for all drugs
        predictions = model.predict(drug_fingerprints)
        
        # Categorize predictions into 'High', 'Medium', 'Low'
    # categories = [
    #     "High" if pred < -9 else "Medium" if -9 <= pred < -7 else "Low"
        #    for pred in predictions
    # ]
        
        # Add results to DataFrame
        results_df[model_name] = predictions

    # Save results to an Excel file
    results_df.to_excel(f"S{j}_grid.xlsx", index_label="Drug")
    print(f"saved s{j}")