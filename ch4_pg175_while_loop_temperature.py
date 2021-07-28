# Colby Darrah
# 2/7/2021
# Exercise pg175
# This program uses while loop to instruct person to check temperature


#create variable to control loop
too_hot = 'y'

#determine if thermostate needs to be changed
while too_hot == 'y':
    #get temperature
    temperature = float(input("Enter substance's temperature: "))

    #is temperature too hot?
    if temperature > 102.5:
        too_hot = 'y'
        print("Turn down thermostate and recheck in 5 minutes")
    else:
        too_hot = 'n'
print("The temerature is acceptable. Recheck in 15 minutes")
