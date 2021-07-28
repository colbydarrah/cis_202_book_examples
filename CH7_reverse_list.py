# Colby Darrah
# 3/23/2021
# reverse order method pg 380
# demonstrates how to use REVERSE the order of items in a LIST.

def main():
    # Create a list with some items.
    food = ['pizza', 'burgers', 'chips']

    # Dislay original order
    print('original order:', food)

    # reverse order
    food.reverse()

    # Display reversed order
    print('Reversed:', food)

# Call the main function
if __name__ == '__main__':
    main()