import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_numbers, include_special_chars):
    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password):
    with open('passwords.txt', 'a') as file:
        file.write(password + '\n')

def main():
    print("Password Generator")
    print("-------------------")
    
    length = int(input("Enter the desired password length: "))
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, include_lowercase, include_uppercase, include_numbers, include_special_chars)
    if password:
        print("Generated password:", password)
        save = input("Do you want to save this password? (y/n): ").lower() == 'y'
        if save:
            save_password(password)
            print("Password saved to passwords.txt")
    
if __name__ == '__main__':
    main()
