import random
import string

def generate_password(min_length, numbers=True, special_characters=True): 
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers: 
        characters += digits
    if special_characters: 
        characters += special

    pswd = ''
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pswd) < min_length: 
        new_char = random.choice(characters)
        pswd += new_char

        if new_char in digits: 
            has_number = True
        elif new_char in special: 
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special
        
    return pswd

min_lenght = int(input("Enter the minimum length:"))
has_number = input("Do you want to have numbers (y/n)").lower() == 'y'
has_special = input("Do you want to have special characters (y/n)").lower() == 'y'
pswd = generate_password(min_lenght, has_number, has_special)

print('The generated password is:', pswd)