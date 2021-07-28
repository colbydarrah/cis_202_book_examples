# Colby Darrah
# 3/23/2021
#  pg 508
# This program demonstrates object pickling

import pickle

def main():
    again = 'y'   # set variable to control repetition loop
    output_file = open('info.dat', 'wb') # Open a file for binary writing.
    while again.lower() == 'y': # Get data until the user wants to stop
        save_data(output_file)  # get data about a person and save it.

        again = input('Enter more data? (y/n): ') # does the user want to enter more data?

    output_file.close() # close the file

# ---- FUNCTION to get data about a person, store in dictionary, & pickles dictionary to file.
def save_data(file):
    person = {}      # Create an empty dictionary.

    # Get data for a person and store it in the dictionary.
    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))

    # Pickle the dictionary.
    pickle.dump(person, file)

# Call the main function
if __name__ == '__main__':
    main()