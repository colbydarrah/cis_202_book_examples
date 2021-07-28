# Colby Darrah
# 3/23/2021
#  pg 494
# SETS
    # 1. Creating empty set
    # 2. passing arguments to set
    # 3. getting number of elements in set
    # 4. Adding to set       pg 496
    # 5. removing from set   pg 496
    # 6. FOR-LOOP to iterate over set pg 497
    # 7. IN & NOT-IN  operators to test for a value in a set pg 497
    # 8. FINDING the UNION of set pg 498
    # 9. finding the INTERSECTION of sets pg 499
    # 10. finding the DIFFERENT OF SETS pg 499
    # 11. finding the SYMMETRIC DIFFERENT OF SETS PG 500
    # 12. finding SUBSETS & SUPERSETS pg 501
    # 13. Set COMPREHENSIONS  pg 504


# a SET is an object that stores a collection of data in the same way as mathematical sets.
#       - all elements in set must be UNIQUE, none can have the same value
#           >> set('aaabc') will save as set('abc')
#       - set elements are unordered
#       - set elements can be different data types
#       - arguments passed to set must be iterable elements = list, tuple, string

def main():
    # 1. ----- CREATING an EMPTY SET --------------------------------------------------------------
    myset = set()

# 2. ----- PASSING arguments to SET ---------------------------------------------------------------
    # ---- passing a list ---------------
    myset - set(['a', 'b', 'c'])
    # ---- passing a string -------------
    myset = set('abc')

# ---- UNABLE to create set which each element is string containing more than 1 character
    myset = ('one', 'two', 'three') # WONT WORK bc it contains multiples of the same character
    # >>>>>INSTEAD<<<<<<
    # items must be passed as a list
    myset = set(['one', 'two', 'three']) # WILL WORK bc elements are the words, not the letters

# 3. ---- GETTING NUMBER OF ELEMENTS IN SET ------------------------------------------------------
    myset = set([1,2,3,4,5])
    len(myset)

# 4. ----- ADDING ELEMENTS ----------------------------------------------------------------------
    # ----- ADDING TO EMPTY SET -------------------
    myset = set()
    myset.add(1) # adds 1 to empty set
    myset.add(2) # adds 2 to set of 1
    myset.add(3) # adds 3 to set 12
    # will return a set of 1, 2, 3
    #----- ADDING TO EXISTING SET -----------------
    myset = set([1,2,3])   # creates set of 123
    myset.update([4,5,6])  # adds 456 to set of 123
    # will return a set of 1,2,3,4,5,6
    #----- ADDING 1 SET TO ANOTHER ----------------
    set1 = set([1,2,3])     # creates one set with 1,2,3
    set2 = set([8,9,10])    # creates second set with 8,9,10
    set1.update(set2)       # adds set 2 to set 1 (set1 1,2,3,8,9,10)
    #----- ADDING STRING TO NUMBER SET ------------
    myset = set([1,2,3])    # creates set of 1,2,3
    myset.update('abc')     # updates myset to include 'abc'
    # returns {'a', 1, 2, 3, 'c', 'b'}

# 5. ----- REMOVING ELEMENTS ----------------------------------------------------------------------
    # -- using REMOVE METHOD -------->> EXCEPTION RAISED if element not found in set
    myset = set([1,2,3,4,5])    # creates set of 1,2,3,4,5
    myset.remove(1)             # removes 1 from set, leaving 2,3,4,5
    # -- using DISCARD METHOD ----->> NO EXCEPTION raised if element not found in set
    myset.discard(5)            # removes 5 from set, leaving 2,3,4

# 6. ----- FOR-LOOP to iterate over a set -----------------------------------------------------
    myset = set(['a', 'b', 'c'])
    for set_variable in myset:
        print(set_variable)
    # will print a b c

# 7. ----- IN / NOT IN to test if value exists in a set ----------------------------------------
    myset = set([1,2,3])
    if 1 in myset:
        print('The value 1 is in the set.')

    if 99 not in myset:
        print('The value 99 is not in the set.')

# 8. ----- FINDING the UNION of set -----------------------------------------------------------
    set1 = set([1,2,3,4])       # create set 1
    set2 = set([3,4,5,6])       # create set 2
    set3 = set1.union(set2)     # set 3 is the union of set1 and set2
    # set3 would equal {1,2,3,4,5,6) ####NO DUPLICATES (OF 3 in this case)

    # --- using "|" to find/create union of two sets --------------------
    set1 = set([1, 2, 3, 4])    # create set 1
    set2 = set([3, 4, 5, 6])    # create set 2
    set3 = set1 | set2          # set3 is union of set1 and set2
    # set3 would equal {1,2,3,4,5,6) ####NO DUPLICATES (OF 3 in this case)

# 9. ----- finding the INTERSECTION of sets ---------------------------------------------------
    # the intersection of two sets is a set that contains only the elements that are found
    #      in both the other sets.
    #----- INTERSECTION METHOD to find intersection -------------
    set1 = set([1, 2, 3, 4])  # create set 1
    set2 = set([3, 4, 5, 6])  # create set 2
    set3 = set1.intersection(set2)  # only includes elements common to both set 1 and set 2
    # set3 would equal {3,4}
    # ----- "&" OPERATOR to find INTERSECTION -------------------
    set1 = set([1, 2, 3, 4])  # create set 1
    set2 = set([3, 4, 5, 6])  # create set 2
    set3 = set1 & set2
    # set3 would equal {3,4}

# 10. ------ finding the DIFFERENT OF SETS -----------------------------------------------------
    # the Difference is the elements that appear in set1 but do not appear in set2
    #---- DIFFERENCE METHOD to find difference -------------
    set1 = set([1, 2, 3, 4])  # create set 1
    set2 = set([3, 4, 5, 6])  # create set 2
    set3 = set1.difference(set2)
    # set3 would equal {1,2}
    # ---- "-" OPERATOR to find difference -----------------
    set1 = set([1, 2, 3, 4])  # create set 1
    set2 = set([3, 4, 5, 6])  # create set 2
    set3 = set1 - set2
    # set3 wold equal {1,2}

# 11. ------ finding the SYMMETRIC DIFFERENT OF SETS ---------------------------------------------
    #Symmetric difference of two sets is a set that contains elements that are not shared by
    #both sets. i.e. elements that R in one set, but not in both.
    # --- SYMMETRICK DIFFERENCE to find difference ---------
    set1 = set([1, 2, 3, 4])  # create set 1
    set2 = set([3, 4, 5, 6])  # create set 2
    set3 = set1.symmetric_difference(set2)
    # set3 equals {1,2,5,6}
    # ---- "^" OPERATOR to find difference ----------------
    set1 = set([1, 2, 3, 4])  # create set 1
    set2 = set([3, 4, 5, 6])  # create set 2
    set3 = set1 ^ set2
    # set3 equals {1,2,5,6}

# 12. ------ finding SUBSETS & SUPERSETS -----------------------------------------------------
    # When set1 set contains all the elements of set2 & more, set2 is a SUBSET of set1.
    # Also, set1 is a SUPERSET of set2
    set1 = set([1,2,3,4])
    set2 = set([2,3])
    # ---- SUBSET SUBSET SUBSET SUBSET -----------------
    # use "issubset method" to determine whether one set is subset of another.
        set2.issubset(set1)
        # ------ OR OR OR OR OR OR -------
        set2 <= set1
    # method returns "True" if set2 is subset of set1, otherwise returns "False".
    # ---- SUPERSET SUPERSET SUPERSET SUPERSET ---------
    # use "issuperset method" to determine whether one set is superset of another.
        set1.issuperset(set2)
        # ------ OR OR OR OR OR OR -------
        set1 >= set2   # book says "set1 >= set2" if set1 is subset of set2.
    # method returns "True" if set1 is a superset of set2, otherwise returns "False".
    # i.e.
    set1 = set([1, 2, 3, 4])
    set2 = set([2, 3])
    set2.issubset(set1)
    # OR OR OR OR
    set2 <= set1
    # returns True
    set1.issuperset(set2)
    # or or or or
    set1 >= set2         # not sure if this means set1 is superset of set 2
    # returns True.

# 13. ------- SET COMPREHENSIONS -------------------------------------------------------------
        # a set comprehension is an epession that reads a sequence of input elements and
        #  uses those input elements to produce a set. Set comprehensions work like list
        #  list comprehensions, except that a set comprehension is enclosed in curly brackets {},
        #  where list comprehensions are enclosed in square brackets [].
    # copying set using set comprehension:
        # create set
        set1 = set([1,20,2, 3,40,5, 7, 80])
        # use set comprehension to make copy of set:
        set2 = {item for item in set1}
        # make copy of set1 w/ squares of set1
        set2 = {item**2 for item in set1}
        # make copy of set1 that contains only integers that R less than 10.
        set2{item for item in set1 if item <10}


# Call the main function
if __name__ == '__main__':
    main()