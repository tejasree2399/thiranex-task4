import pandas as pd
import matplotlib.pyplot as plt

# Sample Retail Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [15000, 18000, 17000, 22000, 25000, 27000],
    "Profit": [3000, 3500, 3200, 4500, 5000, 6000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

# Sales Trend
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("sales_trend.png")
plt.show()

# Profit Chart
plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Profit"])
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.savefig("category_sales.png")
plt.show()

print("\nConclusion:")
print("Sales and profit show an increasing trend over time.")