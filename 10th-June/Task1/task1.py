'Data Manipulation with pandas'
import pandas as pd


def main():
    """
    Main function to perform the data manipulation using pandas library.

    Parameters
    ----------  
    None

    Returns
    -------
    None
    """

    # 1. Load the dataset into a pandas DataFrame
    try:
        df = pd.read_csv("sales_data_sample.csv", encoding='latin1')
    except UnicodeDecodeError:
        df = pd.read_csv("sales_data_sample.csv", encoding='iso-8859-1')
    print("Data loaded successfully!")

    # Print the first 5 rows of the dataframe
    print("\nData Sample:")
    print(df.head())

    # 2. Remove any duplicate rows or missing values
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    print("\nRemoving duplicates and null values successfully!")

    # 3. Extract a subset of columns that are relevant to the analysis
    relevant_columns = ['ORDERNUMBER', 'QUANTITYORDERED',
                        'PRICEEACH', 'SALES', 'PRODUCTLINE']
    df = df[relevant_columns]
    print("\nSelected relevant columns successfully!")

    # 4. Calculate the total sales amount for each category
    category_sales = df.groupby('PRODUCTLINE')['SALES'].sum().reset_index()
    print("\nCategory wise sales:")
    print(category_sales)

    # 5. Identify the top-selling product and its sales quantity
    top_selling_product = df.groupby('PRODUCTLINE')['QUANTITYORDERED'].sum(
    ).reset_index().sort_values(by='QUANTITYORDERED', ascending=False).iloc[0]
    print("\nTop selling product:")
    print(top_selling_product)

    # 6. Generate a summary report with descriptive statistics for numerical columns
    summary_report = df.describe()
    print("\nSummary Report:")
    print(summary_report)

    # 7. Export the cleaned and processed data to a new CSV file
    df.to_csv('cleaned_sales_data.csv', index=False)
    print("\nData saved successfully!")


if __name__ == "__main__":
    main()
