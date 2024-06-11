' Numerical Analysis with NumPy'

import numpy as np
import pandas as pd


def main():
    """
    Main function to perform the numerical analysis using NumPy library.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    # Load the dataset into a pandas DataFrame
    df = pd.read_csv("Task2.csv")
    print(df.head())

    # Select only the numeric columns from the DataFrame
    numeric_df = df.select_dtypes(include=[np.number])

    # Convert the DataFrame to a NumPy array
    data = numeric_df.to_numpy()
    print(data.shape)

    # Calculate mean, median, and standard deviation
    mean_value = np.mean(data, axis=0)
    median_value = np.median(data, axis=0)
    std_deviation = np.std(data, axis=0)

    # Normalize the data using z-score normalization
    normalized_data = (data - mean_value) / std_deviation

    # Identify outliers using IQR method
    q1 = np.percentile(data, 25, axis=0)
    q3 = np.percentile(data, 75, axis=0)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = (data < lower_bound) | (data > upper_bound)

    # Perform element-wise mathematical operations
    data_addition = data + 10
    data_subtraction = data - 5
    data_multiplication = data * 2
    data_division = data / 3

    # Reshape the dataset into a different dimension
    new_shape = (data.shape[0], data.shape[1])
    reshaped_data = np.reshape(data, new_shape)

    # Save the processed data as a NumPy binary file
    np.savez('Task2_processed_data.npz', mean=mean_value, median=mean_value,
            std_deviation=std_deviation, normalization=normalized_data, outliers=outliers,
            addition=data_addition, subtraction=data_subtraction,
            multiplication=data_multiplication, division=data_division, reshaped_data=reshaped_data)

    # Print results for verification
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Standard Deviation: {std_deviation}")
    print(f"Outliers: {data[outliers]}")  # Prints outliers
    print(f"Data after addition:\n{data_addition}")
    print(f"Data after subtraction:\n{data_subtraction}")
    print(f"Data after multiplication:\n{data_multiplication}")
    print(f"Data after division:\n{data_division}")
    print(f"Reshaped data shape: {reshaped_data.shape}")


if __name__ == "__main__":
    main()
