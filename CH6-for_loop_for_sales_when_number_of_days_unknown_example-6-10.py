
# A 'For Loop' differs from 'while loop' in that:
#      1. it automatically reads the lines in a file without
#         testing for any special condition that signals the
#         end of the file.
#      2. it does not require a priming read operation before the
#         the loop.
#      3. It automatically stops when the end of the file has
#         been reached.
# 'For-Loop' is used when you simply want to read the lines in a
#      file, one after another.. this technique is simpler and more
#      elegant than using while loop that explicitly tests for an
#      end of the file condition
#
# 'For-loop' general format:
#       for variable in file_object:
#           statement
#           statement
#           etc.

# This program reads all of the values in the sales.txt file.

def main()
    # Open the sales.txt file for reading.
    sales_file = open('sales.txt', 'r')

    # Read all the lines from the file.
    for line in sales_file:
        # convert line to a float.
        amount = float(line)
        # Format and display the amount.
        print(f'{amount:.2f}')

    # Close the file
    sales_file.close()

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT=============
# 1000.00
# 2000.00
# 3000.00
# 4000.00
# 5000.00
