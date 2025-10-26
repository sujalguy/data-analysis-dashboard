
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Data
data = pd.read_csv('data.csv')
print("✅ Data Loaded Successfully!")
print(data.head(9))

# Step 2: Data Summary
print("\n📊 Basic Statistics:")
print(data.describe())

# Step 3: Total and Average Calculations
total_sales = data['Sales'].sum()
total_profit = data['Profit'].sum()
avg_sales = data['Sales'].mean()

print(f"\n💰 Total Sales: {total_sales}")
print(f"💵 Total Profit: {total_profit}")
print(f"📈 Average Sales per Day: {avg_sales:.2f}")

# Step 4: Analyze Sales by Product
sales_by_product = data.groupby('Product')['Sales'].sum()
profit_by_region = data.groupby('Region')['Profit'].sum()

print("\n🏆 Sales by Product:")
print(sales_by_product)
print(profit_by_region)

# Step 5: Visualization Dashboard
plt.figure(figsize=(12, 6))

# Subplot 1 - Sales by Product
plt.subplot(1, 2, 1)
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')

# Subplot 2 - Profit by Region
plt.subplot(1, 2, 2)
profit_by_region.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='Pastel1')
plt.title('Profit Share by Region')

plt.tight_layout()
plt.show()
