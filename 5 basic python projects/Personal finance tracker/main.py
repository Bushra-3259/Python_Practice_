"""
A tiny Personal Finance CSV helper — with exhaustive, line-by-line comments.
This file explains every construct used: keywords, built-ins, modules, and why each is here.
"""

# -----------------------------
# 1) Imports
# -----------------------------

import pandas as pd  # 'import' loads a module. pandas is a third-party library for tabular data.
                     # 'as pd' creates a short alias to use pd.read_csv(), pd.DataFrame(), etc.

import csv           # csv is a standard library module for reading/writing CSV files.

from datetime import datetime  # 'from' and 'import' are keywords.
                               # datetime (class) comes from the built-in datetime module.
                               # Used to parse string dates → datetime objects and back.

from data_entry import get_amount, get_category, get_date, get_description
# Import helper functions from data_entry.py that interact with the user for input.

import matplotlib.pyplot as plt
# Import pyplot module from matplotlib (third-party library).
# Used for plotting charts (line, bar, scatter, histogram, etc.).
# Provides tools to customize plots: titles, labels, legends, colors, grid, figure size.


# -----------------------------
# 2) Class Definition
# -----------------------------

class CSV:  # 'class' is a keyword to define a class. PascalCase is used by convention.
            # This class acts as a "manager" for one CSV file storing all transactions.

    # -------------------------
    # 2a) Class Variables
    # -------------------------

    CSV_FILE = "finance_data.csv"  # Class variable: filename storing transactions.

    COLUMNS = ["date", "amount", "category", "description"]
    # Class variable: defines the CSV column order.

    FORMAT = date_format = "%d-%m-%Y"  
    # Date format string used throughout the program. "%d-%m-%Y" = Day-Month-Year.
    # Two names defined for convenience: FORMAT and date_format.


    # -------------------------
    # 2b) Class Methods
    # -------------------------

    @classmethod  # Decorator: method gets 'cls' (class) instead of 'self' (instance) as first param.
    def initialize_csv(cls):
        """Ensure CSV file exists; create it if missing."""
        try:  # Attempt to execute code that might fail.
            pd.read_csv(cls.CSV_FILE)  # Try reading CSV into DataFrame.
                                       # If file exists, do nothing else.
        except FileNotFoundError:  # Triggered if file does not exist.
            df = pd.DataFrame(columns=cls.COLUMNS)  # Create empty DataFrame with headers.
            df.to_csv(cls.CSV_FILE, index=False)    # Save empty CSV. index=False avoids writing row numbers.


    @classmethod
    def add_entry(cls, date, amount, category, description):
        """
        Append one transaction to CSV.
        Parameters:
          - date: str (format "dd-mm-yyyy")
          - amount: float/int
          - category: str ("Income" or "Expense")
          - description: str (notes)
        """
        new_entry = {  # Dictionary mapping column names → values.
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }

        # 'with' ensures file closes automatically after writing.
        with open(cls.CSV_FILE, "a", newline="") as csvfile:  # Open CSV in append mode ("a").
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)  
            # DictWriter maps dictionaries to CSV rows using fieldnames.
            writer.writerow(new_entry)  # Write one row.

        print("Entry added successfully.")  # Feedback to user.


    @classmethod
    def get_transactions(cls, start_date, end_date):
        """Return all transactions between start_date and end_date."""
        df = pd.read_csv(cls.CSV_FILE)  # Read CSV into DataFrame.

        # Convert "date" column strings → datetime objects for comparison.
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)

        # Convert user input (strings) → datetime objects for comparison.
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        # Boolean mask: True if row date in the range, False otherwise.
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)

        filtered_df = df.loc[mask]  # Apply mask to get filtered rows.

        if filtered_df.empty:  # Check if filtered DataFrame has no rows.
            print('No transactions found in the given date range.')
        else:
            # Display filtered transactions.
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(
                index=False,
                formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
            ))

            # Calculate totals
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary: ")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")

        return filtered_df  # Return DataFrame for optional further use.


# -----------------------------
# 3) Helper Functions
# -----------------------------

def add():  
    """Add a new transaction by prompting user for details."""
    CSV.initialize_csv()  # Ensure CSV exists.

    # Prompt user for date; allow default to today's date.
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ",
                    allow_default=True)
    amount = get_amount()        # Prompt user for amount.
    category = get_category()    # Prompt user for category.
    description = get_description()  # Prompt user for description.

    CSV.add_entry(date, amount, category, description)  # Append transaction to CSV.


def plot_transactions(df):
    """
    Plot Income and Expense over time.
    df: pandas DataFrame returned from get_transactions()
    """
    df.set_index("date", inplace=True)  # Use "date" column as x-axis.

    # Filter income transactions and resample daily. Fill missing days with 0.
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)
    # Filter expense transactions and resample daily.
    expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)

    # Create figure and axis for plotting.
    plt.figure(figsize=(10, 5))  # Width=10, Height=5 inches.
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")  # Green line for Income.
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")  # Red line for Expense.
    plt.xlabel("Date")  # X-axis label.
    plt.ylabel("Amount")  # Y-axis label.
    plt.title("Income and Expenses Over Time")  # Plot title.
    plt.legend()  # Show legend for line colors.
    plt.grid(True)  # Display gridlines.
    plt.show()  # Display the plot.


# -----------------------------
# 4) Main Menu / Loop
# -----------------------------

def main():  
    """Main program loop: add/view transactions or exit."""
    while True:  # Infinite loop; menu repeats until user exits.
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")  # Get input from user as string.

        if choice == "1":  # Add transaction
            add()
        elif choice == "2":  # View transactions
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (Y/N)? ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":  # Exit program
            print("Exiting...")
            break  # Exit the while loop.
        else:  # Invalid input
            print("Invalid choice. Enter 1, 2 or 3.")


# -----------------------------
# 5) Script Entry Point
# -----------------------------

if __name__ == "__main__":  # Special variable __name__ equals "__main__" if file is executed directly.
    main()                  # Calls main() only if this file is run directly, not imported.
