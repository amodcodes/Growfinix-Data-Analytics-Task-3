import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load Dataset
df = pd.read_csv("data/tour_enquiries.csv")

# Step 2: Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Step 3: Dataset Information
print("\nDataset Information:")
print(df.info())

# Step 4: Dataset Shape
print("\nDataset Shape:")
print(df.shape)

print("\n--- DATA CLEANING STARTED ---")

# Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate Enquiry IDs

df = df.drop_duplicates(
    subset=["Enquiry_ID"]
)

print("\nAfter Removing Duplicates:")
print(df.shape)

# Fill missing age with median

df["Customer_Age"] = df["Customer_Age"].fillna(
    df["Customer_Age"].median()
)

# Fill missing income with median

df["Annual_Income_INR"] = df["Annual_Income_INR"].fillna(
    df["Annual_Income_INR"].median()
)

# Fill missing destination

df["Destination"] = df["Destination"].fillna(
    "Unknown"
)

# Convert columns into correct data types

df["Customer_Age"] = pd.to_numeric(
    df["Customer_Age"], errors="coerce"
)

df["Annual_Income_INR"] = pd.to_numeric(
    df["Annual_Income_INR"], errors="coerce"
)

print("\nUpdated Data Types:")
print(df.dtypes)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nData Cleaning Completed Successfully!")

# Step 5: Column Names
print("\nColumn Names:")
print(df.columns.tolist())

# STEP 5: EXPLORATORY DATA ANALYSIS

print("\n========== EDA STARTED ==========")

# 1. Most Popular Destinations

destination_counts = df["Destination"].value_counts()

print("\nMost Popular Travel Destinations:")
print(destination_counts)

print("\nTop 5 Destinations:")
print(destination_counts.head(5))

# 2. Customer Age Group Analysis

df["Age_Group"] = pd.cut(
    df["Customer_Age"],
    bins=[17, 25, 35, 45, 55, 100],
    labels=["18-25", "26-35", "36-45", "46-55", "56+"]
)

age_analysis = df["Age_Group"].value_counts().sort_index()

print("\nCustomers by Age Group:")
print(age_analysis)

# 3. Customer Income Analysis

df["Income_Bracket"] = pd.cut(
    df["Annual_Income_INR"],
    bins=[0, 30000, 60000, 100000, 150000, float("inf")],
    labels=[
        "Below 30k",
        "30k-60k",
        "60k-100k",
        "100k-150k",
        "150k+"
    ]
)

income_analysis = df["Income_Bracket"].value_counts().sort_index()

print("\nCustomers by Income Bracket:")
print(income_analysis)

# 4. Statistical Analysis

average_age = df["Customer_Age"].mean()

average_income = df["Annual_Income_INR"].mean()

median_income = df["Annual_Income_INR"].median()

print("\nAverage Customer Age:", round(average_age, 2))

print("Average Annual Income:", round(average_income, 2))

print("Median Annual Income:", round(median_income, 2))

# 5. Save EDA Results

destination_counts.to_csv(
    "outputs/destination_analysis.csv"
)

age_analysis.to_csv(
    "outputs/age_analysis.csv"
)

income_analysis.to_csv(
    "outputs/income_analysis.csv"
)

print("\nEDA Completed Successfully!")

# Step 6: Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# STEP 6: DATA VISUALIZATION

import os

os.makedirs("outputs", exist_ok=True)

# Chart 1: Popular Destinations

plt.figure(figsize=(10, 6))

destination_counts.plot(kind="bar")

plt.title("Most Popular Travel Destinations")
plt.xlabel("Travel Destination")
plt.ylabel("Number of Enquiries")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/popular_destinations.png")
plt.show()

# Chart 2: Age Distribution

plt.figure(figsize=(10, 6))

plt.hist(
    df["Customer_Age"],
    bins=15,
    edgecolor="black"
)

plt.title("Customer Age Distribution")
plt.xlabel("Customer Age")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("outputs/age_distribution.png")
plt.show()

# Chart 3: Customers by Age Group

plt.figure(figsize=(9, 5))

age_analysis.plot(kind="bar")

plt.title("Customers by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("outputs/age_groups.png")
plt.show()

# Chart 4: Customers by Income Bracket

plt.figure(figsize=(9, 5))

income_analysis.plot(kind="bar")

plt.title("Customers by Annual Income Bracket")
plt.xlabel("Income Bracket (INR)")
plt.ylabel("Number of Customers")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("outputs/income_brackets.png")
plt.show()

print("\nAll Charts Generated Successfully!")

# STEP 7: EXPORT FINAL DATA

df.to_csv(
    "outputs/cleaned_tour_enquiries.csv",
    index=False
)

print("Cleaned Dataset Exported Successfully!")

# Export Destination Analysis

destination_counts.to_csv(
    "outputs/destination_summary.csv"
)

# Export Age Analysis

age_analysis.to_csv(
    "outputs/age_group_summary.csv"
)

# Export Income Analysis

income_analysis.to_csv(
    "outputs/income_bracket_summary.csv"
)

print("All Summary Files Exported Successfully!")