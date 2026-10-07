import matplotlib.pyplot as plt

from analysis import (
    category_totals,
    monthly_summary
)


def show_category_chart(parent=None):

    data = category_totals()

    if data.empty:

        raise ValueError(
            "No expense data available "
            "for the category chart."
        )

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    data.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Pocket Money - Expense by Category"
    )

    ax.set_xlabel(
        "Category"
    )

    ax.set_ylabel(
        "Expense Amount (₹)"
    )

    ax.tick_params(
        axis="x",
        rotation=30
    )

    fig.tight_layout()

    plt.show()


def show_period_chart(parent=None):

    data = monthly_summary()

    if data.empty:

        raise ValueError(
            "No transaction data available "
            "for the period chart."
        )

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    ax.plot(
        data["Month"],
        data["Income"],
        marker="o",
        label="Income"
    )

    ax.plot(
        data["Month"],
        data["Expense"],
        marker="o",
        label="Expense"
    )

    ax.set_title(
        "Pocket Money - Monthly Income vs Expense"
    )

    ax.set_xlabel(
        "Month"
    )

    ax.set_ylabel(
        "Amount (₹)"
    )

    ax.legend()

    ax.grid(
        True,
        alpha=0.3
    )

    plt.xticks(
        rotation=30
    )

    fig.tight_layout()

    plt.show()