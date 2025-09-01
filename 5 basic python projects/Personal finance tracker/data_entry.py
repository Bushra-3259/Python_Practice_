# -----------------------------
# 1) Imports
# -----------------------------

# Importing the datetime class from the datetime module
from datetime import datetime   
# 'from' and 'import' are Python keywords.
# 'datetime' (first one) is a standard library module that handles dates and times.
# 'datetime' (second one) is a class inside that module.
# We use this class to parse strings into dates, format dates, or get today’s date.

# -----------------------------
# 2) Constants / Globals
# -----------------------------

# Define a date format using Python's strftime/strptime directives
date_format = "%d-%m-%Y"        
# A string that specifies how dates should be formatted.
# "%d" → day as two digits, "%m" → month as two digits, "%Y" → full year (4 digits).
# Example: "29-08-2025"

# Define categories with a dictionary
CATEGORIES = {"I": "Income", "E": "Expense"} 
# {} creates a dictionary, which maps keys to values.
# "I" → "Income", "E" → "Expense"
# Dictionaries allow easy lookup: CATEGORIES["I"] returns "Income".

# -----------------------------
# 3) Helper Functions
# -----------------------------

# Function to get and validate a date
def get_date(prompt, allow_default=False):    
    # 'def' is a keyword to define a function.
    # prompt: message shown to user
    # allow_default: if True, user can press enter for today’s date

    date_str = input(prompt)                  
    # input() → built-in function, always returns a string.
    # Store user's input in date_str

    if allow_default and not date_str:        
        # 'and' is a logical operator; 'not' negates boolean.
        # Condition is True if user pressed enter (empty string) and default allowed.

        return datetime.today().strftime(date_format) 
        # datetime.today() → returns current date and time.
        # .strftime() → formats the date into a string using date_format.
        # return sends this string back to the caller.

    try:                                      
        # 'try' starts exception handling block

        valid_date = datetime.strptime(date_str, date_format)  
        # strptime() → parses string into datetime object according to format
        # Raises ValueError if format is wrong

        return valid_date.strftime(date_format)  
        # Convert datetime object back into formatted string
        # Ensures consistent formatting even if user entered correct but slightly different input
    except ValueError:                         
        # 'except' handles errors raised in try block

        print("Invalid date format. Please enter the date in the format dd-mm-yyyy.") 
        # Print message to user
        return get_date(prompt, allow_default) 
        # Recursively call function to retry until valid input

# Function to get and validate an amount
def get_amount():
    try:  
        amount = float(input("Enter the amount: "))  
        # Convert string input to float
        # Raises ValueError if input is not a number

        if amount <= 0:                       
            raise ValueError("Amount must be a non-negative non-zero value.") 
            # 'raise' throws a custom exception
            # Stops execution and jumps to except block

        return amount                         
        # Return valid float amount
    except ValueError as e:                    
        # 'as' assigns exception to variable e
        print(e)                               
        return get_amount()                    
        # Retry by calling function recursively

# Function to get and validate category
def get_category():
    category = input("Enter the category ('I' for income or 'E' for expense): ").upper()
    # input() → get user input as string
    # .upper() → convert input to uppercase, so 'i' → 'I', 'e' → 'E'

    if category in CATEGORIES:                 
        # 'in' checks if category exists as a key in dictionary
        return CATEGORIES[category]            
        # Lookup in dictionary, return "Income" or "Expense"

    print("Invalid category. Please enter 'I' for income or 'E' for expense.")  
    # Inform user of invalid input

    return get_category()                        
    # Recursively call function until valid input is given
    # (⚠️ Note: parentheses are required, otherwise it returns function itself)

# Function to get optional description
def get_description():
    return input("Enter a description (optional): ") 
    # Simply takes user input and returns it
    # Can be empty string ""
