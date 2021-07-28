# Colby Darrah
# 2/12/2021
# ex 4-08
# This program asks a user for a series of positive numbers and a
#negative number when they're done. At which time, the program displays
#the sum of all the positive numbers.

#set accumulator
total = 0.00
#get input from user
number = float(input("Please Enter a positive number: "))

 #create 'while loop' for negative numbers
while number >= 0:
    #add sum of numbers to accumulator
    total += number
    #get input from user
    number = float(input("Please Enter a positive number or a negative" +\
                          " number if done: "))

    #format total to include commas
    formated_total = '{:,.2f}'.format(total)

#print formated total
print(formated_total)
