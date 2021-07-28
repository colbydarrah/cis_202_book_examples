# Colby Darrah
# 3/23/2021
# 8.1.1 pg 434
# use index [ ] to get specific character in the string.

def main():
# EXAMPLE 1 ------------------------------------------------------------
    # create variable with string.
    my_string = 'Roses are red'
    # assign the character in the 6th position (sale starting at 0) to
    # variable 'ch'.
    ch = my_string[6]
    print(f'ch equals {ch}, the character in the 6th position.')

# EXAMPLE 2 ------------------------------------------------------------
    # now print character in 0 position, 6 position, and 10 position
    print(my_string[0], my_string[6], my_string[10])

# EXAMPLE 3 ------------------------------------------------------------
    # use negative #s to find character positions relative to the end
    # of the string
    # [-1] is the last character in the string, [-2] is second to last, etc.
    print(my_string[-1], my_string[-2], my_string[-13])

# Example 4 ------------------------------------------------------------
    # while loop to print characters in list.
    # IndexError will occur if index is out of range of string.
    # ie... while index < 7: (bc 'boston' doesn't have 7 characters)
    city = 'Boston'
    index = 0
    while index < 6:
        print(city[index])
        index += 1

# Call the main function
if __name__ == '__main__':
    main()