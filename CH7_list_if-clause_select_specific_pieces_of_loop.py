# Colby Darrah
# 3/23/2021
# IF CLAUSES pg 398
# Use "if-clause" to select only certain elements whne processing a list.
# this code only selects integers from the list taht are less than 10

def main():
#========================= NUMBERS ============================================
    ####### EXAMPLE ##############################
    list1 = [1, 12, 2, 20, 3, 15, 4]
    list2 = []
    for n in list1:
        # the "IF" statement appears inside for-loop causing
        # code to only append elements that are <10 to list2.
        if n < 10:
            list2.append(n)
    ######## EXAMPLE USING COMPREHENSION #########
    list1 = [1, 12, 2, 20, 3, 15, 4]
    list2 = [item for item in list1 if item < 10]

# ===================== STRING =================================================
    ######## EXAMPLE #############################
    # if clause selects only names that are less than 6 characters long
    last_names = ['jackson', 'smith', 'hildebrandt', 'jones']
    short_names = [name for name in last_names if len(name) < 6]

    print(short_names)




# Call the main function
if __name__ == '__main__':
    main()