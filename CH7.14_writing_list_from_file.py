# Colby Darrah
# 3/23/2021
# Saving a list to a file pg 394
# Use a for-loop to iterate through a list, writing each element
# with a terminating new-line character so the list does not run together
# in the file.

#This program saves a list of strings to a file.
def main():
    # Create list of strings
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    # Open a file for writing.
    outfile = open('cities.txt', 'w')

    # Write the list to the file.
    for item in cities:
        outfile.write(item + '\n')

    # Close the file.
    outfile.close()


# Call the main function
if __name__ == '__main__':
    main()