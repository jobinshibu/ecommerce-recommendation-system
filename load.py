# Import required libraries
import pandas as pd

# Step 1: Load the Dataset
file_path = "OnlineRetail (1).xlsx"  # Update the path if needed
data = pd.read_excel(file_path)

# Step 2: Inspect the Dataset
print("First 5 rows of the dataset:")
print(data.head())  # Display the first 5 rows

print("\nDataset Information:")
print(data.info())  # Display dataset info (columns, data types, etc.)

# Step 3: Check for Missing Values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())  # Check for null values

# Step 4: Check for Duplicates
print("\nNumber of Duplicate Rows:")
print(data.duplicated().sum())  # Count duplicate rows

# Step 5: Data Cleaning
# Remove duplicates
data = data.drop_duplicates()
print("\nDuplicates removed. Dataset now has", len(data), "rows.")

# Handle missing values
print("\nHandling Missing Values:")
data = data.dropna()  # Drop rows with missing values
print("Rows with missing values removed. Dataset now has", len(data), "rows.")

# Step 6: Save Cleaned Data
try:
    # Save as Excel file with openpyxl engine
    cleaned_excel_path = "Cleaned_OnlineRetail.xlsx"
    data.to_excel(cleaned_excel_path, engine='openpyxl', index=False)
    print("\nCleaned dataset successfully saved as Excel file to:", cleaned_excel_path)
except Exception as e:
    print("Error saving Excel file:", e)

# Save as CSV (alternative format)
csv_file_path = "Cleaned_OnlineRetail.csv"
data.to_csv(csv_file_path, index=False)
print("Cleaned dataset also saved as CSV to:", csv_file_path)

# Step 7: Summary
print("\nFinal Dataset Summary:")
print(data.describe())  # Statistical summary of numerical columns
