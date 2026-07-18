# app.py
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from database import init_db, register_user, login_user, add_transaction, get_report, get_transactions
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'

# Initialize database
init_db()

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not username or not password:
            return render_template('register.html', error='All fields required')
        
        if password != confirm_password:
            return render_template('register.html', error='Passwords do not match')
        
        success, msg = register_user(username, password)
        
        if success:
            return redirect(url_for('login'))
        else:
            return render_template('register.html', error=msg)
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        success, user = login_user(username, password)
        
        if success:
            session['username'] = user
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    report = get_report(username)
    transactions = get_transactions(username)
    
    return render_template('dashboard.html', 
                         username=username,
                         report=report,
                         transactions=transactions)

@app.route('/add-transaction', methods=['POST'])
def add_trans():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    data = request.json
    username = session['username']
    t_type = data.get('type', '').strip().lower()
    amount = data.get('amount', '')
    category = data.get('category', '').strip()
    
    # Validation
    if t_type not in ['income', 'expense']:
        return jsonify({'success': False, 'message': 'Type must be income or expense'})
    
    try:
        amount = float(amount)
        if amount <= 0:
            return jsonify({'success': False, 'message': 'Amount must be greater than 0'})
    except ValueError:
        return jsonify({'success': False, 'message': 'Invalid amount'})
    
    if not category:
        return jsonify({'success': False, 'message': 'Category is required'})
    
    add_transaction(username, t_type, amount, category, str(datetime.now().date()))
    
    return jsonify({'success': True, 'message': 'Transaction added successfully'})

@app.route('/get-report')
def get_rep():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    username = session['username']
    report = get_report(username)
    
    return jsonify({
        'success': True,
        'income': report['income'],
        'expense': report['expense'],
        'balance': report['balance']
    })

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
