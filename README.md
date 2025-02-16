# Company Interest List
A Python CLI application to manage a list of companies a user is interested in. Part of the Capital Group - ITG Internship Interview Task.

**Features:**
- **Add a Company** → Users can add a company to their interest list
- **Remove a Company** → Users can remove a company from the list.
- **Display Companies** → Displays all companies in a numbered format.
- **Error Handling** → Ensures valid inputs, prevents empty inputs and non-numeric inputs in the menu.
- **Case-Insensitive Matching** → Prevents duplicate entries and allows case-insensitive removal of companies.

**Requirements:**
- Python 3

**How to run:**
- Download the Python script (company_interest_list.py).
- Run the script in your chosen IDE (e.g. VS Code, PyCharm)
- Use the terminal/shell to use the program

**Case-Insensitive Functionality:**
This application prevents duplicate entries and allows case-insensitive removal of companies.  
- When adding a company, the system checks for existing names regardless of case.
- When removing a company, users can enter the name in any case, and it will still match the stored name.

**Example:**
```
Enter the company name to add: Tesla
Tesla has been added successfully!

Enter the company name to add: tesla
Tesla is already in the list.  # Duplicate prevented (case-insensitive)
```
```
Enter the company name to remove: TESLA
Tesla has been removed successfully!  # Case-insensitive match found and removed
```
