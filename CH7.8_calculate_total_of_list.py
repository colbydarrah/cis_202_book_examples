# Colby Darrah
# 3/23/2021
# spotlight 7-08 example pg 385
# program calculates the total of a list.

# NUM_EMPLOYEES is used as a constant for the size of the list.
NUM_EMPLOYEES = 6

def main():
    # Create a list.
    numbers = [2, 4, 6, 8, 10]

    # Create a variable to use as an accumulator.
    total = 0

    # Calculate the total of the list elements.
    for value in numbers:
        total += value

    # Display the total of the list elements.
    print(f'The total of the elements is {total}.')

# Call the main function
if __name__ == '__main__':
    main()