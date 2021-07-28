# 6-15 ....1 of 4 programs used by coffee company to manage
#          inventory.

# This program adds coffee inventory records to the coffee.txt file.

def main()
    # Create a variable to control the loop
    another = 'y'

    # Open the coffee.txt file in append mode.
    coffee_file = open('coffee.txt', 'a')

    # Add records to the file.
    while another == 'y' or another == 'Y':
        # Get the coffee record data.
        print('Enter the following coffee data:')
        descr = input('Description: ')
        qty = int(input('Quantity (in pounds): '))

        # Append the data to the file
        coffee_file.write(descr + '\n')
        coffee_file.write(f'{qty}\n')

        # Determine whether the user wants to add another
        # record to the file.
        print('Do you want to add another record?')
        another = input('Y = yes, anothing else = no: ')

    # Close the file.
    coffee_file.close()
    print('Data appended to coffee.txt.')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+

