# Colby Darrah
# 3/23/2021
# 'del' method pg 381
# demonstrates how to use 'del' method to remove specific index from a LIST.

def main():
    # Create a list.
    list_numbers = [1, 2, 3, 4, 5]

    # Display before deletion.
    print('Before deletion:', list_numbers)

    # Delete specific index inside list
    del list_numbers[2]

    # Display list after deleting specific index
    print('After deletion:', list_numbers)

# Call the main function
if __name__ == '__main__':
    main()