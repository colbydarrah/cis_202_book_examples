

# This program demonstrates how numbers that are read from a file
# must be converted from strings before they are used in a math
# operation.

def main()
    # Open a file for writing.
    infile = open('numbers.txt', 'r')

    # Read three numbers from the file
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Close the file
    infile.close()

    # Add the three numbers.
    total = num1 + num2 + num3

    # Display the numbers and their total.
    print(f'The numbers are" {num1}, {num2}, {num3}')
    print(f'Their total is: {total}')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT=============
# The numbers are 22, 14, -99
# Their total is: -63
