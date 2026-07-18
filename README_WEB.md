# Money Tracker - Web Version 🌐

A Flask-based web application for tracking personal finances with a modern, responsive interface.

## Features ✨

- **User Authentication**: Secure registration and login system
- **Transaction Management**: Add income and expense transactions
- **Real-time Dashboard**: View income, expenses, and balance at a glance
- **Transaction History**: See all your transactions with details
- **Responsive Design**: Works on desktop and mobile devices
- **SQLite Database**: Local data storage

## Technology Stack 🛠️

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite3
- **Server**: Gunicorn (for production)

## Installation 🚀

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/Apan2026/money-tracker-app.git
cd money-tracker-app
```

2. Checkout web-version branch:
```bash
git checkout web-version
```

3. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and visit:
```
http://localhost:5000
```

## Usage 📖

### Register
1. Click on "Register here" link
2. Enter a username and password
3. Confirm your password
4. Click "Register" button

### Login
1. Enter your username and password
2. Click "Login" button

### Add Transaction
1. Go to dashboard
2. Fill in the transaction details:
   - Type: Income or Expense
   - Amount: Enter the amount
   - Category: e.g., Salary, Food, Entertainment
3. Click "Add Transaction"

### View Report
- Dashboard shows your Income, Expense, and Balance in real-time
- All amounts are updated instantly

### View History
- Scroll down to see all your transactions
- Latest transactions appear first

## File Structure 📁

```
web-version/
├── app.py                 # Flask application
├── database.py            # Database operations
├── requirements.txt       # Python dependencies
├── templates/
│   ├── base.html         # Base template
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   └── dashboard.html    # Dashboard page
└── static/
    └── style.css         # CSS styles
```

## API Endpoints 🔌

- `GET /` - Redirect to login or dashboard
- `GET /login` - Login page
- `POST /login` - Handle login request
- `GET /register` - Register page
- `POST /register` - Handle registration
- `GET /dashboard` - User dashboard
- `POST /add-transaction` - Add new transaction (JSON)
- `GET /get-report` - Get financial report (JSON)
- `GET /logout` - Logout user

## Deployment 🌍

### Using Heroku

1. Create a Procfile:
```
web: gunicorn app:app
```

2. Install Heroku CLI and deploy:
```bash
heroku login
heroku create your-app-name
git push heroku web-version:main
```

### Using PythonAnywhere

1. Sign up at PythonAnywhere.com
2. Upload your project
3. Configure a web app with Flask
4. Reload the web app

## Security Notes ⚠️

- Change the `secret_key` in `app.py` before deploying to production
- Use HTTPS in production
- Hash passwords properly (consider using werkzeug.security)
- Add CSRF protection for production

## Troubleshooting 🔧

### Port already in use
```bash
python app.py --port 5001
```

### Database issues
Delete `money_tracker.db` and restart the application

## License 📄

MIT License - Feel free to use this project!

## Author 👨‍💻

Created by Apan2026
