# author: Nhlanhla

"""
Utility module for proccessing transaction dat
"""



def calculate_average(num1, num2, num3, num4, num5):
    """
    Calculates the average of a list of numbers

    param: a list of numbers, interger or floating point numbers
    
    returns: average mathematical value
    """
    
    return (num1 + num2 + num3 + num4 + num5)/5


def format_currency (amount):
    """
    Formats a number as a South African rand.
    
    param : value to format

    returns formated south african currency as R number. as a float or intergar
    """
    x = round (amount, 2)
    value = f' R {x} '
    return value


