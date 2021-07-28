# Colby Darrah
# 3/23/2021
# 7-6 removing method pg 380
# demonstrates how to use REMOVE METHOD to remove item from a LIST.

def main():
    # Create a list with some items.
    food = ['pizza', 'burgers', 'chips']

    # Dislay the list
    print('Here are the items in the food list: ')
    print(food)

    # Get the item to change
    item = input('Which item should I remove? ')

    try:
        # Remove the item.
        food.remove(item)

        # Display the list
        print('Here is the revised list: ')
        print(food)

    except ValueError:
        print('That item was not found in the list.')

# Call the main function
if __name__ == '__main__':
    main()