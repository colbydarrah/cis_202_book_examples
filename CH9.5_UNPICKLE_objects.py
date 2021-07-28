# Colby Darrah
# 3/23/2021
#  pg 508
# This program demonstrates object unpickling

import pickle

def main():
    end_of_file = False # To indicate end of file
    input_file = open('info.dat', 'rb') # Open a file for binary reading

    while not end_of_file:  # Read to the end of the file
        try:
            person = pickle.load(input_file)    # unpickle the next object.
            display_data(person)                # Display the object

        except EOFError:
            end_of_file = True  # Set flag to indicate end-of-file has been reached

    input_file.close()  # Close the file

# ------- FUNCTION to display the persons data in the dictionary that is passed as an argument
def display_data(person):
    print('Name:', person['name'])
    print('Age:', person['age'])
    print('Weight:', person['weight'])
    print()

# Call the main function
if __name__ == '__main__':
    main()