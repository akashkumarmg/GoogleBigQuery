import pickle
import os

# :rotating_light: Hardcoded secret
API_KEY = "sk_test_51H8zP5XkGzFakeSecretKeyForSemgrepTesting"

def execute_user_input():
    user_input = input("Enter code to execute: ")
    # :rotating_light: Dangerous use of eval
    result = eval(user_input)
    print(f"Result: {result}")

def insecure_deserialization():
    data = b"some malicious pickle string"
    # :rotating_light: Unsafe deserialization
    obj = pickle.loads(data)
    print("Deserialized:", obj)

def insecure_command_execution():
    filename = input("Enter filename: ")
    # :rotating_light: Unsafe os.system usage
    os.system("cat " + filename)

if __name__ == "__main__":
    execute_user_input()
    insecure_deserialization()
    insecure_command_execution()
