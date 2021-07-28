# 6-19 ....5 of 5 programs used by coffee company to manage
#          inventory.

# This program allows user to delete records from coffee.txt
# This program does this by creating a temporary file where all the
# original file records are copied to...
#    ....EXCEPT the record that is to be deleted.
# The temporary file takes the place of the original file
#      -- you delete the original file
#      -- you rename the temporary file, giving it the name of the original file

#+++++++++++=====GENERAL ALGORITHM for program================================
# Open the original file for input and create a temp file for output
# Get the description of the record to be deleted.
# Read the description field of the first record in the original file.
# While the description is not empty:
#    Read the quantity field
#    If this record's description field does not match the description entered:
#        Write the record to the temporary file.
#    Read the next description field.
# Close the original file and the temporary file.
# delete the original file.
# rename the temporary file, giving it the name of the original file.
#============================================================================

# this program allows the user to delete a record in the coffee.txt file.

# import os for the remove & rename functions
import os

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the coffee record to delete.
    search = input('Which coffee do you want to delete? ')

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

        # If this is not the record to delete, then write it to the temporary file.
        if descr != search:
            # Write the record to the temp file.
            temp_file.write(f'{descr}\n')
            temp_file.write(f'qty}\n')
        else:
            # Set the found flag to True
LINE 38            found = True

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

