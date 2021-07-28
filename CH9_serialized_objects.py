# Colby Darrah
# 3/23/2021
#  pg 506
# Serialized Objects
#       1. pickling object pg 506
#       2. unpickling object pg 507

#     * serializing an object it is converted to a stream of bytes that can be easily stored
#       in a file for later retrieval.
#     * sets, dictionaries, lists, tuples, strings, integers, floating points.can all be serialized
#     * This process is referred to as "pickling".
#     * 'import pickle' module to perform steps to pickle an jobect.
#           -open a file for binary writing.
#           - call the pickle module's dump method to pickle object & write to specific file.
#           - after all objects pickled and saved to file, close file.

def main():

# 1. ------ PICKLING OBJECTS TO A FILE ---------------------------------------------------------------
    # statement opens a file named mydata.dat for binary writing.
    outputfile = open('mydata.dat', 'wb')   # use 'wb' as mode when opening a file for binary writing.
    # once file is open for binary writing, call the 'pickle module's' dump function:
    pickle.dump(object, file)   #'object' = variable to pickle
                            # 'file' = is a variable that references a file object
    #save as many pickled objects as you want, then use close method to close file.
#----EXAMPLE - EXAMPLE - EXAMPLE - EXAMPLE ----------
    # import pickle module
    import pickle
    # create dictionary
    phonebook = {'Chris':'444-3333', 'Katie': '111-2222', 'Joanne': '222-4444'}
    # open a file named phonebook.dat for binary writing.
    output_file = open('phonebook.dat', 'wb')
    # call the pickle modules dump function to serialize phonebook dictionary
    #    and write it to the phonebook.dat file
    pickle.dump(phonebook, output_file)
    # close the phonebook.dat file
    output_file.close()

# 2. ------ UNPICKLING / RETRIEVING OBJECTS TAHT HAVE BEEN PICKLED -----------------------------------
    # open file for 'binary reading' = 'rb':
    inputfile = open('mydata.dat', 'rb')
    # call the pickle modules load function retrieve object and unpickle
    object = pickle.load(file)      # OBJECT is a variable
                                    # FILE is variable that references a file object.
    # you can unpickle as many objects as necessary from the file.
    # once finished, close the the file.
    # ---- EXAMPLE EXAMPLE EXAMPLE EXAMPLE ---
    # inport pickle module
    import pickle
    # open file named phonebook.dat for binary reading
    input_file = open('phonebook.dat', 'rb')
    # calls pickle module's 'load function' to get and unpickle object from phonebook.dat file
    #   assign that object to variable 'pb'.
    pb = pickle.load(inputfile)

    pb
    ## pb now equals: {'Chris':'444-3333', 'Katie': '111-2222', 'Joanne': '222-4444'}
    # close file
    input_file.close()



# Call the main function
if __name__ == '__main__':
    main()