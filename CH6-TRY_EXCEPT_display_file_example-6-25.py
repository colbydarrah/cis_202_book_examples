# 6-23 pg 344 exception with division

# This program uses a TRY / EXCEPT function while calculating gross pay

def main():
    # Get the name of a file.
    filename = input('Enter a file name: ')

    try:
        # Open the file.
        infile = open(filename, 'r')

        # Read the file's contents.
        contents = infile.read()

        #Display the file's contents.
        print(contents)

        # Close the file.
        infile.close()

    except IOError:
        print('An error occurred trying to read the file', filename)

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+

