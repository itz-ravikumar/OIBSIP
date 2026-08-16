# 🔐 Random Password Generator

> A secure, customizable command-line password generation tool built with Python.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Overview

The **Random Password Generator** is a Python-based command-line utility designed to create strong, secure, and unpredictable passwords. It allows users to define the password length and character composition, ensuring that generated passwords meet specific security requirements.

This project was developed as **Task 3** for the Oasis Infobyte SIP (OIBSIP) internship program, targeting the Beginner tier.

## ✨ Key Features

- **Customizable Length**: Generate passwords from a minimum of 8 up to a maximum of 128 characters.
- **Granular Character Control**: Choose precisely which character types to include:
  - 🔠 Uppercase letters (`A-Z`)
  - 🔡 Lowercase letters (`a-z`)
  - 🔢 Numbers (`0-9`)
  - 🔣 Symbols (`!@#$%^&*` etc.)
- **Security First**: Enforces a minimum selection of at least 2 character types to ensure password strength.
- **Guaranteed Inclusion**: Ensures that at least one character from every selected category is present in the final password.
- **Strict Input Validation**: Rejects invalid lengths, non-numeric inputs, and invalid character type selections immediately with robust error handling.
- **Continuous Generation**: Easily generate multiple passwords in a single session without restarting the program.

## 🚀 Quick Start

### Prerequisites

- **Python 3.x** must be installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/itz-ravikumar/OIBSIP.git
   ```
2. Navigate to the project directory:
   ```bash
   cd OIBSIP/Python-Task3-RandomPasswordGenerator
   ```

### Usage

Run the script directly from your terminal:

```bash
python password_generator.py
```

### Example Workflow

```text
Welcome to the Random Password Generator!
Enter desired password length (8-128): 16

Select character types to include (at least 2):
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): n

Generated Password: aK9bX4mP7vL2qW5z

Generate another password? (y/n): n
Thank you for using the Random Password Generator. Goodbye!
```

## 🛠️ Technology Stack

- **Language**: Python
- **Core Modules**:
  - `random`: Used for cryptographically secure character selection and password shuffling.
  - `string`: Provides standard constants for ASCII letters, digits, and punctuation.

## 📂 Project Structure

```text
Python-Task3-RandomPasswordGenerator/
├── password_generator.py   # Main application script containing all logic
└── README.md               # Project documentation
```

## 🧠 Implementation Details

- **Validation Loop Design**: Utilizes continuous `while True` loops coupled with `try-except` blocks to trap invalid user inputs (e.g., entering letters when a number is expected) without crashing the application.
- **Security Check Mechanism**: The `ask_yes_no()` helper function sanitizes input (stripping whitespace and enforcing lowercase) to rigidly restrict answers to 'y' or 'n'.
- **Guaranteed Entropy**: Instead of simply picking characters from a combined pool, the algorithm first guarantees one random character from each chosen set (uppercase, lowercase, numbers, symbols) is added to a list. It then fills the remaining length from the combined pool and shuffles the list to prevent predictable patterns (e.g., the first character always being uppercase).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👤 Author

**Ravikumar**
- GitHub: [@itz-ravikumar](https://github.com/itz-ravikumar)
- Project Link: [OIBSIP Repository](https://github.com/itz-ravikumar/OIBSIP)

## 🙏 Acknowledgements

- [Oasis Infobyte](https://oasisinfobyte.com/) for providing this internship task and opportunity.
