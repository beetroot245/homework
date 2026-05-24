import pandas as pd

df = pd.read_csv("Grocery_Inventory_and_Sales_Dataset.csv")

df["Unit_Price"] = (
    df["Unit_Price"]
    .replace(r"[\$,]", "", regex=True)
    .astype(float)
)

df["Total_Inventory_Value"] = (
    df["Stock_Quantity"] * df["Unit_Price"]
)

print("===== 每個商品的總庫存價值 =====")
print(df[["Product_Name", "Total_Inventory_Value"]])

best_selling = df.loc[df["Sales_Volume"].idxmax()]

print("\n===== 最暢銷商品 =====")
print("商品名稱：", best_selling["Product_Name"])
print("銷售量：", best_selling["Sales_Volume"])

df["Discounted_Revenue"] = (
    df["Sales_Volume"] * df["Unit_Price"] * 0.9
)

total_revenue = df["Discounted_Revenue"].sum()

print("\n===== 9折後的總收入 =====")
print(total_revenue)