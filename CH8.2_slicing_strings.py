# Colby Darrah
# 3/23/2021
# 8.2 pg 439
# slicing strings, w step value, neg step value

def main():
# EXAMPLE 1 ------------------------------------------------------------
    #this is the format:
    # string[start_slice_index : end_slice_index]
    full_name = 'Patty Lynn Smith'
    middle_name = full_name[6:10]
    first_name = full_name[:5]
    last_name = full_name[11:]
    print(full_name)
    print(f'{last_name}, {first_name} {middle_name}')

#   name = full_name[:]
#        -- is equal to --
#   name = full_name [0: len(full_name)]

# EXAMPLE 2 ------SLICING W STEP VALUE--------------------------------
    print()
    # slicing characters w STEP VALUE, so slice is not consecutive
    letters = 'abcdefghijklmnopqrstuvwxyz'
    print(letters[0:26:2])
    # 0 is the starting point
    # 26 is the ending point
    # 2 is the step value

# EXAMPLE 3 ------SLICING W NEGATIVE STEP VALUE--------------------------------
    print()
    full_name2 = 'Jon raymond doe'
    last_name2 = full_name2[-3:]
    print(last_name2)


# Call the main function
if __name__ == '__main__':
    main()