import os
import subprocess
import pickle

# ❌ Hardcoded secret (ERROR)
API_KEY = "sk_live_1234567890abcdef"

# ❌ Use of insecure function: eval (ERROR)
def insecure_eval(user_input):
    return eval(user_input)

# ❌ Use of subprocess with shell=True (ERROR)
def run_command(cmd):
    subprocess.call(cmd, shell=True)

# ❌ Deserialization with pickle (ERROR)
def load_data(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

# ❌ Insecure randomness (ERROR)
from random import random
def generate_token():
    return str(random())

# ❌ Potential command injection
def list_dir(user_input):
    os.system("ls " + user_input)

# Test calls (optional)
if __name__ == "__main__":
    print(insecure_eval("1 + 2"))
    run_command("echo Hello")
    print(generate_token())
    list_dir("; rm -rf /")  # Dangerous!
