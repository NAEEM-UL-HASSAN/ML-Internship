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

1. **Load the Dataset**: The script loads the dataset from a CSV file into a pandas DataFrame and then convert DataFrame to NumPy array.
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

# Data Visualization with Matplotlib (Task # 3)

Task 3 involves data visualization using Matplotlib with a dataset containing various passenger information from the Titanic. The dataset includes variables such as passenger ID, survival status, class, name, sex, age, number of siblings/spouses aboard, number of parents/children aboard, ticket number, fare, cabin, and port of embarkation. The goal is to create meaningful visualizations to understand and analyze the data better.

## Task 3 Overview

1. **Load the Dataset**: The dataset is loaded from a CSV file into a pandas DataFrame.
2. **Line Plot**: A line plot is created to visualize the trend of a specific variable over time. In this case, the trend of fare over passenger ID is plotted.
3. **Bar Chart**: A bar chart is generated to compare the distribution of a categorical variable. Here, the distribution of male and female is plotted.
4. **Scatter Plot**: A scatter plot is constructed to examine the relationship between two numerical variables, specifically PassengerId and Age.
5. **Histogram**: A histogram is designed to display the distribution of a continuous variable, in this case, Fare.
6. **Customization**: The visualizations are customized by adding appropriate labels, titles, and legends.
7. **Save Plots**: The generated plots are saved as image files (PNG format).


## Prerequisites

Make sure you have the following library installed:

- pandas
- matplotlib

You can install the required packages using pip:

```bash
pip install pandas matplotlib
```

# Advanced Data Visualization with Pandas and Matplotlib (Task # 4)

This task involves advanced data visualization using Pandas and Matplotlib. The code is designed to handle complex datasets, perform data preprocessing, generate various types of visualizations, and save the final visualization dashboard as a PDF document.

## Task 4 Overview

1. **Load the Dataset**: Load the dataset from a CSV file into a pandas DataFrame.
2. **Data Preprocessing**: Handle missing values in the dataset by replacing them with appropriate values (e.g., 0 for numerical columns). This ensures data cleanliness and prepares it for visualization.
3. **Create a Pivot Table**: Generate a pivot table to summarize the data, aggregating vaccination counts by country.
4. **Generate a Box Plot**: Create a box plot to compare the distributions of vaccination variables such as total vaccinations, people vaccinated, and people fully vaccinated across different categories (e.g., countries).
5. **Create a Stacked Area Chart**: Develop a stacked area chart to visualize the trend of vaccination variables over time, showing the composition of different variables over the specified time period.
6. **Develop a Heatmap**: Construct a heatmap to display the correlation matrix of numerical variables in the dataset, providing insights into the relationships between different variables.
7. **Combine Visualizations into a Dashboard**: Combine multiple visualizations (box plot, stacked area chart, heatmap) into a dashboard-like layout using Matplotlib's subplots. This layout provides a comprehensive view of the data and its patterns.
8. **Save the Visualization Dashboard**: Save the final visualization dashboard as a PDF document for easy sharing and reference.

## Prerequisites

Make sure you have the following library installed:

- pandas
- matplotlib
- seaborn

You can install the required packages using the following command:

```bash
pip install pandas matplotlib seaborn
```
