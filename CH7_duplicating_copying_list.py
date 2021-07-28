# Colby Darrah
# 3/23/2021
# Copying a list into a 2nd list pg 398
# two methods
# # # also creating list of square roots of items in list 1

def main():
################# FIRST METHOD (not as streamlined)==========================
    ########### EXAMPLE -- NUMBERS ###############
    list1 = [1, 2, 3, 4]
    list2 = []

    for item in list1:
        list2.append(item)

    ############ EXAMPLE -- STRINGS ###############
    str_list = ['winken', 'blinken', 'nod']
    len_list = []
    for s in str_list:
        len_list.append(len(s))
#
#========================================================================
#================= SECOND METHOD (more streamlined) =====================
    ########## EXAMPLE -- NUMBERS ###############
    list1 = [1, 2, 3, 4]
    list2 = [item for item in list1]

    ######### EXAMPLE -- STRINGS ###############
    str_list = ['winken', 'blinken', 'nod']
    len_list = [len(s) for s in str_list]
#=========================================================================

# # # # to make list of square roots of items in list 1
    list1 = [1, 2, 3, 4]
    list2 = [item ** 2 for item in list1]
    print(list2)





# Call the main function
if __name__ == '__main__':
    main()