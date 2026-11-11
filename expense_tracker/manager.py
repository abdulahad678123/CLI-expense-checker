from .exceptions import ExpenseNotFoundError, InvalidExpenseError
from .storage import load_expenses, save_expenses


def add_expense(title, amount, category):
    if not title.strip():
        raise InvalidExpenseError("Title cannot be empty.")

    if not category.strip():
        raise InvalidExpenseError("Category cannot be empty.")

    if amount <= 0:
        raise InvalidExpenseError("Amount must be greater than zero.")

    expenses = load_expenses()

    # Generate a new ID
    new_id = max((expense["id"] for expense in expenses), default=0) + 1

    expense = {
        "id": new_id,
        "title": title.strip(),
        "amount": amount,
        "category": category.strip(),
    }

    expenses.append(expense)

    save_expenses(expenses)

    return expense


def list_expenses():
    return load_expenses()


def delete_expense(expense_id):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            return expense

    raise ExpenseNotFoundError(f"Expense with ID {expense_id} was not found.")


def summarize_expenses():
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    return total, category_totals
