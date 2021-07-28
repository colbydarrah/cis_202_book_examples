# 6-26 pg 348 try /except --- MULTIPLE EXCEPTIONS

# This program uses a TRY / EXCEPT with MULTIPLE EXCEPTS
# to display the total of the amounts in a sales_data.txt file.

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

    # exception if the FILE DOESN'T EXIST **(infile = open('sales_data.txt', 'r')
    # or... program finds PROBLEM READING DATA from the file **(for line in infile: )
    except IOError:
        print('An error occured trying to read the file.')

    # exception for if str entered instead of float **(amount = float(line)
    except ValueError:
        print('Non-numeric data found in the file.')

    # general exception to handle exceptions not covered by IOError or ValueError
    except:
        print('An error occurred.')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+

