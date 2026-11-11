import argparse

from .exceptions import ExpenseNotFoundError, InvalidExpenseError
from .manager import (
    add_expense,
    delete_expense,
    list_expenses,
    summarize_expenses,
)


def main():
    parser = argparse.ArgumentParser(description="CLI Expense Tracker")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new expense")

    add_parser.add_argument("--title", required=True, help="Expense title")

    add_parser.add_argument(
        "--amount", type=float, required=True, help="Expense amount"
    )

    add_parser.add_argument("--category", required=True, help="Expense category")

    # List command
    subparsers.add_parser("list", help="List all expenses")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")

    delete_parser.add_argument("--id", type=int, required=True, help="Expense ID")

    # Summary command
    subparsers.add_parser("summary", help="Summarize all expenses")

    args = parser.parse_args()

    try:
        if args.command == "add":
            expense = add_expense(args.title, args.amount, args.category)

            print("Expense added successfully!")
            print(expense)

        elif args.command == "list":
            expenses = list_expenses()

            if not expenses:
                print("No expenses found.")

            else:
                print("\nAll Expenses:")
                print("-" * 45)

                for expense in expenses:
                    print(
                        f"ID: {expense['id']} | "
                        f"Title: {expense['title']} | "
                        f"Amount: {expense['amount']:.2f} | "
                        f"Category: {expense['category']}"
                    )

        elif args.command == "delete":
            expense = delete_expense(args.id)

            print(f"Expense '{expense['title']}' deleted successfully!")

        elif args.command == "summary":
            total, categories = summarize_expenses()

            print("\nExpense Summary")
            print("-" * 30)
            print(f"Total Expenses: {total:.2f}")

            print("\nCategory-wise Expenses:")

            if not categories:
                print("No expenses found.")

            else:
                for category, amount in categories.items():
                    print(f"{category}: {amount:.2f}")

    except (ExpenseNotFoundError, InvalidExpenseError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
