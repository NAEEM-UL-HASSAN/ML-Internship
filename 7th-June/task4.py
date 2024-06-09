'The code synchronizes files by copying modified or missing files from source to target directory.'
import os
import shutil

class FileSynchronizer:
    """
    Class represent file synchronization tool that keeps files consistent in different directories.

    Attributes
    ----------
    source_dir : string
        The source directory to synchronize files from.
    target_dir : string
        The target directory to synchronize files to.
    """

    def __init__(self, source_dir, target_dir):
        """
        Initializes the FileSynchronizer with source and target directories.

        Parameters
        ----------
        source_dir : string
            The source directory.
        target_dir : string
            The target directory.
        """
        self.source_dir = source_dir
        self.target_dir = target_dir

    def synchronize_files(self):
        """
        Synchronizes files from the source directory to the target directory.

        Displays messages for each action performed.
        """
        print("Starting file synchronization...")

        source_files = os.listdir(self.source_dir)

        for file in source_files:
            source_file_path = os.path.join(self.source_dir, file)
            target_file_path = os.path.join(self.target_dir, file)

            if not os.path.exists(target_file_path) or \
               os.stat(source_file_path).st_mtime > os.stat(target_file_path).st_mtime:
                shutil.copy2(source_file_path, target_file_path)
                print(f"File '{file}' synchronized.")

        print("File synchronization completed.")

if __name__ == "__main__":
    SOURCE_DIRECTORY = "D:\\Source"
    TARGER_DIRECTORY = "D:\\Destination"

    synchronizer = FileSynchronizer(SOURCE_DIRECTORY, TARGER_DIRECTORY)
    synchronizer.synchronize_files()
