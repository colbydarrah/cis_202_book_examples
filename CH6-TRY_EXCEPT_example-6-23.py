# 6-23 pg 344 exception with division

# This program uses a TRY / EXCEPT function while calculating gross pay

def main():
    try:
        # get the number of hours worked.
        hours = int(input('How many hours did you work? '))

        # Get the hourly pay rate.
        pay_rate = float(input('Enter your hourly pay rate: '))

        # Calculate the gross pay.
        gross_pay = hours * pay_rate

        # Display gross pay.
        print(f'Gross Pay: ${gross_pay:,.2f}')
    # Except clause.
    except ValueError:
        #except handler
        print('ERROR: Hours worked and hourly pay rate must be valid numbers.')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+

