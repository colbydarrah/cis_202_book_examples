# Colby Darrah
# 3/23/2021
# string methods pg 447
# string SEARCH & REPLACE

def main():
# endswith(substring) -->   The substring argument is a string. The method
#                           returns true if the string ends with substring.
                #EXAMPLE
                    filename = input('Enter the filename: ')
                    if filename.endswith('.txt'):
                        print('That is the name of a text file.')
                    elif filename.endswith('.py'):
                        print('That is the name of a python source file.')
                    elif filename.endswith('.doc'):
                        print('That is the name of a word processing document.')
                    else:
                        print('Unknown file type.')
                    print()

# startswith(substring -->  The substring argument is a string. The method
#                           returns true if the string starts with substring.


# find(substring) -->   The substring argument is a string. The method returns
#                       the lowest index in the string where substring is
#                       found. if substring is not found the mmethod returns
#                       -1.
                #EXAMPLE:
                    string = 'Four score and seven years ago'
                    position = string.find('seven')
                    if position != -1:
                        print(f'The word "seven was found at index {position}.')
                    else:
                        print('The word "seven" was not found.')
                    print()
# replace(old, new) --> The old and new arguments are both strings. The method
#                       returns a copy of the string with all instances of old
#                       replaced by new.
                #EXAMPLE:
                    string = 'Four score and seven years ago'
                    new_string = string.replace('years', 'days')
                    print(new_string)
                    #output: Four score and seven days ago





# Call the main function
if __name__ == '__main__':
    main()