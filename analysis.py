import pandas as pd

from file_handler import load_transactions


def get_dataframe():

    rows = load_transactions()

    columns = [
        "id",
        "date",
        "type",
        "category",
        "description",
        "amount"
    ]

    df = pd.DataFrame(
        rows,
        columns=columns
    )

    if df.empty:
        return df

    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    ).fillna(0)

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    return df


def totals():

    df = get_dataframe()

    if df.empty:
        return 0.0, 0.0, 0.0

    income = df.loc[
        df["type"] == "Income",
        "amount"
    ].sum()

    expense = df.loc[
        df["type"] == "Expense",
        "amount"
    ].sum()

    balance = income - expense

    return (
        float(income),
        float(expense),
        float(balance)
    )


def category_totals():

    df = get_dataframe()

    if df.empty:

        return pd.Series(
            dtype=float
        )

    expenses = df[
        df["type"] == "Expense"
    ]

    result = expenses.groupby(
        "category"
    )["amount"].sum()

    return result.sort_values(
        ascending=False
    )


def monthly_summary():

    df = get_dataframe()

    if df.empty:

        return pd.DataFrame(
            columns=[
                "Month",
                "Income",
                "Expense"
            ]
        )

    df = df.dropna(
        subset=["date"]
    )

    df["Month"] = (
        df["date"]
        .dt
        .to_period("M")
        .astype(str)
    )

    summary = df.pivot_table(
        index="Month",
        columns="type",
        values="amount",
        aggfunc="sum",
        fill_value=0
    )

    if "Income" not in summary.columns:

        summary["Income"] = 0

    if "Expense" not in summary.columns:

        summary["Expense"] = 0

    summary = summary.reset_index()

    return summary[
        [
            "Month",
            "Income",
            "Expense"
        ]
    ]


def major_spending_category():

    category = category_totals()

    if category.empty:

        return "No expenses"

    return str(
        category.idxmax()
    )


def filter_transactions(
        search_text="",
        transaction_type="All",
        category="All"):

    df = get_dataframe()

    if df.empty:
        return df

    result = df.copy()

    # Filter by transaction type
    if transaction_type != "All":

        result = result[
            result["type"] == transaction_type
        ]

    # Filter by category
    if category != "All":

        result = result[
            result["category"] == category
        ]

    # Search
    search_text = (
        search_text
        .strip()
        .lower()
    )

    if search_text:

        description_match = (
            result["description"]
            .astype(str)
            .str
            .lower()
            .str
            .contains(
                search_text,
                na=False
            )
        )

        category_match = (
            result["category"]
            .astype(str)
            .str
            .lower()
            .str
            .contains(
                search_text,
                na=False
            )
        )

        date_match = (
            result["date"]
            .astype(str)
            .str
            .contains(
                search_text,
                na=False
            )
        )

        result = result[
            description_match
            | category_match
            | date_match
        ]

    return result