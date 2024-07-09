# Expense Tracker Application

This project is a graphical user interface (GUI) based Expense Tracker application built using `customtkinter`, `tkcalendar`, and `PIL` libraries for Python. The application allows users to add, view, and analyze their expenses, and stores the data in a MySQL database.

## Features

- **Add Expenses**: Users can input item names, quantities, unit costs, and dates to add expenses.
- **Clear Input Fields**: Users can clear input fields with a button click.
- **View Expenses**: The application displays added expenses in a structured format.
- **Analyze Expenses**: Users can analyze monthly expenses through graphical representations (pie chart and bar graph).

## Requirements

- Python 3.x
- `customtkinter` library
- `tkcalendar` library
- `PIL` (Pillow) library
- `pandas` library
- `mysql-connector-python` library
- `matplotlib` library
- MySQL database

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/expense-tracker.git
    cd expense-tracker
    ```

2. **Install the required Python libraries**:
    ```sh
    pip install customtkinter tkcalendar pillow pandas mysql-connector-python matplotlib
    ```

3. **Set up the MySQL database**:
    - Create a MySQL database named `expense_tracker`.
    - Create a table named `expenses` with the following structure:
        ```sql
        CREATE TABLE expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            item VARCHAR(255),
            quantity INT,
            cost INT,
            total INT,
            date DATE
        );
        ```

4. **Update the database configuration**:
    - Edit the database connection settings in the code to match your MySQL server configuration:
        ```python
        db = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="1234",
            database="expense_tracker"
        )
        ```

## Usage

1. **Run the application**:
    ```sh
    python expense_tracker.py
    ```

2. **Add an Expense**:
    - Enter the item name, quantity, unit cost, and date.
    - Click the "Add Item" button to add the expense to the list and database.

3. **Clear Input Fields**:
    - Click the "Clear" button to reset the input fields.

4. **View Expenses**:
    - The added expenses will be displayed in a structured format.

5. **Analyze Expenses**:
    - Click the "Analyze" button to view a pie chart and bar graph representing the total expenses for the current month by item.

## Code Overview

- **Import Libraries**:
    - Import necessary libraries including `customtkinter`, `tkcalendar`, `PIL`, `pandas`, `datetime`, `matplotlib`, and `mysql.connector`.

- **Database Connection**:
    - Connect to the MySQL database.

- **Initialize GUI**:
    - Set the appearance mode and initialize the main window.
    - Configure the main window layout.

- **Load Background Image**:
    - Load and resize the background image.

- **Global Variables**:
    - Initialize an empty list to store items.

- **Add Item Function**:
    - Add item details to the list and database.
    - Display the item details in the GUI.

- **Clear Item Function**:
    - Clear input fields.

- **Analyze Function**:
    - Fetch data from the database and current session.
    - Combine and analyze data.
    - Display analysis using pie chart and bar graph.

- **GUI Layout**:
    - Create and place frames, labels, entries, buttons, and date picker.
    - Configure layout and styles.

## Screenshots

![Expense Tracker](screenshots/expense_tracker.png)


---

For any issues or questions, please contact [22wh1a05h8@bvrithyderabad.edu.in].

