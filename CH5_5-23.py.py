# Colby Darrah

# Colby Darrah
# 2/27/2021
# In-Spotlight chapter example 5-23 pg. 266
# Commission generate
# This program calculates a salesperson's pay

def main():
    # get amount of sales.
    sales = get_sales()
    # Get the amount of advanced pay
    advanced_pay = get_advanced_pay()
    # determine commission rate.
    commission_rate = determine_commission_rate(sales)
    # calculate pay
    pay = sales * commission_rate - advanced_pay
    # display the amount of pay.
    print(f'the pay is ${pay:,.2f}.')

    #determine whether the pay is negative
    if pay < 0:
        print('The salesperson must reimburse')
        print('the company.')


# function to get amount in sales
def get_sales():
    sales = float(input("Enter total amount of sales: "))
    return sales


# function to get amount of advanced pay
def get_advanced_pay():
    advanced_pay = float(input("Enter amount of money advanced to employee: "))
    return advanced_pay

def determine_commission_rate(sales):
    #commission for sales less than 10k
    if sales < 10000:
        commission_rate = .1
    #commission for sales between 10k and 15k
    elif sales < 15000:
        commission_rate = .12
    #commission for sales between 1499.99 and 18k
    elif sales < 18000:
        commission_rate = .14
    #commission for sales between 1799.99 and 22k
    elif sales < 22000:
        commission_rate = .16
    #commission for sales above 2199.99
    else:
        commission_rate = .18
    #return
    return commission_rate

#call main function
main()
