

# This program prompts the user for sales amounts and writes
# those =amounts to the sales.txt file.

def main()
    # Get the number of days
    num_days = int(input('For how many days do ' +
                         'You have sales? '))

    # Open a new file named sales.txt
    sales_file = open('sales.txt', 'w')

    # Get the amount of sales for each day and write
    # it to the file
    for count in range(1, num_days + 1):
        # Get the sales for a day.
        sales = float(input(f'Enter the sales for the day #{count}: '))

        # Write the sales amount to the file.
        sales_file.write(f'{sales}\n')

    # Close the file
    sales_file.close()
    print('Data written to sales.txt')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT=============
# For how many days do you have sales? 5 *enter
# Enter the sales for day #1: 1000.0
# Enter the sales for day #2: 2000.0
# Enter the sales for day #3: 3000.0
# Enter the sales for day #4: 1000.0
# Enter the sales for day #5: 5000.0
# Data written to sales.txt


