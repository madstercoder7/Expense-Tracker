from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('expense-tracker-db.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    transactions = conn.execute('SELECT * FROM transactions').fetchall()

    total_income = conn.execute('SELECT SUM(amount) FROM transactions WHERE amount > 0').fetchone()[0] or 0
    total_expenses = conn.execute('SELDCT SUM(amount) FORM transactions WHERE amount < 0').fetchone()[0] or 0
    conn.close()

    return render_template('index.html', transactions=transactions, total_income=total_income, total_expenses=total_expenses)