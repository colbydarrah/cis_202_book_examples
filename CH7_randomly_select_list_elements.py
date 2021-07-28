# Colby Darrah
# 3/23/2021
# randomly select element from list pg 393
# Random module provides a function named choice that randomly selects
# an element in a list.
# The list is passed as an argument to the function, the function returns
# a randomly selected element. you must IMPORT RANDOM MODULE. ie, import random.

import random

def main():

# random module for names:
    names = ['Jenny', 'Kelly', 'Chloe', 'Aubrey']
    winner = random.choice(names)
    print(winner)

# Random module for numbers:
    numbers = [1,2,3,4,5,6,7,8,9,10]
    # the 'K' at the end signifies how many random numbers you want selected
    selected = random.choices(numbers, k=2)
    print(selected)

# Sometimes Random Module above can return duplicate elements from list
# To randomly select unique elements, use the random module SAMPLE FUNCTION
# instead:
    numbers = [1,2,3,4,5,6,7,8,9,10]
    selected = random.sample(numbers, k=3)
    print(selected)

# Call the main function
if __name__ == '__main__':
    main()