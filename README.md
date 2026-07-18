# Money Tracker App 💰

A Python-based Desktop Application for tracking personal finances with features like income/expense management, reporting, and Excel export.

## Features ✨

- **User Authentication**: Register and login functionality
- **Transaction Management**: Add income and expense transactions
- **Categories**: Organize transactions by categories
- **Financial Reports**: View total income, expenses, and balance
- **Transaction History**: View all past transactions
- **Excel Export**: Export financial reports to Excel format
- **SQLite Database**: Secure local data storage

## Project Structure 📁

```
money-tracker-app/
├── main.py              # Main application with GUI
├── database.py          # Database operations
├── login.py             # User authentication
├── tracker.py           # Transaction handling
├── reports.py           # Financial reports
├── excel_export.py      # Excel export functionality
└── README.md            # Project documentation
```

## Requirements 📋

- Python 3.7+
- tkinter (usually included with Python)
- pandas
- openpyxl
- sqlite3 (built-in)

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/Apan2026/money-tracker-app.git
cd money-tracker-app
```

2. Install dependencies:
```bash
pip install pandas openpyxl
```

3. Run the application:
```bash
python main.py
```

## Usage 💡

1. **Register**: Create a new account with username and password
2. **Login**: Enter your credentials to access the dashboard
3. **Add Transaction**: 
   - Enter type (income/expense)
   - Enter amount
   - Enter category
   - Click "Add Transaction"
4. **View Report**: See your total income, expenses, and balance
5. **View History**: Check all your past transactions
6. **Export to Excel**: Download your financial report as Excel file

## Database Schema 🗄️

### Users Table
- `id`: Primary Key
- `username`: Unique username
- `password`: User password

### Transactions Table
- `id`: Primary Key
- `username`: Associated user
- `type`: income or expense
- `amount`: Transaction amount
- `category`: Transaction category
- `date`: Transaction date

## License 📄

This project is open source and available under the MIT License.

## Author 👨‍💻

Created by Apan2026
