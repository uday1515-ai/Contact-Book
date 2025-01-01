Contact Book

Project Description:

A Contact Book is a software application that allows users to store, manage, and organize contact information such as names, phone numbers, email addresses, and other relevant details. It serves as a digital version of an address book or phonebook, enabling users to easily access, update, or delete their contact information. A contact book can be particularly useful for both personal and professional purposes, helping individuals manage relationships and communications efficiently.
Key Features:
1)	Add Contact:
•  Allows users to input new contact details such as name, phone number, and email address.
•  Each contact is saved and stored in a system, making it easy to retrieve at any time.

2)	View Contacts:
•  Displays a list of all stored contacts, showing relevant details such as name, phone number, and email address.
•  Helps users quickly access their contact information without needing to search elsewhere.

3)	Search Contact:
•  Provides the ability to search for a contact by name or other information.
•  Saves time by enabling users to quickly find specific contacts instead of scrolling through an entire list.

4)	Update Contact:
•  Allows users to modify existing contact details, such as changing a phone number or updating an email address.
•  Ensures that the contact information is always up to date.

5)	Delete Contact:
•  Enables users to remove contacts from the book, helping to maintain an accurate and relevant list.
•  Provides control over the contacts stored, allowing for efficient management.

6)	Save & Load Contacts:
•  The contact book typically saves contact data to a file (e.g., using a file format like pickle, json, or txt), so the information is not lost when the program is closed.
•  Upon restarting, the program can load the previously saved contacts, ensuring that data persists across sessions.

Team members:

1)Uday Todmal
2)Rushikesh Yadav
3)Pratik Sangale

Project Phases:

Developing a Contact Book application follows a structured approach that ensures the final product is functional, user-friendly, and efficient. Below are the typical project phases involved in the development of a Contact Book project:

1. Planning and Requirements Gathering

Objective: Understand the project goals, define the scope, and gather detailed requirements.

Tasks:

•	Define the Purpose: Understand the need for the contact book (e.g., managing personal or business contacts).
•	Identify Stakeholders: Determine who will be using the application (e.g., individual users, businesses) and gather feedback on their needs.
•	List Functional Requirements: Define key features such as adding, viewing, editing, searching, and deleting contacts.
•	List Non-functional Requirements: Identify system constraints such as performance, reliability, security, and user interface preferences.
•	Set Project Scope: Outline the features and functionality that will be included in the first version of the application.
•	Timeline and Milestones: Set a project timeline with key milestones (e.g., requirements finalization, development completion, testing phase).

2. System Design

Objective: Plan the architecture, data structure, and user interface for the application.

Tasks:

•	Architecture Design: Decide on the overall structure of the application (e.g., modular design with separate components for contact management, file handling, and user interface).
o	Determine how data will be stored (e.g., using files like Pickle/JSON or a database).
o	Design the flow of information between components (e.g., adding, editing, and deleting contacts).
•	Data Structure Design: Plan how contact information will be stored in memory (e.g., a dictionary, list, or class-based structure) and how data will be serialized and saved.

3. Development

Objective: Implement the features and functionality of the Contact Book application.

Tasks:
•	Set Up Development Environment: Set up necessary tools, libraries, and development environments (e.g., Python, Pickle/JSON).
•	Core Features Implementation:
o	Contact Class: Create a class to represent a contact with attributes like name, phone number, and email.
o	Add Contact: Implement the functionality to add new contacts.
o	View Contacts: Create a function to display a list of all contacts.
o	Search Contact: Allow searching for a contact by name or other attributes.
o	Update Contact: Implement the ability to modify contact details.
o	Delete Contact: Allow users to delete contacts from the list.
•	Persistence Layer:
o	Implement functionality to save contacts to a file (Pickle/JSON) and load them when the application restarts.
•	Data Validation: Ensure user input is validated (e.g., phone number format, email format).

4. Testing

Objective: Ensure the application is functioning as expected and meets the requirements.

Tasks:

•	Unit Testing: Test individual functions and components to ensure they work as intended (e.g., adding a contact, searching for contacts).
•	Integration Testing: Test how different components of the application interact with each other (e.g., adding a contact should reflect in the contact list, and saved contacts should load correctly).
•	Usability Testing: Test the user interface to ensure it is intuitive and easy to navigate. For example, ask potential users to interact with the app and provide feedback.
•	Error Handling: Test how the application handles edge cases (e.g., invalid inputs, empty fields, or file loading errors).

5. Deployment

Objective: Prepare the Contact Book for release and make it available for users.

Tasks:
•	Final Code Cleanup: Ensure all code is clean, efficient, and free of bugs. Document the code to ensure others can maintain it.
•	Packaging: If applicable, package the application into an executable file (e.g., using PyInstaller for Python) or prepare the source code for distribution.
•	Deployment on Platforms: If the contact book is a desktop application, prepare installation packages for different operating systems (Windows, macOS, Linux). If it's a web-based app, deploy it to a hosting platform.
•	Release to Users: Provide users with instructions on how to install and use the application. For example, upload the executable to a website or share it through other means.

6. Maintenance and Updates

Objective: Continuously improve the application by fixing bugs, adding new features, and enhancing performance.

Tasks:

•	Bug Fixing: Address any issues or bugs reported by users after the application is released.
•	Feature Enhancements: Based on user feedback, add new features to improve functionality (e.g., exporting contacts to CSV, implementing backups).
•	Performance Optimization: Optimize the application for better performance, especially if the contact list grows.
•	Security Updates: If sensitive data is stored, implement security measures like encryption, password protection, or data anonymization.

Technical Requirements:

These describe the specific tools, technologies, and systems needed to implement the Contact Book:
1.	Programming Language:
o	Python is commonly used for developing a contact book due to its simplicity and readability.
o	Alternatively, you could use other programming languages depending on your preference or platform, such as JavaScript (for web apps), Java, C#, or Ruby.

2.	File Storage:
o	Pickle: For serializing Python objects (like the contact dictionary) and saving them to a file.
o	JSON: For storing contacts in a human-readable format. It’s easier to modify manually and can be used across different programming languages.
o	Text Files: For storing plain text contact data, though this may be less structured and harder to scale.

3.	Data Validation:
o	Regular Expressions (Regex): To validate phone numbers and email addresses, ensuring they meet standard formats (e.g., using the re module in Python).

4.	Error Handling:
o	Exception Handling: Ensure the application handles common issues like missing files or incorrect inputs gracefully using try-except blocks.
How it Works:
•	The program starts by creating an instance of the ContactBook class. This instance automatically attempts to load any existing contacts from contacts.pkl.
•	The menu function is the main driver, displaying options to the user and calling the corresponding methods based on the user's input.
•	The program allows you to:
o	Add new contacts
o	View all contacts
o	Search for contacts by name
o	Update contact information (phone/email)
o	Delete contacts
o	Save and load contacts from a pickle file (to persist data across sessions)

Sample Interaction:

--- Contact Book ---
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Save Contacts
7. Exit
Enter your choice: 1
Enter name: Uday Todmal
Enter phone: 8208703115
Enter email: udaytodmal007@gmail.com
Contact for Uday Todmal added successfully.


--- Contact Book ---
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Save Contacts
7. Exit
Enter your choice: 2

Name: Uday Todmal , Phone: 8208703115, Email:udaytodmal007@gmail.com

