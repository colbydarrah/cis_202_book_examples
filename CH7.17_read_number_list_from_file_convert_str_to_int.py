# Colby Darrah
# 3/23/2021
# Copying a list into a 2nd list pg 398
# two methods

def main():
    # first method (not as streamlined)=====================================
    list1 = [1, 2, 3, 4]
    list2 = []

    for item in list1:
        list2.append(item)
#=========================================================================
# SECOND METHOD (more streamlined
    list1 = [1, 2, 3, 4]
    list2 = [item for item in list1]
#=========================================================================

# # # # to make list of square roots of items in list 1
    list1 = [1, 2, 3, 4]
    list2 = [item for item in list1]


# Call the main function
if __name__ == '__main__':
    main()