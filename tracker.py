# tracker.py

from datetime import date
from database import add_transaction


def save_transaction(username, t_type, amount, category):

    # Debug
    print("Username:", repr(username))
    print("Type:", repr(t_type))
    print("Amount:", repr(amount))
    print("Category:", repr(category))

    # Clean input
    t_type = t_type.strip().lower()
    category = category.strip()

    # Validate type
    if t_type not in ["income", "expense"]:
        return False, "Type must be income or expense"

    # Validate amount
    try:
        amount = float(amount)

        if amount <= 0:
            return False, "Amount must be greater than 0"

    except ValueError:
        return False, "Invalid amount"

    # Save to database
    add_transaction(
        username,
        t_type,
        amount,
        category,
        str(date.today())
    )

    return True, "Transaction added successfully"