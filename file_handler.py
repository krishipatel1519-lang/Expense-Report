import csv
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent / "transactions.csv"

FIELDS = [
    "id",
    "date",
    "type",
    "category",
    "description",
    "amount"
]


def ensure_file():

    if not DATA_FILE.exists():

        with open(
            DATA_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=FIELDS
            )

            writer.writeheader()


def load_transactions():

    ensure_file()

    try:

        with open(
            DATA_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            return list(
                csv.DictReader(file)
            )

    except (OSError, csv.Error) as error:

        raise RuntimeError(
            f"Unable to read transaction file: {error}"
        )


def save_transactions(transactions):

    try:

        with open(
            DATA_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=FIELDS
            )

            writer.writeheader()
            writer.writerows(transactions)

    except OSError as error:

        raise RuntimeError(
            f"Unable to save transactions: {error}"
        )


def add_transaction(transaction):

    transactions = load_transactions()

    transactions.append(transaction)

    save_transactions(transactions)


def update_transaction(transaction_id, updated):

    transactions = load_transactions()

    found = False

    for row in transactions:

        if row["id"] == str(transaction_id):

            row.update(updated)

            found = True
            break

    if not found:

        raise ValueError(
            "Transaction not found."
        )

    save_transactions(transactions)


def delete_transaction(transaction_id):

    transactions = load_transactions()

    new_transactions = []

    for row in transactions:

        if row["id"] != str(transaction_id):

            new_transactions.append(row)

    if len(new_transactions) == len(transactions):

        raise ValueError(
            "Transaction not found."
        )

    save_transactions(new_transactions)