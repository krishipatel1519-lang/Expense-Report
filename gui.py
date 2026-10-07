import tkinter as tk

from tkinter import ttk, messagebox

from datetime import date

from file_handler import (
    load_transactions,
    add_transaction,
    update_transaction,
    delete_transaction
)

from transaction import (
    CATEGORIES,
    TRANSACTION_TYPES,
    create_transaction,
    next_id
)

from analysis import (
    totals,
    major_spending_category,
    filter_transactions
)

from reports import (
    show_category_chart,
    show_period_chart
)


class PocketMoneyApp:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "Pocket Money Management System"
        )

        self.root.geometry(
            "1100x700"
        )

        self.root.minsize(
            950,
            620
        )

        self.selected_id = None

        # Form variables
        self.date_var = tk.StringVar(
            value=date.today().strftime(
                "%Y-%m-%d"
            )
        )

        self.type_var = tk.StringVar(
            value="Expense"
        )

        self.category_var = tk.StringVar(
            value=CATEGORIES[0]
        )

        self.description_var = tk.StringVar()

        self.amount_var = tk.StringVar()

        # Search variables
        self.search_var = tk.StringVar()

        self.filter_type_var = tk.StringVar(
            value="All"
        )

        self.filter_category_var = tk.StringVar(
            value="All"
        )

        # Dashboard variables
        self.income_var = tk.StringVar(
            value="₹0.00"
        )

        self.expense_var = tk.StringVar(
            value="₹0.00"
        )

        self.balance_var = tk.StringVar(
            value="₹0.00"
        )

        self.major_var = tk.StringVar(
            value="No expenses"
        )

        self.build_style()

        self.build_ui()

        self.refresh()

    # --------------------------------
    # STYLE
    # --------------------------------

    def build_style(self):

        style = ttk.Style()

        try:
            style.theme_use(
                "clam"
            )
        except tk.TclError:
            pass

        style.configure(
            "Title.TLabel",
            font=("Arial", 22, "bold")
        )

        style.configure(
            "Card.TLabel",
            font=("Arial", 14, "bold")
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        style.configure(
            "Treeview",
            rowheight=28,
            font=("Arial", 10)
        )

    # --------------------------------
    # MAIN UI
    # --------------------------------

    def build_ui(self):

        title = ttk.Label(
            self.root,
            text=(
                "💰 Pocket Money Management "
                "& Spending Analysis"
            ),
            style="Title.TLabel"
        )

        title.pack(
            pady=(15, 8)
        )

        self.build_dashboard()

        self.build_form()

        self.build_filter()

        self.build_table()

        self.build_buttons()

    # --------------------------------
    # DASHBOARD
    # --------------------------------

    def build_dashboard(self):

        frame = ttk.Frame(
            self.root
        )

        frame.pack(
            fill="x",
            padx=15,
            pady=5
        )

        cards = [
            (
                "Total Income",
                self.income_var
            ),
            (
                "Total Expenses",
                self.expense_var
            ),
            (
                "Remaining Balance",
                self.balance_var
            ),
            (
                "Major Spending",
                self.major_var
            )
        ]

        for title, variable in cards:

            box = ttk.LabelFrame(
                frame,
                text=title
            )

            box.pack(
                side="left",
                fill="both",
                expand=True,
                padx=5
            )

            ttk.Label(
                box,
                textvariable=variable,
                style="Card.TLabel"
            ).pack(
                padx=10,
                pady=15
            )

    # --------------------------------
    # TRANSACTION FORM
    # --------------------------------

    def build_form(self):

        frame = ttk.LabelFrame(
            self.root,
            text="Transaction Details"
        )

        frame.pack(
            fill="x",
            padx=15,
            pady=8
        )

        # Date
        ttk.Label(
            frame,
            text="Date (YYYY-MM-DD)"
        ).grid(
            row=0,
            column=0,
            padx=6,
            pady=6
        )

        ttk.Entry(
            frame,
            textvariable=self.date_var,
            width=15
        ).grid(
            row=1,
            column=0,
            padx=6,
            pady=3
        )

        # Type
        ttk.Label(
            frame,
            text="Type"
        ).grid(
            row=0,
            column=1,
            padx=6,
            pady=6
        )

        ttk.Combobox(
            frame,
            textvariable=self.type_var,
            values=TRANSACTION_TYPES,
            state="readonly",
            width=14
        ).grid(
            row=1,
            column=1,
            padx=6,
            pady=3
        )

        # Category
        ttk.Label(
            frame,
            text="Category"
        ).grid(
            row=0,
            column=2,
            padx=6,
            pady=6
        )

        ttk.Combobox(
            frame,
            textvariable=self.category_var,
            values=CATEGORIES,
            state="readonly",
            width=16
        ).grid(
            row=1,
            column=2,
            padx=6,
            pady=3
        )

        # Description
        ttk.Label(
            frame,
            text="Description"
        ).grid(
            row=0,
            column=3,
            padx=6,
            pady=6
        )

        ttk.Entry(
            frame,
            textvariable=self.description_var,
            width=25
        ).grid(
            row=1,
            column=3,
            padx=6,
            pady=3
        )

        # Amount
        ttk.Label(
            frame,
            text="Amount (₹)"
        ).grid(
            row=0,
            column=4,
            padx=6,
            pady=6
        )

        ttk.Entry(
            frame,
            textvariable=self.amount_var,
            width=15
        ).grid(
            row=1,
            column=4,
            padx=6,
            pady=3
        )

        # Add button
        ttk.Button(
            frame,
            text="Add Transaction",
            command=self.add
        ).grid(
            row=1,
            column=5,
            padx=8
        )

        # Clear
        ttk.Button(
            frame,
            text="Clear",
            command=self.clear_form
        ).grid(
            row=1,
            column=6,
            padx=8
        )

    # --------------------------------
    # SEARCH / FILTER
    # --------------------------------

    def build_filter(self):

        frame = ttk.LabelFrame(
            self.root,
            text="Search / Filter"
        )

        frame.pack(
            fill="x",
            padx=15,
            pady=5
        )

        ttk.Label(
            frame,
            text="Search"
        ).pack(
            side="left",
            padx=5
        )

        ttk.Entry(
            frame,
            textvariable=self.search_var,
            width=25
        ).pack(
            side="left",
            padx=5
        )

        ttk.Label(
            frame,
            text="Type"
        ).pack(
            side="left",
            padx=5
        )

        ttk.Combobox(
            frame,
            textvariable=self.filter_type_var,
            values=[
                "All"
            ] + TRANSACTION_TYPES,
            state="readonly",
            width=12
        ).pack(
            side="left",
            padx=5
        )

        ttk.Label(
            frame,
            text="Category"
        ).pack(
            side="left",
            padx=5
        )

        ttk.Combobox(
            frame,
            textvariable=self.filter_category_var,
            values=[
                "All"
            ] + CATEGORIES,
            state="readonly",
            width=15
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame,
            text="Apply Filter",
            command=self.refresh
        ).pack(
            side="left",
            padx=8
        )

        ttk.Button(
            frame,
            text="Show All",
            command=self.reset_filter
        ).pack(
            side="left",
            padx=5
        )

    # --------------------------------
    # TABLE
    # --------------------------------

    def build_table(self):

        frame = ttk.Frame(
            self.root
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        columns = (
            "id",
            "date",
            "type",
            "category",
            "description",
            "amount"
        )

        self.tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        headings = {
            "id": "ID",
            "date": "Date",
            "type": "Type",
            "category": "Category",
            "description": "Description",
            "amount": "Amount (₹)"
        }

        widths = {
            "id": 50,
            "date": 100,
            "type": 90,
            "category": 130,
            "description": 250,
            "amount": 110
        }

        for column in columns:

            self.tree.heading(
                column,
                text=headings[column]
            )

            self.tree.column(
                column,
                width=widths[column],
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_row
        )

    # --------------------------------
    # BOTTOM BUTTONS
    # --------------------------------

    def build_buttons(self):

        frame = ttk.Frame(
            self.root
        )

        frame.pack(
            fill="x",
            padx=15,
            pady=8
        )

        ttk.Button(
            frame,
            text="Update Selected",
            command=self.update
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame,
            text="Delete Selected",
            command=self.delete
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            frame,
            text="📊 Expense by Category",
            command=self.category_chart
        ).pack(
            side="right",
            padx=5
        )

        ttk.Button(
            frame,
            text="📈 Monthly Comparison",
            command=self.period_chart
        ).pack(
            side="right",
            padx=5
        )

    # --------------------------------
    # REFRESH
    # --------------------------------

    def refresh(self):

        try:

            self.refresh_table()

            self.refresh_dashboard()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # --------------------------------
    # REFRESH TABLE
    # --------------------------------

    def refresh_table(self):

        for item in self.tree.get_children():

            self.tree.delete(item)

        df = filter_transactions(
            self.search_var.get(),
            self.filter_type_var.get(),
            self.filter_category_var.get()
        )

        if df.empty:
            return

        for _, row in df.iterrows():

            if hasattr(
                row["date"],
                "strftime"
            ):

                formatted_date = (
                    row["date"]
                    .strftime("%Y-%m-%d")
                )

            else:

                formatted_date = row["date"]

            self.tree.insert(
                "",
                "end",
                values=(
                    row["id"],
                    formatted_date,
                    row["type"],
                    row["category"],
                    row["description"],
                    f"{float(row['amount']):.2f}"
                )
            )

    # --------------------------------
    # DASHBOARD REFRESH
    # --------------------------------

    def refresh_dashboard(self):

        income, expense, balance = totals()

        self.income_var.set(
            f"₹{income:,.2f}"
        )

        self.expense_var.set(
            f"₹{expense:,.2f}"
        )

        self.balance_var.set(
            f"₹{balance:,.2f}"
        )

        self.major_var.set(
            major_spending_category()
        )

    # --------------------------------
    # ADD
    # --------------------------------

    def add(self):

        try:

            rows = load_transactions()

            transaction = create_transaction(
                next_id(rows),
                self.date_var.get(),
                self.type_var.get(),
                self.category_var.get(),
                self.description_var.get(),
                self.amount_var.get()
            )

            add_transaction(
                transaction
            )

            self.clear_form()

            self.refresh()

            messagebox.showinfo(
                "Success",
                "Transaction added successfully."
            )

        except (
            ValueError,
            RuntimeError
        ) as error:

            messagebox.showerror(
                "Invalid Transaction",
                str(error)
            )

    # --------------------------------
    # SELECT
    # --------------------------------

    def select_row(self, event=None):

        selected = self.tree.selection()

        if not selected:
            return

        values = self.tree.item(
            selected[0],
            "values"
        )

        self.selected_id = values[0]

        self.date_var.set(
            values[1]
        )

        self.type_var.set(
            values[2]
        )

        self.category_var.set(
            values[3]
        )

        self.description_var.set(
            values[4]
        )

        self.amount_var.set(
            values[5]
        )

    # --------------------------------
    # UPDATE
    # --------------------------------

    def update(self):

        if not self.selected_id:

            messagebox.showwarning(
                "Select Transaction",
                "Please select a transaction first."
            )

            return

        try:

            transaction = create_transaction(
                self.selected_id,
                self.date_var.get(),
                self.type_var.get(),
                self.category_var.get(),
                self.description_var.get(),
                self.amount_var.get()
            )

            update_transaction(
                self.selected_id,
                transaction
            )

            self.clear_form()

            self.refresh()

            messagebox.showinfo(
                "Success",
                "Transaction updated successfully."
            )

        except (
            ValueError,
            RuntimeError
        ) as error:

            messagebox.showerror(
                "Update Error",
                str(error)
            )

    # --------------------------------
    # DELETE
    # --------------------------------

    def delete(self):

        if not self.selected_id:

            messagebox.showwarning(
                "Select Transaction",
                "Please select a transaction first."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete "
            "this transaction?"
        )

        if not answer:
            return

        try:

            delete_transaction(
                self.selected_id
            )

            self.clear_form()

            self.refresh()

            messagebox.showinfo(
                "Success",
                "Transaction deleted successfully."
            )

        except (
            ValueError,
            RuntimeError
        ) as error:

            messagebox.showerror(
                "Delete Error",
                str(error)
            )

    # --------------------------------
    # CLEAR FORM
    # --------------------------------

    def clear_form(self):

        self.selected_id = None

        self.date_var.set(
            date.today().strftime(
                "%Y-%m-%d"
            )
        )

        self.type_var.set(
            "Expense"
        )

        self.category_var.set(
            CATEGORIES[0]
        )

        self.description_var.set(
            ""
        )

        self.amount_var.set(
            ""
        )

        for item in self.tree.selection():

            self.tree.selection_remove(
                item
            )

    # --------------------------------
    # RESET FILTER
    # --------------------------------

    def reset_filter(self):

        self.search_var.set(
            ""
        )

        self.filter_type_var.set(
            "All"
        )

        self.filter_category_var.set(
            "All"
        )

        self.refresh()

    # --------------------------------
    # CATEGORY CHART
    # --------------------------------

    def category_chart(self):

        try:

            show_category_chart(
                self.root
            )

        except ValueError as error:

            messagebox.showwarning(
                "No Data",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Chart Error",
                str(error)
            )

    # --------------------------------
    # PERIOD CHART
    # --------------------------------

    def period_chart(self):

        try:

            show_period_chart(
                self.root
            )

        except ValueError as error:

            messagebox.showwarning(
                "No Data",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Chart Error",
                str(error)
            )

    # --------------------------------
    # RUN
    # --------------------------------

    def run(self):

        self.root.mainloop()