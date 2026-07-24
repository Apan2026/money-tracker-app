# main.py


from tkinter import messagebox

from database import create_tables
from login import register, login
from tracker import save_transaction
from reports import get_report, get_transactions
from excel_export import export_excel


# ---------------- Dashboard ----------------

def open_dashboard(username):

    login_window.destroy()

    app = tk.Tk()
    app.title("Money Track App")
    app.geometry("500x600")


    tk.Label(
        app,
        text="Money Track App",
        font=("Arial", 20, "bold")
    ).pack(pady=10)


    tk.Label(
        app,
        text=f"User: {username}"
    ).pack()


    tk.Label(
        app,
        text="Type (income/expense)"
    ).pack()

    type_entry = tk.Entry(app)
    type_entry.pack()


    tk.Label(
        app,
        text="Amount"
    ).pack()

    amount_entry = tk.Entry(app)
    amount_entry.pack()


    tk.Label(
        app,
        text="Category"
    ).pack()

    category_entry = tk.Entry(app)
    category_entry.pack()



    def add_money():

        success, msg = save_transaction(
            username,
            type_entry.get(),
            amount_entry.get(),
            category_entry.get()
        )

        if success:
            messagebox.showinfo(
                "Success",
                msg
            )

            type_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)

        else:
            messagebox.showerror(
                "Error",
                msg
            )



    def view_report():

        data = get_report(username)

        messagebox.showinfo(
            "Report",
            f"""
Income : {data['income']}

Expense : {data['expense']}

Balance : {data['balance']}
"""
        )



    def history():

        data = get_transactions(username)

        if not data:
            messagebox.showinfo(
                "History",
                "No data found"
            )
            return


        text = ""

        for row in data:
            text += (
                f"{row[0]} | "
                f"{row[1]} | "
                f"{row[2]} | "
                f"{row[3]}\n"
            )


        messagebox.showinfo(
            "History",
            text
        )



    def export_file():

        try:

            file = export_excel(username)

            messagebox.showinfo(
                "Excel",
                f"File created: {file}"
            )

        except Exception as e:

            messagebox.showerror(
                "Excel Error",
                str(e)
            )



    tk.Button(
        app,
        text="Add Transaction",
        command=add_money,
        width=20
    ).pack(pady=10)


    tk.Button(
        app,
        text="View Report",
        command=view_report,
        width=20
    ).pack(pady=10)


    tk.Button(
        app,
        text="History",
        command=history,
        width=20
    ).pack(pady=10)


    tk.Button(
        app,
        text="Export Excel",
        command=export_file,
        width=20
    ).pack(pady=10)


    app.mainloop()



# ---------------- Login Functions ----------------

def login_button():

    username = username_entry.get()
    password = password_entry.get()


    success, user = login(
        username,
        password
    )


    if success:

        open_dashboard(user)

    else:

        messagebox.showerror(
            "Login Failed",
            "Wrong username or password"
        )



def register_button():

    success, msg = register(
        username_entry.get(),
        password_entry.get()
    )


    if success:

        messagebox.showinfo(
            "Register",
            msg
        )

    else:

        messagebox.showerror(
            "Register Error",
            msg
        )



# ---------------- Start ----------------

create_tables()


login_window = tk.Tk()

login_window.title(
    "Money Track Login"
)

login_window.geometry(
    "350x300"
)


tk.Label(
    login_window,
    text="Money Track App",
    font=("Arial",18,"bold")
).pack(pady=15)



tk.Label(
    login_window,
    text="Username"
).pack()


username_entry = tk.Entry(login_window)
username_entry.pack()



tk.Label(
    login_window,
    text="Password"
).pack()


password_entry = tk.Entry(
    login_window,
    show="*"
)

password_entry.pack()



tk.Button(
    login_window,
    text="Login",
    command=login_button,
    width=15
).pack(pady=10)



tk.Button(
    login_window,
    text="Register",
    command=register_button,
    width=15
).pack()



login_window.mainloop()
