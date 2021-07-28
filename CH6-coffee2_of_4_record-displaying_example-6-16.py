# 6-16 ....2 of 4 programs used by coffee company to manage
#          inventory.

# This program displays records in the coffee.txt file.

def main():
    # Open the coffee.txt file.
    coffee_file = open('coffee.txt', 'r')

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Display the record
        print(f'Description: {descr}')
        print(f'Quantity: {qty}')

    # Close the file
    coffee_file.close()

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+

