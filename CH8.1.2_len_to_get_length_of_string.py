# Colby Darrah
# 3/23/2021
# 8.1.2 pg 436
# use len to get length of string.

def main():
# EXAMPLE 1 ------------------------------------------------------------
    city = 'boston'
    size = len(city)
    print(size)

# Example 2 -----------------------------------------------------------
    print()
    # Use 'len' to prevent loops from iterating beyond end of string
    city = 'boston'
    index = 0
    while index < len(city):
        print(city[index])
        index += 1

# Call the main function
if __name__ == '__main__':
    main()