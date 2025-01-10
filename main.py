import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv('data.csv')
print("Data Loaded Successfully:")
print(data)

# Calculate total sales
total_sales = data['Sales'].sum()
print(f"\nTotal Sales: {total_sales}")

# Calculate average sales
avg_sales = data['Sales'].mean()
print(f"Average Sales: {avg_sales}")

# Bar chart of sales per region
region_sales = data.groupby('Region')['Sales'].sum()
print("\nSales per Region:")
print(region_sales)

# Create the plot
plt.figure(figsize=(8, 6))  # Adjust the figure size if necessary
region_sales.plot(kind='bar', title='Sales by Region', color='skyblue')

# Set labels
plt.xlabel('Region')
plt.ylabel('Total Sales')

# Display the plot on the screen
plt.show()

# Save bar chart as image
plt.savefig('sales_by_region.png', bbox_inches='tight')  # bbox_inches='tight' ensures the chart fits properly
print("Bar chart saved as 'sales_by_region.png'")

# Maximum and minimum sales by region
max_sales_region = region_sales.idxmax()
print(f"Region with Maximum Sales: {max_sales_region} ({region_sales[max_sales_region]})")

min_sales_region = region_sales.idxmin()
print(f"Region with Minimum Sales: {min_sales_region} ({region_sales[min_sales_region]})")

# Standard deviation of sales
std_dev_sales = data['Sales'].std()
print(f"Standard Deviation of Sales: {std_dev_sales}")

# Export metrics to CSV
metrics = {
    "Metric": ["Total Sales", "Average Sales", "Standard Deviation of Sales"],
    "Value": [total_sales, avg_sales, std_dev_sales]
}
metrics_df = pd.DataFrame(metrics)
metrics_df.to_csv('sales_metrics.csv', index=False)
print("Metrics saved to 'sales_metrics.csv'")
