# Colby Darrah
# 3/23/2021
# COPY a list method pg 383
# demonstrates how to copy a list to have 2, separate, but identical lists.

def main():
    # Create a list.
    list_1 = [1, 2, 3, 4, 5]

#=====================FIRST METHOD TO COPY LIST (LESS ELEQUENT)===============
    # Create an empty list
    list_2 = []
    # Copy list_1 to list_2-----
    for item in list_1:
        list_2.append(item)
#======================END FIRST EXAMPLE=====================================

#================SECOND EXAMPLE (MORE ELEQUENT)===============================
    # Create list_2 & copy list_1 to list_2
    list_2 = [] + list_1
#================END SECOND EXAMPLE===========================================

# Call the main function
if __name__ == '__main__':
    main()