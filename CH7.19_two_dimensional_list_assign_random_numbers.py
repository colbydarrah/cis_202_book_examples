# Colby Darrah
# 3/23/2021
# 7-19 pg 403
# Program assigns random numbers to a two-dimensional list.

import random

# create list of months
# function generate amount of rainfall
# function to insert rainfall for each month
# function calculating and displaying total rainfall for year.
# function to calculate average monthly rainfall
# function determining months with greatest and lowest amount of rain



# Constants for rows and columns.
ROWS = 3
COLS = 4

def main():
    # Create a two-dimensional list.
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    # Fill the list with random numbers.
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)

    # Display random numbers.
    print(values)

# Call the main function
if __name__ == '__main__':
    main()

