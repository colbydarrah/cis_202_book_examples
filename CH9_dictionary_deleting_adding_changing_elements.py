# Colby Darrah
# 3/23/2021
#  pg 470
# DICTIONARIES
# Creating
# retrieving data from
# adding to / changing data in dictionary
# deleting elements
# getting number of elements in dictionary
# mixing data types in dictionary   ie. lists, strings, ints, tuples
# creating an empty dictionary
# using FOR-LOOP with dictionary

def main():
# ------- CREATING a dictionary called 'phonebook' -----------------------------------------
# dictionary = {'key':'value', 'key':'value'}
phonebook = {'Chris':'555-1234', 'Katie':'333-1234', 'Jimmy':'222-2222'}


# ------ RETRIEVING dictionary value --------------------------------------------------------
#dictionary_name[key]
phonebook['Chris']   # elements ARE case sensitive
# prevent traceback errors by using if-else statement when retrieving
if 'Chris' in phonebook:
    print(phonebook['Chris'])
else
    print('Chris is not in the dictionary')


# ------- ADDING/CHANGING ELEMENTS to an existing dictionary --------------------------------
# adds samanatha and her number to Dictionary
phonebook['Samantha'] = '777-7788'
# changes Chris's phone number in dictionary
phonebook['Chris'] = '111-1111'


# ------- DELETING ELEMENTS ------------------------------------------------------
# del dictionary_name[key]
del phonebook['Chris'] # deletes 'Chris' and Chris's number


# ------- Getting NUMBER OF ELEMENTS in dictionary -------------------------------
# use len()
number_of_dict_elements = len(phonebook)


# ------- MIXING DATA TYPES in dictionary ----------------------------------------
# =====LISTS==== as Elements
test_scores = {'Kayla':[12,93,45], 'Luis':[95,35,23], 'Tim':[56,43,67]}
# each key and element can be different: string vs list, vs integer
mixed_elements = {'abc':1,           # key=string, element=int
                  999: 'yada yada'   # key=int, element=string
                  (3,6,9):[3,6,9]}   # key=tuple, element=list
# example with employee:
employee= {'name':'Keven Smith', 'id': 1234, 'payrate': 25.75}


# ------ creating EMPTY DICTIONARY --------------------------------------------
phonebook = {}
# OR OR  OR  OR  OR
phonebook = dict()



# ------- using FOR-LOOP to ITERATE over dictionary --------------------------------
# for VARIABLE in DICTIONARY
#   statement... etc
for key in phonebook:   # everytime loop iterates 'key' is assigned a key
    print(key)
# output:
    # name
    #name etc
for key in phonebook:
    print(key, phonebook[key])
#output:
    # name number
    # name number   etc



# Call the main function
if __name__ == '__main__':
    main()