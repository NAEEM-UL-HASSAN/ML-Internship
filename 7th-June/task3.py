
'This program enables users to open, edit, and save files, perform search and replace operations.'

import re


class TextEditor:
    """
    Class  reprsent basic command-line text editor.

    Attributes
    ----------
        file_name : string
            The name of the file being edited.
        content : string
            The content of the file.
    """

    def __init__(self, file_name=None):
        """
        Initializes the text editor with optional filename.

        Parameters
        ----------
        file_name : string, optional
            The name of the file to open.
        """
        self.file_name = file_name
        self.content = ""

        if file_name:
            self.open_file()

    def open_file(self):
        """
        Opens a file and reads its content into the editor.
        """
        with open(self.file_name, 'r', encoding="utf-8") as file:
            self.content = file.read()

    def save_file(self):
        """
        Saves the content of the editor to a file.
        """
        with open(self.file_name, 'w', encoding="utf-8") as file:
            file.write(self.content)

    def edit_content(self, new_content):
        """
        Updates the content of the editor.

        Parameters
        ----------
        new_content : string
            The new content to set.
        """
        self.content = new_content

    def search_replace(self, search_str, replace_str):
        """
        Searches for a string in the content and replaces it with another string.

        Parameters
        ----------
        search_str : string
            The string to search for.
        replace_str : string
            The string to replace with.
        """
        self.content = re.sub(search_str, replace_str, self.content)

    def add_line_numbers(self):
        """
        Adds line numbers to the content.
        """
        lines = self.content.split('\n')
        numbered_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]
        self.content = '\n'.join(numbered_lines)

    def word_count(self):
        """
        Counts the number of words in the content.

        Returns
        -------
        int
            The word count.
        """
        words = re.findall(r'\w+', self.content)
        return len(words)


if __name__ == "__main__":
    FILE_NAME = '7th-June\\task3.txt'
    editor = TextEditor(FILE_NAME)

    print("Current content:")
    print(editor.content)

    CONTENT = 'Hello I am professional graphic designer. I have 5 years experience.'

    editor.edit_content(CONTENT)
    editor.save_file()

    print("\nUpdated content:")
    print(editor.content)

    count = editor.word_count()
    print(f"\nWord count: {count}")

    editor.search_replace("new", "modified")
    editor.add_line_numbers()
    count = editor.word_count()

    print("\nModified content with line numbers:")
    print(editor.content)

    print(f"\nWord count: {count}")
