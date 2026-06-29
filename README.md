Secure Coding Review - CodeAlpha Internship

Author

Fadwa Ben Abdallah

Project Description

This project demonstrates a basic secure coding review. It identifies vulnerabilities in a Python script and provides a secure version of the same program.

Vulnerabilities Found

- Hardcoded password inside the code
- Use of "os.system()" which allows command injection
- No validation of user input
- Lack of security controls

Improvements Made

- Removed unsafe "os.system()" usage
- Used "subprocess.run()" instead
- Restricted allowed commands
- Improved authentication structure
- Used safer input handling

Tools Used

- Python
- Kali Linux
- Manual Code Review

Learning Outcome

Learned how insecure coding practices can lead to security risks and how to write safer Python code.
