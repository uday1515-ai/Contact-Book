import pickle

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()
    
    def add_contact(self, contact):
        self.contacts[contact.name] = contact
        print(f"Contact for {contact.name} added successfully.")
    
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts.values():
                print(contact)
    
    def search_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(contact)
        else:
            print(f"Contact with name {name} not found.")
    
    def update_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(f"Updating contact for {name}.")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            contact.phone = new_phone
            contact.email = new_email
            print("Contact updated successfully.")
        else:
            print(f"Contact with name {name} not found.")
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact for {name} deleted successfully.")
        else:
            print(f"Contact with name {name} not found.")
    
    def save_contacts(self):
        with open("contacts.pkl", "wb") as f:
            pickle.dump(self.contacts, f)
        print("Contacts saved successfully.")
    
    def load_contacts(self):
        try:
            with open("contacts.pkl", "rb") as f:
                self.contacts = pickle.load(f)
        except FileNotFoundError:
            self.contacts = {}
    
    def menu(self):
        while True:
            print("\n--- Contact Book ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Save Contacts")
            print("7. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                contact = Contact(name, phone, email)
                self.add_contact(contact)
            
            elif choice == "2":
                self.view_contacts()
            
            elif choice == "3":
                name = input("Enter name to search: ")
                self.search_contact(name)
            
            elif choice == "4":
                name = input("Enter name to update: ")
                self.update_contact(name)
            
            elif choice == "5":
                name = input("Enter name to delete: ")
                self.delete_contact(name)
            
            elif choice == "6":
                self.save_contacts()
            
            elif choice == "7":
                print("Exiting the contact book.")
                break
            
            else: 
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu() 
