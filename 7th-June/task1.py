'This program allows the user to encrypt/decrypt a file using the Caesar cipher algorithm.'

import tkinter as tk
from tkinter import filedialog

def encrypt(text, shift):
    """
    Encrypts the given text using the Caesar cipher.

    Parameters
    ----------
    text : string
        The text to be encrypted.
    shift : int
        The shift value for encryption.

    Returns
    -------
    string
        The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """
    Decrypts the given text using the Caesar cipher.

    Parameters
    ----------
    text : string
        The text to be decrypted.
    shift : int
        The shift value for decryption.

    Returns
    -------
    string
        The decrypted text.
    """
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    """
    Main function to run the file encryption/decryption program.
    """
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select a file for encryption/decryption")
    with open(file_path, encoding="utf-8") as file:
        original_text = file.read()

    shift = int(input("Enter the shift value for encryption/decryption (e.g., 3): "))

    encrypted_text = encrypt(original_text, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print("Original Text:")
    print(original_text)
    print("\nEncrypted Text:")
    print(encrypted_text)
    print("\nDecrypted Text:")
    print(decrypted_text)

if __name__ == "__main__":
    main()
