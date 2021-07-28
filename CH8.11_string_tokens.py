# Colby Darrah
# 3/23/2021
# 8-9    pg 453
# this program demonstrates how to tokenize strings

def main():
    # Strings to tokenize
    str1 = 'one two three four'
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'
    str4 = '1;2;3;4;5;6'

    # Display the tokens in each string
    display_tokens(str1, ' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3, '/')
    print()
    display_tokens(str4, ';')

    # The display_tokens function displays the tokens in the string.
    # The data parameter is the string to tokenize an the delimiter
    # parameter is the delimiter (ie. a space, :, /, ;)
def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    for item in tokens:
        print(f'Token: {item}')



# Call the main function
if __name__ == '__main__':
    main()