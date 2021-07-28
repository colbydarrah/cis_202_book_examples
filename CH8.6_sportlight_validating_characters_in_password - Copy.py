# Colby Darrah
# 3/23/2021
# SPOTLIGHT pg 448
# VALIDATING THE CHARACTERS IN A PASSWORD

#password must be at least 7 characters long, have 1 upper case, 1 lower case,
# and 1 number
# program must accept password as argument and validate it meets criteria.
# **********program uses earlier spotlight code to get user ID too***********
def main():
    first_name, last_name, id_number = get_user_input()
    login_name = get_login_name(first_name, last_name, id_number)
    display_login_name(login_name)
    is_valid = valid_password(password)
# --------FUNCTION to get USER ID user input ---------------------------------
def get_user_input():
    first_name = input('Enter you first name: ')
    last_name = input('Enter you last name: ')
    id_number = input('Enter you ID number: ')
    return first_name, last_name, id_number

# -------- Function to create login name -------------------------------------
def get_login_name(first_name, last_name, id_number):
    # get first 3 letters of first name.
    # if name is <3 characters, use entire 1st name
    set1 = first_name[0:3]
    # get first 3 letters of last name.
    # if name is <3 characters, use entire last name
    set2 = last_name[0:3]
    # get first 3 characters of student ID number.
    # if name is <3 characters, use entire ID number
    set3 = id_number[-3:]

    # join sets together
    login_name = set1 + set2 + set3

    return login_name

# --------- FUNCTION to display login name
def display_login_name(login_name):
    print('Your system login name is: ')
    print(login_name)

# the valid_password function accepts a password as an argument and returns
# either true or false to indicate whether the password is valid. a valid
# password must be at least 7 characters long, have at least 1 uppercase, 1
# lowercase, and 1 digit.
def valid_password(password):
    # Set the boolean variables to false.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Begin the validation. Start by testing length.
    if len(password) >= 7:
        correct_length = True

        # Test each character and set the appropriate flag when a required
        # character is found.
        for character in password:
            if character.isupper():
                has_uppercase = True
            if character.islower():
                has_lowercase = True
            if character.isdigit():
                has_digit = True
    # Determin ewhether all of the requirements are met. If they are, set
    # is_valid to true. Otherwise, set is_valid to false.
    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False
    return is_valid


# Call the main function
if __name__ == '__main__':
    main()