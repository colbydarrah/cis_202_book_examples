# Colby Darrah
# 3/23/2021
# tuples pg 404
# shows creation of TUPLE & how FOR-LOOP can iterate over elements of TUPLE


def main():
    # use parenthesis, not brackets
    my_tuple = (1, 2, 3, 4, 5)
    # Print the tuple
    print(my_tuple)

#==========================================================================================
    # use FOR-LOOP to iterate through tuple
    names = ('holly', 'warren', 'ashley')
    for n in names:
        print(n)

#===========================================================================================
    # INDEXing in a tuple
    names = ('holly', 'warren', 'ashley')
    for i in range(len(names)):
        print(names[i])

    # Tuples DO support:                            Tuples DO NOT support:
    # subscript indexing                                # append
    # methods such as index                             # remove
    # built in functions like len,min,&max              # insert
    # slicing expressions                               # reverse
    # the 'in' operator                                 # sort
    # the '+' and '*' operator


# Call the main function
if __name__ == '__main__':
    main()

