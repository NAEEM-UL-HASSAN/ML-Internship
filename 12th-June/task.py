'Read all files, folders, sub-folders, and sub-files within a directory'

import os
import pandas as pd
import matplotlib.pyplot as plt

def gather_file_metadata(directory):
    """
    Recursively gather metadata for all files within the directory.

    Parameters
    ----------
    directory : str
        Path to the directory to read.

    Returns
    -------
    pd.DataFrame
        DataFrame containing metadata for each file including file name,
        file size, folder size, number of files in the folder, and parent folder name.
    """
    file_records = []

    for root, dirs, files in os.walk(directory):
        folder_size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
        num_files = len(files)
        parent_folder = os.path.basename(root)
        dirs = ""
        print(dirs)
        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            file_records.append({
                'parent_folder': parent_folder,
                'file_name': name,
                'file_size': file_size,
                'folder_size': folder_size,
                'num_of_files_in_parent_folder': num_files,
                'file_extension': os.path.splitext(name)[1]  
            })

    df = pd.DataFrame(file_records)
    return df

def sort_and_summarize(df):
    """
    Sort DataFrame by file extension and generate summary.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing file metadata.

    Returns
    -------
    pd.DataFrame
        Sorted DataFrame.
    pd.DataFrame
        Summary DataFrame.
    """
    df_sorted = df.sort_values(by='file_extension')
    summary = df.groupby('file_extension').agg(
        total_files=('file_name', 'count'),
        total_size=('file_size', 'sum')
    ).reset_index()
    return df_sorted, summary

def save_results(df, summary, output_dir):
    """
    Save the results to CSV files.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing sorted file metadata.
    summary : pd.DataFrame
        DataFrame containing the summary of file metadata.
    output_dir : str
        Directory to save the CSV files.
    """
    df.to_csv(os.path.join(output_dir, 'file_metadata.csv'), index=False)
    summary.to_csv(os.path.join(output_dir, 'summary.csv'), index=False)

def visualize_summary(summary, output_dir):
    """
    Create and save visualization of the summary.

    Parameters
    ----------
    summary : pd.DataFrame
        DataFrame containing the summary of file metadata.
    output_dir : str
        Directory to save the visualization.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(summary['file_extension'], summary['total_size'], color='blue')
    plt.xlabel('File Extension')
    plt.ylabel('Total Size (MBs)')
    plt.title('Total Size by File Extension')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'summary.png'))
    plt.show()

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    output_directory = input("Enter the output directory path: ")

    metadata_df = gather_file_metadata(directory_path)
    sorted_df, summary_df = sort_and_summarize(metadata_df)

    save_results(sorted_df, summary_df, output_directory)
    visualize_summary(summary_df, output_directory)
