
def password(password_length):
    
    import string
    import secrets

    # Define character sets for password generation

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    # This ensures the password will have a mix of uppercase, digits, special chars, and lowercase
    all_characters = uppercase + digits + punctuation + lowercase
    
    # Generate password by randomly selecting characters from all_characters
    # secrets.choice() provides cryptographically secure random selection (better than random.choice())
    # This comprehension creates password_length random characters and joins them into one string
    password = ''.join(secrets.choice(all_characters) for _ in range(password_length))
    return password


if __name__ == "__main__":  
    password_length = int(input("Enter the desired password length: "))
    print("Generated Password:", password(password_length))