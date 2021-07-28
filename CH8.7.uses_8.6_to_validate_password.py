# Colby Darrah
# 3/23/2021
# 8-7 spotlight  pg 451
# this program gets a password from the user and validates it using the
# login.py program

import login
def main():
    # Get a password from the user.
    print('Password must be at least 7 digits long.')
    print('Password must have lat least 1 uppercase letter, 1 lowercase letter,')
    print('and 1 number.')
    print()
    password = input('Enter your password: ')

    # Validate the password.
    while not login.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')
    print('That is a valid password')


# Call the main function
if __name__ == '__main__':
    main()