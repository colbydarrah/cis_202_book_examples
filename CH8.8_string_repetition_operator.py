# Colby Darrah
# 3/23/2021
# 8-8 spotlight  pg 452
# this program demonstrates teh repetition operator.

def main():
    # print the string, 'w' 5 times.
    my_string = 'w' * 5
    print(my_string)
    print()

    # print nine rows increasing in length.
    for count in range(1, 10):
        print('Z' * count)

    # Print nine rows decreasing in length.
    for count in range(8,0,-1):
        print('Z' * count)

# Call the main function
if __name__ == '__main__':
    main()