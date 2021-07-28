# Colby Darrah
# 3-8-21
# ch6 example program 6-01

# This program reads and displays the contents of the
# philosophers.txt file.

def main():
    # open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Read the file's contents.
    file_contents = infile.read()

    # Close the file.
    infile.close()

    #Print the data that was read into memory.
    print(file_contents)

# call the main function
if __name__ == '__main__':
    main()
