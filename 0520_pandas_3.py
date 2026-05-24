import pandas as pd

df = pd.read_csv("SuperMarket Analysis.csv")

print("資料筆數：", len(df))

print("\n前五筆資料：")
print(df.head())

filtered_df = df[(df["Branch"] == "A") & (df["Customer type"] == "Member")]

print("\nBranch 為 A 且 Customer type 為 Member 的資料：")
print(filtered_df.head())

product_summary = (
    df.groupby("Product line")
    .agg(
        Total_Sales=("Sales", "sum"),
        Average_Rating=("Rating", "mean")
    )
    .round(2)
)

print("\n各產品線銷售與評分：")
print(product_summary)

city_gender_summary = (
    df.groupby(["City", "Gender"])
    .agg(
        Average_Sales=("Sales", "mean"),
        Transaction_Count=("Invoice ID", "count")
    )
    .round(2)
)

print("\nCity 與 Gender 分組結果：")
print(city_gender_summary)

top_product = product_summary["Total_Sales"].idxmax()
top_sales = product_summary["Total_Sales"].max()

print("\n總銷售額最高的產品線：")
print(f"{top_product}，總銷售額：{top_sales:.2f}")

product_summary.to_csv("0520_pandas_3OK.csv", encoding="utf-8-sig")

print("\n檔案已輸出：0520_pandas_3OK.csv")