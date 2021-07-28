

# This program reads the contents of the philosophers.txt
# file one line at a time... but uses rstrip to get rid of
# extra line.

#=======================================================
# ***rstrip removes specific characters from right end of string
# so you don't get extra spaces between strings in file
# name = 'Joanne Jones\n'
# name = name.rstrip('\n')
# #========================================================

def main():
    # Open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Read three lines from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    #Strip the \n from each string.
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    # Close the file
    infile.close()

    # Print the data that was read into memory.
    print(line1)
    print(line2)
    print(line3)

# call the main function
if __name__ == '__main__':
    main()

# ==============OUTPUT=========================
# John Locke
# EDavid Hume
# Edmund Burke