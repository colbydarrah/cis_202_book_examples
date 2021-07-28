# Colby Darrah
# 3-8-21
# ch6 example program 6-01

# THis program writes three lines od data to a file

def main():
    # open a file named philosophers.txt.
    outfile = open('philosophers.txt', 'w')

    # write the names of three philosophers to the file
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # close the file
    outfile.close()

# call the main function
if __name__ == '__main__':
    main()
