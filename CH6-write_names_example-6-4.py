

# This program gets three names from the user and writes
# them to a file.

#=======================================================
# the data items that are written to a file are not
# string literals, but values in memory referenced by
# variables. This is the case in a program that prompts
# users to enter data and then writes that data to a file.
# In this case it is necessary to link a \n escape sequence
# to the data before writing it to ensure each piece of
# data is written to a separate line in the file.
#========================================================

def main():
    # Get three names.
    print('Enter the names of three friends.')
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Friend #3: ')

    # Open a file named friends.txt
    myfile = open('friends.txt', 'w')

    # Write the names to the file.
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')
    #====OR=====OR===OR=====OR===OR=============
    # write names to the file using an f-string
    # myfile.write(f'{name1}\n')
    # myfile.write(f'{name2}\n')
    # myfile.write(f'{name3}\n')
    # ==========================================




    # close the file.
    myfile.close()
    print('The names were written to friends.txt')

# call the main function
if __name__ == '__main__':
    main()

# ==============OUTPUT=========================
# Enter the names of three friends.
# Friend #1: Joe **Enter**
# friend #2: Rose **Enter**
# Friend #3: Geri **Enter**
# The names were written to friends.txt.