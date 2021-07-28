# Colby Darrah
# 3/23/2021
# 8-9    pg 453
# this program demonstrates the split operator. the Split operator
# turns a string with multiple words into a list (using the spaces
# between the words to split the items in the list)

def main():
    # Create a string with multiple words.
    my_string = 'one two three four'

    # Split the string.
    word_list = my_string.split()

    # Print the list of words.
    print(f'string: {my_string}')
    print('    vs')
    print(f'list: {word_list}')

    print('------------------------------------')
 # use "/" to split if splitting string containing forward (/) slash
    # create string containing forward-slash
    date_string = '11/26/2020'
    date_list = date_string.split('/')
    print(f'date string: {date_string}')
    print('       vs')
    print(f'date list: {date_list}')


# Call the main function
if __name__ == '__main__':
    main()