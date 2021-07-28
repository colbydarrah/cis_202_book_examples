# 6-21 pg 342 exception with division

# This program divides a number by another number
# This program tests if the denominator is a zero and prints an error message

def main():

    # Get two numbers.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    # If num2 is not 0, divide num1 by num2 & display the result
    if num2 != 0:
        result = num1 / num2
        print(f'{num1} divided by {num2} is {result}')
    else
        print('Cannot divide by zero.')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+

