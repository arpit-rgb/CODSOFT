# contact_book.py

import os

CONTACTS_FILE = "contacts.txt"

# Helper to load contacts from file
def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, phone, email, address = line.strip().split("|")
                contacts.append({
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "address": address
                })
    return contacts

# Helper to save contacts back to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            line = f"{contact['name']}|{contact['phone']}|{contact['email']}|{contact['address']}\n"
            file.write(line)

# Add new contact
def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    print("\n--- Contact List ---")
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

# Search for a contact
def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone number to search: ").strip()
    contacts = load_contacts()
    found = False

    for contact in contacts:
        if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
            print("\nContact Found:")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True

    if not found:
        print("No matching contact found.")

# Update contact
def update_contact():
    print("\n--- Update Contact ---")
    name_to_update = input("Enter the name of the contact to update: ").strip()
    contacts = load_contacts()
    found = False

    for contact in contacts:
        if contact["name"].lower() == name_to_update.lower():
            print("Leave field empty to keep current value.")
            new_name = input(f"New Name [{contact['name']}]: ").strip()
            new_phone = input(f"New Phone [{contact['phone']}]: ").strip()
            new_email = input(f"New Email [{contact['email']}]: ").strip()
            new_address = input(f"New Address [{contact['address']}]: ").strip()

            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            save_contacts(contacts)
            print("Contact updated successfully.")
            found = True
            break

    if not found:
        print("Contact not found.")

# Delete contact
def delete_contact():
    print("\n--- Delete Contact ---")
    name_to_delete = input("Enter the name of the contact to delete: ").strip()
    contacts = load_contacts()
    updated_contacts = [c for c in contacts if c["name"].lower() != name_to_delete.lower()]

    if len(updated_contacts) != len(contacts):
        save_contacts(updated_contacts)
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main program loop
def main():
    while True:
        print("\n====== Contact Book ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
