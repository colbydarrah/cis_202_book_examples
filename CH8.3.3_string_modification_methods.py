# Colby Darrah
# 3/23/2021
# string methods pg 446
# string MODIFICATION METHODS

def main():

# lower() -->   returns a copy of the string with all the alphabetic
#               letters converted to lower-case. any character that is
#               already lowercase, or is not alphabetic letter, is unchanged.
        # EXAMPLE 1
                letters = 'WXYZ'
                print(letters, letters.lower())
                #output: WXYZ wxyz
                print()
        # EXAMPLE 2
                again = 'y'
                while again.lower() == 'y':
                    print('hello')
                    print('Do you want to see that again?')
                    again = input('type y for yes, anything else = no: ')
                # expression is TRUE if the again variable references either
                #      upper-case or lowercase Y


# upper() -->   returns a copy of the string with all the alphabetic letters
#               converted to uppercase. ANy character taht is already upper
#               case or is not an alphabetic letter will be unchanged.
                letters2 = 'abcde'
                print(letters2, letters2.upper())
                #output: abcde ABCDE


# lstrip() -->  Returns a copy of the string with all the leading whitesapce
#               characters removed. Leading whitespace characters are spaces,
#               newlines (\n), and tabs (\t) that appear at teh beginning of
#               the string.


# lstrip(char) -->  The char argument is a string containing a character.
#                   Returns a copy of the string with all the instances
#                   of char that appear at the beginning of the string removed.

# rstrip() -->  Returns a copy of the string with all trailing whitespace
#               characters removed (ie: spaces, newlines (\n), and tabs (\t)
#               that appear at the end of the string.

# rstrip(char) -->  The char argument is a string containing a character. The
#                   method returns a copy of the string with all instances of
#                   char that appear at the end of the string removed.

# strip() -->   returns a copy of the string with all leading and trailing
#               white space characters removed.

# strip(char) -->   returns a copy of the string with all instances of char
#                   that appear at the beginning and the end of the string
#                   removed.







# Call the main function
if __name__ == '__main__':
    main()