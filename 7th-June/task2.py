'This program allows users to add, view, update, and delete contacts.'
class ContactManager:
    """
    Class representing a contact management system.

    Attributes
    ----------
    contacts : dictionary
        A dictionary to store contact information.
    """

    def __init__(self):
        """
        Initializes the ContactManager object with an empty contacts dictionary.
        """
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        """
        Adds a new contact to the contact list.

        Parameters
        ----------
        name : string
            The name of the contact.
        phone_number : string
            The phone number of the contact.
        email : string
            The email address of the contact.
        """
        self.contacts[name] = {'phone_number': phone_number, 'email': email}

    def view_contact(self, name):
        """
        Displays the contact information for a given name.

        Parameters
        ----------
        name : string
            The name of the contact to view.
        """
        if name in self.contacts:
            contact_info = self.contacts[name]
            print(f"Name: {name}")
            print(f"Phone Number: {contact_info['phone_number']}")
            print(f"Email: {contact_info['email']}")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name, phone_number=None, email=None):
        """
        Updates the contact information for a given name.

        Parameters
        ----------
        name : string
            The name of the contact to update.
        phone_number : string, optional
            The new phone number for the contact.
        email : string, optional
            The new email address for the contact.
        """
        if name in self.contacts:
            contact_info = self.contacts[name]
            if phone_number is not None:
                contact_info['phone_number'] = phone_number
            if email is not None:
                contact_info['email'] = email
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        """
        Deletes a contact from the contact list.

        Parameters:
        name : string
            The name of the contact to delete.
        """
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")


def main():
    """
    Main function to run the contact management system.
    """
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_manager.add_contact(name, phone_number, email)
        elif choice == '2':
            name = input("Enter name to view contact: ")
            contact_manager.view_contact(name)
        elif choice == '3':
            name = input("Enter name to update contact: ")
            phone_number = input("Enter new phone number (leave blank to keep existing): ")
            email = input("Enter new email (leave blank to keep existing): ")
            contact_manager.update_contact(name, phone_number, email)
        elif choice == '4':
            name = input("Enter name to delete contact: ")
            contact_manager.delete_contact(name)
        elif choice == '5':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
