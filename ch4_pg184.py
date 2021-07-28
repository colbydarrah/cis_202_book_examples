# Colby Darrah
# 2/8/2021
# Exercise pg184
# This program uses for loop to convert kph to mph in 10kph increments

#establish parameters
START_SPEED = 60            #starting speed
END_SPEED = 131             #ending speed
INCREMENT = 10              #speed increase increment
CONVERSION_FACTOR = 0.6214  #the factor to change kph to mph

#print table headings
print('kph\tmph')
print('---------------')

#create range
for kph in range (START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(f'{kph}\t{mph:.1f}')
