# TASK 3 · Random Password Generator

## Objective
Build a Python tool that generates strong, random passwords based on user-defined criteria. This is a command-line version designed for beginners.

## Tech Stack
- Python
- `random` module
- `string` module

## Features
- Prompts user to specify desired password length (minimum 8 characters enforced)
- Prompts user to choose which character types to include: uppercase letters, lowercase letters, numbers, symbols (at least 2 types must be selected)
- Generates and displays a password matching all specified criteria
- Input validation: rejects invalid lengths or if fewer than 2 character types are selected
- Option to generate another password without restarting the program

## Usage
Run the script using Python:
```bash
python password_generator.py
```
Follow the on-screen prompts to generate your secure passwords.
