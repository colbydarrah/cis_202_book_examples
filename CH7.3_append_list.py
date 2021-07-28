# Colby Darrah
# 3/23/2021
# program 7-5 pg 378
# demonstrates how to INSERT into a LIST.

def main():
    # First, create an empty list.
    name_list = []

    # Create a variable to control the loop.
    again = 'y'

    # Add some names to the list
    while again == 'y':
        #Get a name from the user.
        name = input('Enter an name: ')

        # APPEND the name to the list
        name_list.append(name)

        # add another name?
        print('Do you want to add another name?')
        again = input('y = yes, anything else = no: ')
        print()

    # Display the names that were entered.
    print('Here are the names you entered:')
    for name in name_list:
        print(name)


# Call the main function
if __name__ == '__main__':
    main()