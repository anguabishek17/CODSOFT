def generate_password(length):
    
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    symbols = '!@#$%^&*()?'

    all_characters = upper + lower + digits + symbols
    password = ''

    
    for i in range(length):
        index = (i * 7 + 3) % len(all_characters)  
        password += all_characters[index]
    
    return password
def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            password = generate_password(length)
            print("\nGenerated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
