# excel_export.py

import os
import pandas as pd
from database import connect


def export_excel(username):

    conn = connect()

    query = """
    SELECT
        username,
        type,
        amount,
        category,
        date
    FROM transactions
    WHERE username = ?
    ORDER BY id DESC
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(username,)
    )

    conn.close()

    if df.empty:
        return "No transaction data found"

    file_name = f"{username}_money_report.xlsx"

    file_path = os.path.abspath(file_name)

    df.to_excel(
        file_path,
        index=False,
        engine="openpyxl"
    )

    return file_path