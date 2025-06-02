import os
import sqlite3

# Rule: User input should not be used in SQL queries without proper sanitization
def vulnerable_sql_query(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Rule: Hardcoded credentials should not be used
def hardcoded_credentials():
    username = "admin"
    password = "mysecretpassword"
    # Use the hardcoded credentials for authentication
    if username == "admin" and password == "mysecretpassword":
        return True
    else:
        return False

# Rule: Path traversal vulnerability
def serve_file(path):
    with open(path, 'r') as file:
        content = file.read()
        return content

# Rule: Command injection vulnerability
def execute_command(input):
    command = f"echo {input}"
    os.system(command)

# Rule: Insecure deserialization
import pickle
def deserialize(data):
    return pickle.loads(data)

if __name__ == "__main__":
    username = input("Enter your username: ")
    vulnerable_sql_query(username)
    hardcoded_credentials()
    serve_file("/files/" + input("Enter the file path: "))
    execute_command(input("Enter the input: "))
    deserialize(input("Enter the data: ").encode())
#
