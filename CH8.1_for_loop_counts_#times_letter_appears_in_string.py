# Colby Darrah
# 3/2/2021
# Ex 8-1 pg 434
# This program counts the number of times the letter 'T' (upper case & lower case)
# appears in a string.

def main():
    # Create a variable to use to hold the count.
    # The variable MUST START w ZERO
    count = 0

    # Get a string from the user.
    my_string = input('Enter a sentence: ')

    # Count the Ts.
    for letter in my_string:
        if letter == 'T' or letter == 't':
            count += 1

    # print the result.
    print(f'The letter T appears {count} times.')

# ----------------------------------------------------------------------------------------
# Call the main function
if __name__ == '__main__':
    main()