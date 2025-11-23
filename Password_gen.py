import random
import string

def generate_password(length=12):

    
    characters = string.ascii_letters  
    characters += string.digits        
    characters += string.punctuation   

   
    if length < 4:
        print("Warning: Password length too short. Setting minimum length to 4.")
        length = 4

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    
    
    while True:
        try:
            
            pass_length = int(input("Enter the desired length of the password (e.g., 12): "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

   
    new_password = generate_password(pass_length)
    
    print("\n--- Your New Strong Password ---")
    print(new_password)
    print("--------------------------------")
