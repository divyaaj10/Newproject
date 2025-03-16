
import pandas as pd
import pyreadstat

# Specify the path to your .sav file (update this accordingly)
sav_file_path = "diabetes_model.sav"  # Change this to your actual file name

try:
    # Read the .sav file
    df, meta = pyreadstat.read_sav(sav_file_path)

    # Display the first few rows
    print("Data from .sav file:")
    print(df.head())

    # Save as a CSV (optional)
    df.to_csv("output.csv", index=False)
    print("CSV file saved successfully as output.csv.")

except FileNotFoundError:
    print(f"Error: The file {sav_file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
