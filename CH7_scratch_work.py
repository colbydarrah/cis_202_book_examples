# Colby Darrah
# 3/23/2021
# program 7-1 pg 367
# sales_list example shows how user input can be assigned to the elements of
# a list.

# The NUM_DAYS constant holds the number of days that we will gather sales
# data for.
NUM_DAYS = 5

def main():
    # Create a list to hold the sales for each day.
    sales = [0] * NUM_DAYS

    print('Enter the sales for each day.')

    # Get the sales for each day.
    for index in range(len(sales)):
        sales[index] = float(input(f'Day #{index + 1}: '))

    # Display the values entered.
    print('Here are the values you entered: ')
    for value in sales:
        print(value)

# Call the main function
if __name__ == '__main__':
    main()