import requests
import os

# Hardcoded credentials
username = "admin"
password = "mysecretpassword"

# API keys
google_api_key = "AIzaSyBd7jHi412dasdfaBMRighDfrt351231412341234LaU"
aws_access_key_id = "AKIAIOSFODNN7EXAMPLE"
aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Database credentials
db_username = "myuser"
db_password = "mypassword"
db_host = "localhost"
db_name = "mydb"

# Slack webhook URL
slack_webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def send_slack_notification(message):
    requests.post(slack_webhook_url, json={"text": message})

def connect_to_db():
    # Using string formatting for SQL queries (SQL injection vulnerability)
    query = "SELECT * FROM users WHERE username = '%s'" % username
    # Database connection code...

if __name__ == "__main__":
    send_slack_notification("Hello from Python!")
    connect_to_db()
