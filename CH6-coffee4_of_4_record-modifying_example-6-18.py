# 6-18 ....4 of 4 programs used by coffee company to manage
#          inventory.

# This program allows user to modify the quantity field in an existing record
# This program does this by creating a second temporary file where all the
# original file's records are copied to...
#       ...but when the program reaches the record to be modified, it DOES NOT
# copy the info.. instead it writes the new modified values to the temporary
# file.
#       ...then continue copying any remaining records from the original
# file to the temporary file.
#       ...The temporary file then takes the place of the original file &
# you delete the original file and rename the temporary file with the original
# file's name

# using:    remove('coffee.txt')                *remove function
#   and     rename('temp.txt', 'coffee.txt')    *rename function
#============================================================================

#import os for the remove & rename functions
import os

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value and the new quantity.
    search = input('Enter a description to search for: ')
    new_qty = int(input('Enter the new quantity: '))

    #Open the original coffee.tx file
    coffee_file = open('coffee.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first record's description field.
    descr = coffee_file.readline()

    #Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description
        descr = descr.rstrip('\n')

        # Write either this record to the temporary file, or the new
        # record if this is the one that is to be modified.
        if descr == search:
            # Write the modified record to the temp file.
            temp_file.write(f'{descr}\n')
            temp_file.write(f'new_qty}\n')

            # Set the found flag to True.
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')

        # Read the next description.
        descr = coffee_file.readline()

    # Close the coffee file and the temporary file.
    coffee_file.close()
    temp_file.close()

    # Delete the original coffee.txt file
    os.remove('coffee.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'coffee.txt')

    # If the search value was not found in the file, display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+

