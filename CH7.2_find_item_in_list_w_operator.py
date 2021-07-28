# Colby Darrah
# 3/23/2021
# program 7-2 pg 373
# finding item in list with operator

def main():
    # Create a list of product numbers.
    prod_nums = ['V475', 'F987', 'Q143', 'R688']

    # Get a product number to search for.
    search = input('Enter a product number to search for: ')

    # Determine whether the product number is in the list.
    if search in prod_nums:
        print(f'{search} was found in the list.')
    else:
        print(f'{search} was not found in the list.')

# Call the main function
if __name__ == '__main__':
    main()