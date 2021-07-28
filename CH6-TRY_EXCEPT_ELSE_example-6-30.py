# 6-30 pg 352 TRY / EXCEPT / ELSE

# ELSE suite (statement after Else Clause) executes after statements in the TRY
# suite, but only if no exceptions were raised. If an exception is raised, the
# ELSE suite is skipped.


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

    except Exception as err:
        print(err)

    else:
        # print the total.
        print(f'{total:,.2f}')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+

