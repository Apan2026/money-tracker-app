# reports.py

from database import connect


def get_report(username):

    conn = connect()
    cursor = conn.cursor()


    # Total Income
    cursor.execute(
        """
        SELECT SUM(amount)
        FROM transactions
        WHERE username=? AND type='income'
        """,
        (username,)
    )

    income = cursor.fetchone()[0]

    if income is None:
        income = 0


    # Total Expense
    cursor.execute(
        """
        SELECT SUM(amount)
        FROM transactions
        WHERE username=? AND type='expense'
        """,
        (username,)
    )

    expense = cursor.fetchone()[0]

    if expense is None:
        expense = 0


    balance = income - expense


    conn.close()


    return {
        "income": income,
        "expense": expense,
        "balance": balance
    }



def get_transactions(username):

    conn = connect()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT type, amount, category, date
        FROM transactions
        WHERE username=?
        ORDER BY id DESC
        """,
        (username,)
    )


    data = cursor.fetchall()

    conn.close()

    return data