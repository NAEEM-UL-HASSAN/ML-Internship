'Data Visualization with Matplotlib'

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load the dataset from a CSV file into a pandas DataFrame.

    Parameters
    ----------
    filepath : string
        The path to the CSV file.

    Returns
    -------
    pd.DataFrame
        The loaded dataset.
    """
    return pd.read_csv(file_path)

def line_plot(temp_data, x_col, y_col, title, xlabel, ylabel, file_name):
    """
    Create a line plot to visualize the trend of a specific variable over time.

    Parameters
    ----------
    data : pd.DataFrame
        The dataset containing the data to be plotted.
    x_col : string
        The column name to be used as the x-axis.
    y_col : string
        The column name to be used as the y-axis.
    title : string
        The title of the plot.
    xlabel : string
        The label for the x-axis.
    ylabel : string
        The label for the y-axis.
    filename : string
        The name of the file to save the plot as.

    Returns
    -------
    None
    """
    plt.figure()
    plt.plot(temp_data[x_col], temp_data[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(file_name)
    plt.close()

def bar_chart(temp_data, x_col, title, xlabel, ylabel, file_name):
    """
    Generate a bar chart to compare the distribution of a categorical variable.

    Parameters
    ----------
    data : pd.DataFrame
        The dataset containing the data to be plotted.
    x_col : string
        The column name to be used for the categories.
    title : string
        The title of the plot.
    xlabel : string
        The label for the x-axis.
    ylabel : string
        The label for the y-axis.
    filename : string
        The name of the file to save the plot as.

    Returns
    -------
    None
    """
    plt.figure()
    temp_data[x_col].value_counts().plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(file_name)
    plt.close()

def scatter_plot(temp_data, x_col, y_col, title, xlabel, ylabel, file_name):
    """
    Construct a scatter plot to examine the relationship between two numerical variables.

    Parameters
    ----------
    data : pd.DataFrame
        The dataset containing the data to be plotted.
    x_col : string
        The column name to be used as the x-axis.
    y_col : string
        The column name to be used as the y-axis.
    title : string
        The title of the plot.
    xlabel : string
        The label for the x-axis.
    ylabel : string
        The label for the y-axis.
    filename : string
        The name of the file to save the plot as.

    Returns
    -------
    None
    """
    plt.figure()
    plt.scatter(temp_data[x_col], temp_data[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(file_name)
    plt.close()

def histogram(temp_data, x_col, title, xlabel, ylabel, file_name):
    """
    Design a histogram to display the distribution of a continuous variable.

    Parameters
    ----------
    data : pd.DataFrame
        The dataset containing the data to be plotted.
    x_col : string
        The column name to be used for the histogram.
    title : string
        The title of the plot.
    xlabel : string
        The label for the x-axis.
    ylabel : string
        The label for the y-axis.
    filename : string
        The name of the file to save the plot as.

    Returns
    -------
    None
    """
    plt.figure()
    plt.hist(temp_data[x_col].dropna(), bins=30)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(file_name)
    plt.close()

def main():
    'Data Visualization using Matplotlib'
    # Load the dataset
    filepath = 'Task3.csv'
    data = load_data(filepath)

    # Create visualizations
    line_plot(data, 'PassengerId', 'Fare', 'Fare Trend Over Time', 'Passenger ID', 'Fare',
    'line_plot.png')
    bar_chart(data, 'Sex', 'Gender Distribution', 'Gender', 'Count', 'bar_chart.png')
    scatter_plot(data, 'PassengerId', 'Age', 'PassengerId vs Age', 'PassengerId', 'Age',
    'scatter_plot.png')
    histogram(data, 'Fare', 'Fare Distribution', 'Fare', 'Frequency', 'histogram.png')

if __name__ == "__main__":
    main()
