# Colby Darrah
# 3/23/2021
# string methods pg 444
# this string-methods

# isalnum() --> returns true if the string contains only alphabetic letters
#               or digits and is at least 1 character in length.

# isalpha() --> returns true if string contains only alphabetic letters and
#               is at least 1 character in length.

# isdigit() --> returns true if string contains only numeric digits and
#               is at least 1 character in length

# lslower() --> returns true if all the alphabetic letters in the string
#               are lowercase, and the string contains at least 1
#               alphabetic letter.

# issplace() --> returns true if the string contains only whtespace
#               characters and is at least 1 character in length.
#               (whitespace characters are: spaces, new lines, & tabs)

# isupper() --> returns true if all of the alphabetic letters in the string
#               are uppercase, and the string contains at least 1
#               alphabetic letter

def main():
# -------'isdigit' method returns true of strong contains ONLY NUMERIC DIGITS
    # EXAMPLE 1 ---------------------
    string1 = '1200'
    if string1.isdigit():
        print(f'{string1} contains only digits')
    else:
        print(f'{string1} contains characters other than digits')

    # EXAMPLE 2 -------------------
    print()
    string2 = '123abc'
    if string2.isdigit():
        print(f'{string2} contains only digits')
    else:
        print(f'{string2} contains characters other than digits')

# -----demonstrates several string testing methods:
    print()
    # get string from user:
    user_string = input('Enter a string: ')
    print('info about string from string methods: ')
    if user_string.isalnum():
        print('The string is alphanumeric.')
    if user_string.isdigit():
        print('The string contains only digits')
    if user_string.isalpha():
        print('The string contains only alphabetic characters.')
    if user_string.isspace():
        print('The string contains only whitesapce characters.')
    if user_string.islower():
        print('The letters int he string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase')



# Call the main function
if __name__ == '__main__':
    main()