POCKET MONEY MANAGEMENT AND SPENDING ANALYSIS SYSTEM
=====================================================

1. INTRODUCTION
---------------

The Pocket Money Management and Spending Analysis System is a
Python-based application developed to help students record and
analyze their pocket-money transactions.

The system records income and expenses and calculates the remaining
balance. It also provides category-wise and monthly spending analysis.

2. OBJECTIVE
------------

The main objectives of the project are:

1. Record pocket-money income.
2. Record daily expenses.
3. Calculate total income.
4. Calculate total expenses.
5. Calculate remaining balance.
6. Identify the major spending category.
7. Search and filter transactions.
8. Update existing transactions.
9. Delete transactions.
10. Generate visual reports.

3. TECHNOLOGIES USED
--------------------

Programming Language:
Python

GUI:
Tkinter

Data Analysis:
Pandas

Visualization:
Matplotlib

Data Storage:
CSV

IDE:
Visual Studio Code

4. MODULES
----------

main.py
Starts the application.

gui.py
Contains the Tkinter graphical user interface.

transaction.py
Handles transaction creation and validation.

file_handler.py
Handles CSV file operations.

analysis.py
Performs data analysis using Pandas.

reports.py
Creates Matplotlib visualizations.

5. FEATURES
-----------

- Add Income
- Add Expense
- View Transactions
- Search Transactions
- Filter Transactions
- Update Transactions
- Delete Transactions
- Calculate Balance
- Category Analysis
- Monthly Analysis
- Expense Chart
- Income vs Expense Chart
- Input Validation
- Exception Handling
- Persistent CSV Storage

6. INSTALLATION
---------------

Open the VS Code terminal and execute:

pip install pandas matplotlib numpy

7. RUNNING THE PROJECT
----------------------

Execute:

python main.py

8. VISUAL REPORTS
-----------------

The system provides two meaningful visual reports:

1. Expense by Category

This chart shows the amount spent in each expense category.

2. Monthly Income vs Expense

This chart compares income and expenses across different months.

9. VALIDATION
-------------

The application validates:

- Date format
- Transaction type
- Category
- Description
- Amount

The amount must be greater than zero.

10. EXCEPTION HANDLING
----------------------

The project uses try-except blocks to handle:

- Invalid input
- Invalid dates
- Invalid amounts
- CSV file errors
- Missing transactions
- Chart errors

11. TESTING
-----------

Test Case 1:
Add an income of Rs.5000.

Expected Result:
Total income increases by Rs.5000.

Test Case 2:
Add an expense of Rs.200.

Expected Result:
Total expense increases by Rs.200.

Test Case 3:
Enter negative amount.

Expected Result:
Error message is displayed.

Test Case 4:
Enter incorrect date.

Expected Result:
Date validation error is displayed.

Test Case 5:
Select a transaction and update it.

Expected Result:
Transaction is updated.

Test Case 6:
Select a transaction and delete it.

Expected Result:
Transaction is removed.

Test Case 7:
Click Expense by Category.

Expected Result:
Matplotlib category chart appears.

Test Case 8:
Click Monthly Comparison.

Expected Result:
Income and expense comparison chart appears.

12. CONCLUSION
--------------

The Pocket Money Management and Spending Analysis System provides
a simple and effective way for students to manage their pocket money.

The project demonstrates Python programming, functions, modules,
file handling, Pandas data analysis, Tkinter GUI development,
Matplotlib visualization, input validation and exception handling.