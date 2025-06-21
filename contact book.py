def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, details in contacts.items():
        print("\nName:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])


def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name in contacts:
        phone = input("Enter new phone (leave blank to keep current): ").strip()
        email = input("Enter new email (leave blank to keep current): ").strip()
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print("Contact updated.")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete {name}? (y/n): ").lower()
        if confirm == 'y':
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Delete cancelled.")
    else:
        print("Contact not found.")


def main():
    contacts = {}

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
