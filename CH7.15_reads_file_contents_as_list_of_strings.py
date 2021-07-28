# Colby Darrah
# 3/23/2021
# 7-15 getting a list from a file pg 395
# Use READLINES to return a file's contents as a list of strings.
# Each line in the file will be an item in the list
# items in list will include their terminating new line character '\n\,
#        which will need to be stripped.

# Program reads a file's contents into a list, the loop steps through the list,
# stripping the '\n' character from each element.

def main():
    # Open a file for reading.
    infile = open('cities.txt', 'r')

    # Read the contents of the file into a list.
    cities = infile.readlines()

    # Close the file.
    infile.close()

    # Strip the \n from each element.
    for index in range(len(cities)):
        cities[index] = cities[index].rstrip('\n')

    # Print the contents of the list.
    print(cities)

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