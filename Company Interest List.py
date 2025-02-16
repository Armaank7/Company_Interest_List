# Author: Armaan Khan
# Capital Group - ITG Internship Interview Task

companies = [] # Stores the list of comapnies 

def menu():
    """Displays the menu for the user to navigate through the app"""
    while True:
        print("\nCompany Interest List Menu:")
        print("1. Add a company")
        print("2. Remove a company")
        print("3. Display all companies")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice < 1 or choice > 4:    # Ensures that user can only choose a valid option (1-4)
                print("Invalid choice! Please enter a number between 1-4.")
            else:
                return choice   # Returns valid user choice 
        except ValueError:  # Handles a non-numeric input from the user
            print("Invalid choice! Please enter a number.")


def add_company():
    """Adds a company to the list of companies, if it doesn't already exist"""
    company = input("Enter the company name to add: ").strip()  # Allows user to input company to add, removes extra whitespaces

    if company == "": 
        print("Company name cannot be empty!")
        return  # Prevents empty company names from being added, returns user to menu

    for i in companies:     # Iterates through list of companies to check for duplicates
        if i.lower() == company.lower():    # Converts both stored and inputted company names to lowercase
            print(company + " is already in the list.")
            return

    companies.append(company)     # Adds the company to the list
    print(company + " has been added successfully!")


def remove_company():
    """Removes a company from the list of companies, if it already exists"""
    if len(companies) == 0:     # Checks that the list is empty before attempting to remove
        print("The company list is empty - nothing to remove.")
        return
    company = input("Enter the company name to remove: ").strip()   # Allows user to input company to remove, removes extra whitespaces
    if company == "":
        print("Company name cannot be empty!")
        return  # Prevents empty input and returns to the menu without making changes


    for i in companies:     # Iterates through list of companies to check for duplicates
        if i.lower() == company.lower():    # Converts both stored and inputted company names to lowercase
            companies.remove(i)     # Removes matching company from list
            print(i + " has been removed successfully!")
            return  
    else:
        print(company + " is not in the list.")     # Message if company not in list, returns to menu


def display_companies():
    """Displays all the companies in the list in a clear, numbered format"""
    if len(companies) == 0:     # Checks if list is empty before displaying, returns to menu if it is empty
        print("No companies in the list.")
        return

    print("\nCompany Interest List:")
    for i, company in enumerate(companies, start=1):    # Iterates through list of companies, assigns each company a number
        print(str(i) + ". " + company)     # Displays companies with their number

# Main program - loop that runs until user selects the exit option (4)
while True:
    option = menu()
    # Performs corresponding action based on the user's choice
    if option == 1:
        add_company()
    elif option == 2:
        remove_company()
    elif option == 3:
        display_companies()
    elif option == 4:
        print("Goodbye!")
        break   # Terminates program