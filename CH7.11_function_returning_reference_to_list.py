# Colby Darrah
# 3/23/2021
# spotlight 7-11 example pg 389
# program uses a function to create a list and returns a reference to the list
# so list can be used in other parts of program.



def main():
    # Get a list with values stored in it.
    numbers = get_values()

    # Display the values in the list.
    print('The numbers in the list are: ')
    print(numbers)

# The get_values function gets a series of numbes from the user and stores them in
# a list. The function returns a reference to the list.
def get_values():
    # Create an empty list.
    values = []

    # Create a variable to control the loop.
    again = 'y'

    # Get the values from the user and add them to the lsit.
    while again == 'y':
        # Get a number and add it to the list.
        num = int(input('Enter a number: '))
        values.append(num)

        # Want to do this again?
        print('Do you want to add another number? ')
        again = input("type 'y' for yes, 'n' for no: ")
        print()

    # return the list
    return values


# Call the main function
if __name__ == '__main__':
    main()