# Colby Darrah
# 3/23/2021
# program sorting list pg 379
# demonstrates how to SORT a LIST.

def main():
    # Create a list with some names.
    names = ['James', 'Kathryn', 'Bill', 'Aaron']
    print('Original Order:', names)
    names.sort()
    print

    # Display the list.
    print('The list before the insert:')
    print(names)

    # Insert a new name at element 0.
    names.insert(0, 'Joe')

    # Display the list again
    print('The list after the insert:')
    print(names)

# Call the main function
if __name__ == '__main__':
    main()