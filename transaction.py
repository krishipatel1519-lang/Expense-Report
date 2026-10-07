from datetime import datetime


CATEGORIES = [
    "Food",
    "Travel",
    "Education",
    "Shopping",
    "Entertainment",
    "Bills",
    "Health",
    "Other"
]

TRANSACTION_TYPES = [
    "Income",
    "Expense"
]


def validate_transaction(date_text, transaction_type,
                         category, description, amount):

    # Validate date
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        raise ValueError(
            "Date must be in YYYY-MM-DD format."
        )

    # Validate transaction type
    if transaction_type not in TRANSACTION_TYPES:
        raise ValueError(
            "Please select a valid transaction type."
        )

    # Validate category
    if category not in CATEGORIES:
        raise ValueError(
            "Please select a valid category."
        )

    # Validate description
    if not description.strip():
        raise ValueError(
            "Description cannot be empty."
        )

    # Validate amount
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        raise ValueError(
            "Amount must be a valid number."
        )

    if amount <= 0:
        raise ValueError(
            "Amount must be greater than zero."
        )

    return round(amount, 2)


def create_transaction(transaction_id,
                       date_text,
                       transaction_type,
                       category,
                       description,
                       amount):

    amount = validate_transaction(
        date_text,
        transaction_type,
        category,
        description,
        amount
    )

    transaction = {
        "id": str(transaction_id),
        "date": date_text,
        "type": transaction_type,
        "category": category,
        "description": description.strip(),
        "amount": f"{amount:.2f}"
    }

    return transaction


def next_id(transactions):

    if not transactions:
        return 1

    ids = []

    for row in transactions:
        try:
            ids.append(int(row["id"]))
        except (KeyError, ValueError):
            continue

    return max(ids, default=0) + 1