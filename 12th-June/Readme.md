# Directory File Metadata Analyzer

## Description

This Repo provides a program to recursively read all files, folders, sub-folders, and sub-files within a specified directory. It generates a record for each file, containing metadata such as the file name, file size, folder size, number of files in the folder, and the parent folder name. The records are then sorted according to file extension, and a final summary of the results is displayed. The results are also saved to CSV files, and a visualization of the final result is created.

## Prerequisites

Make sure you have the following library installed:

- pandas
- matplotlib

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/NAEEM-UL-HASSAN/ML-Internship.git
    ```

2. Navigate to the project directory:
    ```bash
    cd 12th-June
    ```

3. Install the required Python packages:
    ```bash
    pip install pandas matplotlib
    ```

## Usage

1. Run the script:
    ```bash
    python task.py
    ```

2. When prompted, enter the path to the directory you want to analyze.

3. When prompted, enter the path to the output directory where the results will be saved.

## Output

The script will generate the following output files in the specified output directory:

1. `file_metadata.csv`: Contains metadata for each file including file name, file size, folder size, number of files in the folder, file extension, and parent folder name.
2. `summary.csv`: Contains a summary of the total number of files and their total size per file extension.
3. `summary.png`: A bar chart visualization of the total file sizes by file extension.