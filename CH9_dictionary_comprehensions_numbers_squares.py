# Colby Darrah
# 3/23/2021
#  pg 490
# dictionary comprehensions
#   copying list, key=list, value= square of key
#   copying dictionary
#   select only certain elements of dictionary using IF CLAUSE

def main():
# ------- COPY LIST INTO DICTIONARY w squares as values ----------------------------------------
    # copying list, key=list, value= square of key
    # example - turn list of numbers into dictionary of numbers & and their squares
    numbers = [1,2,3,4,5]   #list of numbers
    # dictionary to populate with numbers list & the squares of those elements
    squares = {item:item ** 2 for item in numbers}
    # the above expression begins with the result expression    "item:item**2"
    # the above expression ends with an iteration expression    "for item in numbers"
        # above is the equivelant to:
    #       squares = {}
    #       for item in numbers:
    #            squares[item] = item ** 2


# -------- COPY DICTIONARY ---------------------------------------------------------------------
    # you can also use an existing dictionary as the input to a comprehension.
    # for example, an existing phonebook:
    phonebook={'Chirs':'123-1234', 'Katie':'111-1111', 'Joanne':'222-2222'}
    # this makes a copy of phonebook dictionary:
    phonebook_copy{k:v for k,v in phonebook.itmes()}
        # k:v  ---- is the result expression
        # for k,v in phonebook.items() ---- is the iteration expression


# -------- SELECT CERTAIN ELEMENTS FROM LIST using IF clause -----------------------------------
    populations = {'New York': 8398723, 'Los Angeles': 3990456, 'Chicago': 2705994,
                   'Houston': 2325502, 'Phoenix': 1660272, 'Philadelphia': 1584138}
    # Create a copy of the populations dictionary,
    # BUT... only include cities with a population greater than 2 million
    largest = {}
    for k, v in populations.items():
        if v > 2000000:
            largest[k] = v
    # ---OR  OR  OR  OR  OR  OR  OR  OR  OR ----------
    largest = {k:v for k,v in populations.items() if v > 2000000}





# Call the main function
if __name__ == '__main__':
    main()