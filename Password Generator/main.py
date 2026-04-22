def password(password_length):
    

    import string
    import secrets
   
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    

    all_characters =  uppercase + digits + punctuation + lowercase
    
    
    password = ''.join(secrets.choice(all_characters) for _ in range(password_length))
    
    return password

if __name__ == "__main__":  
    # Generate a random password of length specified by the user
    password_length = int(input("Enter the desired password length: "))
    print("Generated Password:", password(password_length))