# Colby Darrah
# 3/23/2021
# program 7-4 pg 377
# demonstrates how to get the index of an item in a list and then replace
# that item with a new item.

def main():
    # Create a list with some names.
    names = ['James', 'Kathryn', 'Bill']

    # Display the list.
    print('The list before the insert is: ')
    print(names)

    # Insert a new name at element 0.
    names.insert(0, 'Joe')

    # Display the list again.
    print('The list after the insert is: ')
    print(names)


# Call the main function
if __name__ == '__main__':
    main()