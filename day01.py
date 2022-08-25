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
