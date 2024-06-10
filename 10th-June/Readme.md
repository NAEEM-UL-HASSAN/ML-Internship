# Sales Data Cleaning and Analysis (Task # 1)
Task 1 is to clean and analyze a sales transactions dataset using pandas. It performs several tasks to prepare the data for analysis, extract useful insights, and export the cleaned data.

## Task 1 Overview

1. **Load the Dataset**: The script loads the dataset from a CSV file into a pandas DataFrame.
2. **Data Cleaning**: It removes any duplicate rows and rows with missing values to ensure data quality.
3. **Extract Relevant Columns**: Only the relevant columns for the analysis are extracted from the dataset.
4. **Calculate Total Sales**: The script calculates the total sales amount for each transaction by multiplying the quantity by the unit price.
5. **Category-wise Sales Calculation**: It computes the total sales amount for each product category.
6. **Identify Top-Selling Product**: The script identifies the top-selling product based on the total quantity sold.
7. **Generate Summary Report**: It generates a summary report with descriptive statistics for the numerical columns.
8. **Export Cleaned Data**: Finally, the cleaned and processed data is exported to a new CSV file.

## Prerequisites

Make sure you have the following libraries installed:

- pandas

You can install these libraries using pip:

```bash
pip install pandas
```

# Numerical Analysis with NumPy (Task # 2)

Task 2 involves performing numerical analysis on a dataset using NumPy. The script executes several tasks to process the data, including statistical calculations, normalization, outlier detection, and data reshaping.

## Task 2 Overview

1. **Load the Dataset**: The script loads the dataset from a CSV file into a NumPy array, skipping the first row which contains column headings.
2. **Calculate Mean, Median, and Standard Deviation**: It calculates the mean, median, and standard deviation for each column in the dataset.
3. **Normalize the Data**: The data is normalized using z-score normalization to standardize the dataset.
4. **Identify Outliers**: Outliers are identified using the Interquartile Range (IQR) method.
5. **Perform Element-wise Mathematical Operations**: The script performs element-wise addition, subtraction, multiplication, and division on the dataset.
6. **Reshape the Dataset**: The dataset is reshaped into a different dimension as required.
7. **Save the Processed Data**: Finally, the processed data is saved as a NumPy binary file.

## Prerequisites

Make sure you have the following library installed:

- numpy

You can install this library using pip:

```bash
pip install numpy
```

