# Step 1: Import Libraries
import pandas as pd
import numpy as np

# Step 2: Load Dataset

df = pd.read_csv("E:\guvi\onlinefoodorder pro2\ONINE_FOOD_DELIVERY_ANALYSIS.csv")

print("First 5 rows:")
print(df.head())

print("\nOriginal Dataset Shape:")
print(df.shape)

print("\nColumn Data Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Step 3: Handle Missing Values

# Numerical columns - fill with median

df["Customer_Age"] = df["Customer_Age"].fillna(
    df["Customer_Age"].median()
)

df["Delivery_Time_Min"] = df["Delivery_Time_Min"].fillna(
    df["Delivery_Time_Min"].median()
)

df["Distance_km"] = df["Distance_km"].fillna(
    df["Distance_km"].median()
)

df["Order_Value"] = df["Order_Value"].fillna(
    df["Order_Value"].median()
)


# Categorical columns - fill with mode

df["Customer_Gender"] = df["Customer_Gender"].fillna(
    df["Customer_Gender"].mode()[0]
)

df["City"] = df["City"].fillna(
    df["City"].mode()[0]
)

df["Area"] = df["Area"].fillna(
    df["Area"].mode()[0]
)

df["Cuisine_Type"] = df["Cuisine_Type"].fillna(
    df["Cuisine_Type"].mode()[0]
)

df["Payment_Mode"] = df["Payment_Mode"].fillna(
    df["Payment_Mode"].mode()[0]
)


# Step 4: Check Missing Values

print("\nMissing Values After Basic Cleaning:")
print(df.isnull().sum())


# Step 5: Check and Handle Invalid Values


# Delivery Rating
print("\nInvalid Delivery Ratings:")

print(
    ((df["Delivery_Rating"] < 0) |
     (df["Delivery_Rating"] > 5)).sum()
)


# Restaurant Rating
print("\nInvalid Restaurant Ratings:")

print(
    ((df["Restaurant_Rating"] < 0) |
     (df["Restaurant_Rating"] > 5)).sum()
)

# Limit Restaurant Rating to maximum 5
df["Restaurant_Rating"] = df["Restaurant_Rating"].clip(upper=5)


# Negative values

print("\nNegative Profit Margin:",
      (df["Profit_Margin"] < 0).sum())

print("Negative Order Value:",
      (df["Order_Value"] < 0).sum())

print("Negative Delivery Time:",
      (df["Delivery_Time_Min"] < 0).sum())

print("Negative Distance:",
      (df["Distance_km"] < 0).sum())


# Step 6: Handle Cancellation Reason

# Cancelled orders without cancellation reason are marked as Unknown

df.loc[
    (df["Order_Status"] == "Cancelled") &
    (df["Cancellation_Reason"].isna()),
    "Cancellation_Reason"
] = "Unknown"


# Step 7: Handle Delivery Rating

# Cancelled orders should not have a delivery rating

df.loc[
    df["Order_Status"] == "Cancelled",
    "Delivery_Rating"
] = np.nan


# Step 8: Convert Order Date

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

print("\nOrder_Date Data Type:")
print(df["Order_Date"].dtype)

print("Missing Order_Date:",
      df["Order_Date"].isnull().sum())

print("Minimum Order Date:",
      df["Order_Date"].min())

print("Maximum Order Date:",
      df["Order_Date"].max())


# Step 9: Convert Order Time

df["Order_Time"] = pd.to_datetime(
    df["Order_Time"],
    errors="coerce"
).dt.time

print("\nOrder_Time Data Type:")
print(df["Order_Time"].dtype)

print("Missing Order_Time:",
      df["Order_Time"].isnull().sum())


# Step 10: Handle Discount Applied

# If no discount is recorded, consider it as 0

df["Discount_Applied"] = df["Discount_Applied"].fillna(0)


# Step 11: Calculate Final Amount

# Final Amount = Order Value - Discount

df["Final_Amount"] = (
    df["Order_Value"] -
    df["Discount_Applied"]
)

print("\nMissing Final_Amount:",
      df["Final_Amount"].isnull().sum())


# Step 12: Handle Peak Hour

# Missing Peak_Hour values are treated as False

df["Peak_Hour"] = df["Peak_Hour"].fillna(False)

print("\nMissing Peak_Hour:",
      df["Peak_Hour"].isnull().sum())


# Step 13: Final Missing Value Check

print("FINAL DATA QUALITY CHECK")

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

"""
# Step 14: Save Cleaned Dataset

df.to_csv(
    "food_delivery_cleaned.csv",
    index=False
)

print("CLEANING COMPLETED SUCCESSFULLY!")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("File: food_delivery_cleaned.csv")
"""