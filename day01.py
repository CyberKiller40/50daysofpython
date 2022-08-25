import math

def divide_or_square(num):
    try:
        nummod = num%5
        if(nummod == 0):
            return round(math.sqrt(num), 2)
        else:
            return nummod
    except:
        print("Int or float required")

def longest_value(dictionary):
    try:
        longest = ''
        for item in dictionary.values():
            if len(item) > len(longest):
                longest = item
        return longest
    except:
        print("Dictionary required")

# dict for testing
# fruits = {
#     'first': 'one',
#     'fruit': 'apple',
#     'color': 'green',
#     'short': 'aaa'
# }

if __name__ == "__main__":
    import os
    import sys
    print(f"Don't run this script directly. Usage: import {os.path.splitext(os.path.basename(sys.argv[0]))[0]}")
