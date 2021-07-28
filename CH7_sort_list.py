# Colby Darrah
# 3/23/2021
# program sorting list pg 379
# demonstrates how to SORT a LIST.

def main():
    # Create a list with some names.
    names = ['James', 'Kathryn', 'Bill', 'Aaron']
    print('Original Order:', names)
    names.sort()
    print('Sorted order:', names)


    # Create a list with some numbers.
    number_list = [9, 5, 3, 8, 4, 7, 1, 0, 6, 2]
    print('Original Order:', number_list)
    number_list.sort()
    print('Sorted order:', number_list)


# Call the main function
if __name__ == '__main__':
    main()