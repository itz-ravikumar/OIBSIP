import string
import random

def get_password_length():
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length >= 8:
                return length
            else:
                print("Length must be at least 8. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_character_types():
    while True:
        print("\nSelect character types to include (at least 2):")
        inc_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        inc_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        inc_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        inc_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        selected_count = sum([inc_upper, inc_lower, inc_numbers, inc_symbols])
        if selected_count >= 2:
            return inc_upper, inc_lower, inc_numbers, inc_symbols
        else:
            print("You must select at least 2 character types. Please try again.")

def generate_password(length, inc_upper, inc_lower, inc_numbers, inc_symbols):
    char_pool = ""
    guaranteed_chars = []
    
    if inc_upper:
        char_pool += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if inc_lower:
        char_pool += string.ascii_lowercase
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if inc_numbers:
        char_pool += string.digits
        guaranteed_chars.append(random.choice(string.digits))
    if inc_symbols:
        char_pool += string.punctuation
        guaranteed_chars.append(random.choice(string.punctuation))
        
    # Generate the rest of the password
    remaining_length = length - len(guaranteed_chars)
    password = guaranteed_chars + [random.choice(char_pool) for _ in range(remaining_length)]
    
    # Shuffle the password list so guaranteed characters aren't always at the beginning
    random.shuffle(password)
    
    return "".join(password)

def main():
    print("Welcome to the Random Password Generator!")
    while True:
        length = get_password_length()
        inc_upper, inc_lower, inc_numbers, inc_symbols = get_character_types()
        
        password = generate_password(length, inc_upper, inc_lower, inc_numbers, inc_symbols)
        print(f"\nGenerated Password: {password}\n")
        
        another = input("Generate another password? (y/n): ").strip().lower()
        if another != 'y':
            print("Thank you for using the Random Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
