# 6-27 pg 349 try /except --- 1 Except clause for MULTIPLE EXCEPTIONS

# This program uses a TRY / EXCEPT t odisplay the total of the amounts in the
# sales_data.txt file.

def main():
    # Initialize an accumulator
    total = 0.0

    try:
        # Open the sales_data.txt file
        infile = open('sales_data.txt', 'r')

        # Read the values from the file and accumulate them.
        for line in infile:
            amount = float(line)
            total += amount

        # Close the file.
        infile.close()

        # Print the total.
        print(f'{total:,.2f}')

    #general / unspecific except to catch all errors.
    except:
        print('An error occurred.')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+

