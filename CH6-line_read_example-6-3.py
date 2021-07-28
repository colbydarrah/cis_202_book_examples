# Colby Darrah
# 3-8-21
# ch6 example program 6-01

# This program reads the contents of the philosophers.txt
# file one line at a time.

def main():
    # Open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Read three lines from the file.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # close the file.
    infile.close()

    # print the data that was read into memory.
    print(line1)
    print(line2)
    print(line3)

# call the main function
if __name__ == '__main__':
    main()
