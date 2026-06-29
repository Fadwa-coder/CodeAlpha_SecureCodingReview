import subprocess
import getpass

USERNAME = "admin"
PASSWORD = "StrongPassword@2026"

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

if username == USERNAME and password == PASSWORD:
    print("Login Successful")
else:
    print("Access Denied")

command = input("Enter command: ")

if command == "date":
    subprocess.run(["date"])
elif command == "whoami":
    subprocess.run(["whoami"])
else:
    print("Command not allowed.")
