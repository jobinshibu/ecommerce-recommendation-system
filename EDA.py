# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "Cleaned_OnlineRetail.xlsx"  # Path to your cleaned dataset
data = pd.read_excel(file_path)

# Step 1: Add a Total Revenue Column
data['TotalRevenue'] = data['Quantity'] * data['UnitPrice']

# Step 2: Most Frequently Purchased Products
product_counts = data['StockCode'].value_counts().head(10)
print("\nTop 10 Most Frequently Purchased Products:")
print(product_counts)

# Plot the top products
plt.figure(figsize=(10, 6))
product_counts.plot(kind='bar', color='skyblue')
plt.title("Top 10 Most Purchased Products")
plt.xlabel("Stock Code")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()

# Step 3: Top Products by Revenue
product_revenue = data.groupby('StockCode')['TotalRevenue'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Revenue:")
print(product_revenue)

# Plot revenue by product
plt.figure(figsize=(10, 6))
product_revenue.plot(kind='bar', color='orange')
plt.title("Top 10 Products by Revenue")
plt.xlabel("Stock Code")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.show()

# Step 4: Transactions by Country
country_transactions = data['Country'].value_counts().head(10)
print("\nTop 10 Countries by Number of Transactions:")
print(country_transactions)

# Plot transactions by country
plt.figure(figsize=(10, 6))
country_transactions.plot(kind='bar', color='green')
plt.title("Top 10 Countries by Transactions")
plt.xlabel("Country")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.show()

# Step 5: Sales Trends Over Time
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])  # Convert dates to datetime format
sales_trends = data.groupby(data['InvoiceDate'].dt.to_period('M'))['TotalRevenue'].sum()
print("\nSales Trends Over Time:")
print(sales_trends)

# Plot sales trends
plt.figure(figsize=(12, 6))
sales_trends.plot(kind='line', color='purple', marker='o')
plt.title("Sales Trends Over Time")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.grid(True)
plt.show()

# Step 6: Customer Insights
unique_customers = data['CustomerID'].nunique()
print(f"\nNumber of Unique Customers: {unique_customers}")

avg_items_per_transaction = data.groupby('InvoiceNo')['Quantity'].sum().mean()
print(f"Average Number of Items Purchased Per Transaction: {avg_items_per_transaction:.2f}")

# Step 7: Save Processed Data (Optional)
processed_file_path = "Processed_OnlineRetail.xlsx"
data.to_excel(processed_file_path, engine='openpyxl', index=False)
print("\nProcessed dataset saved to:", processed_file_path)
