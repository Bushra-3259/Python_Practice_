# Plans on how to start and what to do in the project
# Collect user preferences
# -length
# -should contain uppercase
# -should contain special
# -should contain digits
# get all available characters 
# randomly pick characters upto the length
# ensure we have at least one of each character type 
# ensure length is valid 

import random #Allows you to use the random module, which provides functions for generating random numbers and performing random operations.
import string #Gives us access to a list of all characters that are lowercase, uppercase, digits, or special characters.

def generate_password():
    length = int( input( "Enter the length of your password: ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    if length < 4:
        print("Password length must be at least 4 characters. ")
        return #Anything below return won't work. it will straight exit the function.
    lower = string.ascii_lowercase #Gives all of the lowercase letters 
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else " " #Inline if statement or ternary statement
    special = string.punctuation if include_special == "yes" else " "
    digits = string.digits if include_digits == "yes" else " "
    all_characters = lower + uppercase + special + digits #Concatenating all strings to a large string

    required_characters = []
    if include_uppercase =="yes":
        required_characters.append(random.choice(uppercase)) #From all the uppercases, choose a random one. Then add/append it to the list named required_characters.
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length): #The underscore is simply a placeholder variable when you dont want to define something.
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)
    
    string_password = "".join(password) #To convert the password to string. The empty string, "", means combine all of the values in a list to a string.
    return string_password              #Inside this empty string, if we use comma, then comma will be given after every single character.

password = generate_password()
print(password)