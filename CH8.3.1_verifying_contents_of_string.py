# Colby Darrah
# 3/23/2021
# spotlight pg 440
# this code uses operator 'in' and 'not in' to determine if one strong
# contains another string

def main():
# EXAMPLE ----- IF-ELSE **IN** to check if string contains smaller string
    text = 'Four score and seven years ago'
    if 'seven' in text:
        print('The string "seven" was found.')
    else:
        print('The string "seven" was not found.')

# EXAMPLE ----- IF-ELSE **NOT IN** to heck if strong doesn't contain
#                                                      smaller string
    print()
    names = 'Bill joanne susan chris juan katie'
    if 'Pierre' not in names:
        print('Pierre was not found.')
    else:
        print('Pierre was found.')


# Call the main function
if __name__ == '__main__':
    main()