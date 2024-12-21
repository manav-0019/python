# Phonebook program using dictionary
def display_menu():
    print("\nPhonebook Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

def is_valid_phone_number(phone_number):
    return phone_number.isdigit() and len(phone_number) == 10

def add_contact(phonebook):
    name = input("Enter contact name: ").strip()
    if name in phonebook:
        print("Contact already exists!")
    else:
        phone_number = input("Enter phone number: ").strip()
        if is_valid_phone_number(phone_number):
            phonebook[name] = phone_number
            print(f"Contact {name} added successfully!")
        else:
            print("Invalid phone number! Phone number must be exactly 10 digits.")

def search_contact(phonebook):
    name = input("Enter the name to search: ").strip()
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print("Contact not found!")

def update_contact(phonebook):
    name = input("Enter the name to update: ").strip()
    if name in phonebook:
        phone_number = input(f"Enter new phone number for {name}: ").strip()
        if is_valid_phone_number(phone_number):
            phonebook[name] = phone_number
            print(f"Contact {name} updated successfully!")
        else:
            print("Invalid phone number! Phone number must be exactly 10 digits.")
    else:
        print("Contact not found!")

def delete_contact(phonebook):
    name = input("Enter the name to delete: ").strip()
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")

def display_contacts(phonebook):
    if not phonebook:
        print("Phonebook is empty!")
    else:
        print("\nContacts:")
        for name in sorted(phonebook):
            print(f"{name}: {phonebook[name]}")


# Main program
if __name__ == "__main__":
    phonebook = {}
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_contact(phonebook)
        elif choice == "3":
            update_contact(phonebook)
        elif choice == "4":
            delete_contact(phonebook)
        elif choice == "5":
            display_contacts(phonebook)
        elif choice == "6":
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
