# 6-29 pg 355 try /except --- 1 except clause to catch ALL EXCEPTIONS


# This program uses one exception clause to catch all exceptions raised in
# in the try suite.
# This program displays the total of the amounts in the sales_data.txt file.

def main():
    # initialize an accumulator.
    total = 0.0

    try:
        # Open the sales_data.txt file.
        infile =  open('sales_data.txt', 'r')

        # Read the values from the file and accumulate them.
        for line in infile:
            amount = float(line)
            total += amount

        # close the file.
        infile.close()

        # Print the total.
        print(f'{total:,.2f}')

    except Exception as err:
        print(err)

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+

