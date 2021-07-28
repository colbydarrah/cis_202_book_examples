

# This program demonstrates how numbers must be converted
# to strings before they are written to a text file.

def main()
    # Open a file for writing.
    outfile = open('numbers.txt', 'w')

    # Get three numbers from the user.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter another number: '))

    # Write the numbers to the file.
    outfile.write(str(num1) + '\n') #converts to string
    outfile.write(str(num2) + '\n') #converts to string
    outfile.write(str(num3) + '\n') #converts to string

    # Close the file.
    outfile.close()
    print('Data written to numbers.txt')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT=============
# Enter a number:       22 **enter**
# Enter another number: 14 **enter**
# Enter another number: -99 **enter**
# Data written to numbers.txt
# Data written to numbers.txt
