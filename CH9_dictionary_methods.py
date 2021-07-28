# Colby Darrah
# 3/23/2021
#  pg 475
# DICTIONARY METHODS

# clear     method
# get       method
# items     method
    # FOR-LOOP with tuple from item
# keys      method
# pop       method
# popitem   method
# values    method

def main():

# ---- CLEAR METHOD -------------------------------
# deletes all elements in a dictionary
# dictionary_name.clear()
# create list:
phonebook = {'Chris': '555-1234', 'Katie': '333-1234', 'Jimmy': '222-2222'}
# clear list
phonebook.clear()


# ---- GET METHOD ---------------------------------
# use as an alternative to [ ] operator for getting value from dictionary
# GET METHOD does not raise exception if the specified key is not found
# dictionary.get(key, default)     ******DEFAULT if key not found********
value = phonebook.get('Chris', 'Entry not found') # gets 'Chris'
    # or gets 'entry not found'


# ---- ITEMS METHOD ------------------------------
# returns all of a dictionary's keys and their associated values
# they are returned in a special sequence known as 'dictionary view'
# where each element is a tuple containing a key and its assoc. value
phonebook.items()
# method returns:
    # [('Chris': '555-1234'), ('Katie': '333-1234'), ('Jimmy': '222-2222')]


# ---- FOR LOOP to iterate over tuple sequence---pg 477------------------
for key, value in phonebook.items():
    print(key, value)


# ---- KEYS METHOD -----pg 477---------------------------
# returns all of a dictionary's keys as a dictionary view.
phonebook.keys()
# returns: [ 'Chris', 'Katie', 'Jimmy']


# ---- POP METHOD -------pg 478--------------------------------
# returns a value associated with the specified key and
# removes that key-value pair from the dictionary.
# if key not found, mehtod returs a default value.
# ie
# dictionary.pop(key, default)
phone_number = phonebook.pop('Chris', 'Entry not found')
    # assigns chris's number, '555-1234' to variable 'phone_number
    #  &   removes chris & chris-phone number from dictionary
phone_number = phonebook.pop('Phil', 'Entry not found')
    # returns: 'Entry not found'


# ---- POPITEM METHOD ------pg 479------------------------------
# performs 2 actions:
    # 1. it removes the key-value pair that was LAST ADDED to dictionary
    # 2. returns that key-value pair as a tuple
        # ---- then assign the returned value to variables
key_variable, value_variable = phonebook.popitem()
    # which ever key-value pair last added will be affected


# ---- VALUES METHOD ----- pg 479 -------------------------------
# Returns all the dictionary's values (without the associated keys) in
# dictionary view format
phonebook.values()
    # returns ['555-1234', '333-1234', '222-2222']






# Call the main function
if __name__ == '__main__':
    main()