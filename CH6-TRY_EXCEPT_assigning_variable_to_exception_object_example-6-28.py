# 6-28 pg 350 try /except --- assigning a variable name to exception object

# When exception is thrown, an object called an "exception object" is created
# in memory. The "object" usually contains a default error message pertaining
# to the exception. When writing an exception clause, yo ucan optionally assign
# the "exception object" to a variable.
#   .....i.e.....except ValueError as err:
# The expression that appears after the exception calsue specifies you're assigning
# assigning the "exception object" to the variable. (any variable name can be used)
# The exception "handler (statements after exception line) can pass the object
# variable to the print function to display the default error message that Python
# provides for that type of error.

# This program uses a TRY / EXCEPT to calculate gross pay
# this program assigns the exception object to a variable.

def main():

    try:
        # Get the number of hours worked.
        hours - int(input('How many hours did you work? '))

        # Get the hourly pay rate.
        pay_rate = float(input('Enter your hourly pay rate: '))

        # Calcualte the gross pay.
        gross_pay = hours * pay_rate

        # Display the gross pay.
        print(f'Gross pay: #{gross_pay:,.2f}')
    except ValueError as err:
        print(err)


# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+

