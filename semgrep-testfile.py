import os
import subprocess
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# 1. Hardcoded secret (High severity)
API_KEY = "1234567890abcdef"

# 2. Insecure subprocess call (Command Injection)
@app.route('/ping')
def ping():
    host = request.args.get('host')
    return subprocess.check_output("ping -c 1 " + host, shell=True)

# 3. SQL Injection vulnerability
@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return str(result)

# 4. Use of eval() with user input
@app.route('/calc')
def calc():
    expr = request.args.get('expr')
    return str(eval(expr))  # Dangerous

# 5. Insecure deserialization using pickle
import pickle
@app.route('/load')
def load_data():
    data = request.args.get('data')
    return pickle.loads(bytes(data, 'utf-8'))  # Unsafe

# 6. Insecure random generator for security tokens
import random
@app.route('/token')
def get_token():
    return str(random.randint(100000, 999999))  # Not secure
