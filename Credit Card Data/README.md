# Credit Card Customer Data Analysis

## Overview

This project involves an in-depth analysis of a Kaggle dataset containing information on credit card customers. The goal is to gain insights into customer behavior and identify patterns through Exploratory Data Analysis (EDA) and clustering analysis. Findings and insights will be documented for potential business applications.

- **Dataset Source:** [Kaggle - Credit Card Customer Data](https://www.kaggle.com/datasets/arjunbhasin2013/ccdata?resource=download)
- **Rows:** 8,950
- **Columns:** 18

## Dataset Features

| Column Name                        | Description                                          | Data Type |
| ---------------------------------- | ---------------------------------------------------- | --------- |
| `CUST_ID`                          | Customer ID                                          | `object`  |
| `BALANCE`                          | Current balance                                      | `float64` |
| `BALANCE_FREQUENCY`                | Frequency of balance updates                         | `float64` |
| `PURCHASES`                        | Total purchase amount                                | `float64` |
| `ONEOFF_PURCHASES`                 | One-time purchase amount                             | `float64` |
| `INSTALLMENTS_PURCHASES`           | Installment purchases amount                         | `float64` |
| `CASH_ADVANCE`                     | Cash advance amount                                  | `float64` |
| `PURCHASES_FREQUENCY`              | Purchase frequency                                   | `float64` |
| `ONEOFF_PURCHASES_FREQUENCY`       | One-time purchase frequency                          | `float64` |
| `PURCHASES_INSTALLMENTS_FREQUENCY` | Installment purchase frequency                       | `float64` |
| `CASH_ADVANCE_FREQUENCY`           | Cash advance frequency                               | `float64` |
| `CASH_ADVANCE_TRX`                 | Number of cash advance transactions                  | `int64`   |
| `PURCHASES_TRX`                    | Number of purchase transactions                      | `int64`   |
| `CREDIT_LIMIT`                     | Credit limit                                         | `float64` |
| `PAYMENTS`                         | Total payments                                       | `float64` |
| `MINIMUM_PAYMENTS`                 | Minimum payments due                                 | `float64` |
| `PRC_FULL_PAYMENT`                 | Percentage of full payments                          | `float64` |
| `TENURE`                           | Number of months the customer has been with the bank | `int64`   |

## Project Structure

- **Data Preprocessing:** Data cleaning, handling missing values, and feature scaling.
- **Exploratory Data Analysis (EDA):** Visualizing data distributions, customer segmentation, and spending patterns.
- **Clustering Analysis:** Identifying clusters for customer segmentation using the optimal number of clusters (k=6).
- **Results and Insights:** Interpreting clusters and highlighting significant patterns.

## Analysis Summary

- **Data Cleaning:** Addressed missing values and outliers.
- **EDA Insights:**
  - Analyzed customer spending patterns in categories like one-time purchases, installment purchases, and cash advances.
  - Examined credit usage frequency, credit limits, and customer tenure.
- **Clustering Analysis:** Segmented customers into 6 clusters, offering insights into distinct customer groups based on behavior metrics.

## Key Findings

1. **High-Spending Customers:** Identified customers with high `BALANCE` and `PURCHASES`, suggesting potential for premium services.
2. **Credit Reliant Customers:** Segmented customers frequently using `CASH_ADVANCE` and high `CREDIT_LIMIT`, indicating reliance on credit.
3. **Installment Shoppers:** Customers with high `INSTALLMENTS_PURCHASES`, indicating a preference for payment installments.

## Future Work

- Expand analysis with predictive modeling for customer attrition.
- Include trend analysis on customers' payment behaviors to predict credit risk.
