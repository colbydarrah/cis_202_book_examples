# Colby Darrah
# 3/23/2021
# spotlight pg 440
# this program creates a login name for users using the 1st 3 characters
# of the users first name, last name, and last 3 of student ID number.

def main():
    first_name, last_name, id_number = get_user_input()
    login_name = get_login_name(first_name, last_name, id_number)
    display_login_name(login_name)

def get_user_input():
    first_name = input('Enter you first name: ')
    last_name = input('Enter you last name: ')
    id_number = input('Enter you ID number: ')

    return first_name, last_name, id_number


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

def display_login_name(login_name):
    print('Your system login name is: ')
    print(login_name)


# Call the main function
if __name__ == '__main__':
    main()