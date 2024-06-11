'Data Visualization using Pandas and Matplotlib'
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_dataset(file_path):
    """
    Load the dataset from a CSV file into a pandas DataFrame.

    Parameters
    ----------
    file_path : str
        The path to the CSV file.

    Returns
    -------
    pd.DataFrame
        The loaded dataset.
    """
    return pd.read_csv(file_path)


def preprocess_data(dataframe):
    """
    Perform data preprocessing tasks such as handling missing values.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The dataset to be preprocessed.

    Returns
    -------
    pd.DataFrame
        The preprocessed dataset.
    """
    dataframe.fillna(0, inplace=True)
    return dataframe


def create_pivot_table(dataframe):
    """
    Create a pivot table to summarize the data.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The dataset to be summarized.

    Returns
    -------
    pd.DataFrame
        The pivot table.
    """
    return pd.pivot_table(dataframe, index='country',
                          values=['total_vaccinations',
                                  'people_vaccinated', 'people_fully_vaccinated'],
                                  aggfunc='sum')


def generate_box_plot(dataframe):
    """
    Generate a box plot to compare the distributions of vaccination variables.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The dataset containing vaccination variables.

    Returns
    -------
    None
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=dataframe[['total_vaccinations',
                'people_vaccinated', 'people_fully_vaccinated']])
    plt.title('Boxplot of Vaccination Variables')
    plt.xlabel('Variables')
    plt.ylabel('Values')
    plt.show()
    plt.close()


def generate_stacked_area_chart(dataframe):
    """
    Create a stacked area chart to visualize vaccination variables over time.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The dataset containing vaccination variables and date.

    Returns
    -------
    None
    """
    plt.figure(figsize=(10, 6))
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    dataframe.set_index('date', inplace=True)
    dataframe[['total_vaccinations', 'people_vaccinated',
               'people_fully_vaccinated']].plot(kind='area', stacked=True)
    plt.title('Stacked Area Chart of Vaccination Variables Over Time')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.show()
    plt.close()


def generate_heatmap(dataframe):
    """
    Create a heatmap to display the correlation matrix of numerical variables.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The dataset containing numerical variables.

    Returns
    -------
    None
    """
    plt.figure(figsize=(10, 6))
    numeric_df = dataframe.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap of Numerical Variables')
    plt.show()
    plt.close()


def create_visualization_dashboard(dataframe):
    """
    Combine multiple visualizations into a dashboard-like layout using Matplotlib's subplots.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The dataset containing vaccination and numerical variables.

    Returns
    -------
    None
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Box plot
    sns.boxplot(data=dataframe[[
                'total_vaccinations', 
                'people_vaccinated','people_fully_vaccinated']], ax=axes[0, 0])
    axes[0, 0].set_title('Boxplot of Vaccination Variables')

    # Stacked area chart
    dataframe[['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']].plot(
        kind='area', stacked=True, ax=axes[0, 1])
    axes[0, 1].set_title(
        'Stacked Area Chart of Vaccination Variables Over Time')

    # Heat map
    numeric_df = dataframe.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=axes[1, 0])
    axes[1, 0].set_title('Correlation Heatmap of Numerical Variables')

    # Remove empty subplot
    fig.delaxes(axes[1, 1])

    plt.tight_layout()
    plt.show()
    plt.close()

def save_visualization_dashboard(dataframe, filename):
    """
    Save the final visualization dashboard as a PDF document.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The dataset containing vaccination and numerical variables.
    filename : str
        The filename for the saved PDF document.

    Returns
    -------
    None
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Box plot
    sns.boxplot(data=dataframe[[
                'total_vaccinations',
                'people_vaccinated','people_fully_vaccinated']],ax=axes[0, 0])
    axes[0, 0].set_title('Boxplot of Vaccination Variables')

    # Stacked area chart
    dataframe[['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']].plot(
        kind='area', stacked=True, ax=axes[0, 1])
    axes[0, 1].set_title(
        'Stacked Area Chart of Vaccination Variables Over Time')

    # Heat map
    numeric_df = dataframe.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=axes[1, 0])
    axes[1, 0].set_title('Correlation Heatmap of Numerical Variables')

    # Remove empty subplot
    fig.delaxes(axes[1, 1])

    plt.tight_layout()
    plt.savefig(filename)


def main():
    """
    Main function to perform data visualization tasks using Pandas and Matplotlib.

    Returns
    -------
        None
    """
    # Step 1: Load the dataset into a pandas DataFrame
    df = load_dataset("Task4.csv")

    # Step 2: Data preprocessing
    df = preprocess_data(df)

    # Step 3: Create a pivot table
    create_pivot_table(df)

    # Step 4: Generate a box plot
    generate_box_plot(df)

    # Step 5: Create a stacked area chart
    generate_stacked_area_chart(df)

    # Step 6: Develop a heat map
    generate_heatmap(df)

    # Step 7: Create visualization dashboard
    create_visualization_dashboard(df)

    # Step 8: Save the final visualization dashboard as a PDF document
    save_visualization_dashboard(df, "visualization.pdf")


if __name__ == "__main__":
    main()
