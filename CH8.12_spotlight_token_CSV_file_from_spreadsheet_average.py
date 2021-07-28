# Colby Darrah
# 3/23/2021
# 8-12    pg 457
# this program opens a CSV (comma separated values) originating from
# a spreadsheet of 5 grades from 5 students. The program tokenizes
# the information and calculates each students average score.

def main():
    # open the file
    csv_file = open('test_scores.csv', 'r')

    # Read the files lines into a list.
    lines = csv_file.readlines()

    #Close the file
    csv_file.close()

    # Process the lines
    for line in lines:
        # Get the test scores as tokens.
        tokens = line.split(',')

        # Calculate the total of the test scores.
        total = 0.0
        for token in tokens:
            total += float(token)

        # Calculate the average of the test scores.
        average = total / len(tokens)
        print(f'Average: {average}')




# Call the main function
if __name__ == '__main__':
    main()