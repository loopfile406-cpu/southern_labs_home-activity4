# author: Nhlanhla
"""
Data Utilities Module
---------------------
Provides helper operations for custom mathematical workflows, including
calculating numerical list averages and formatting values as currency string tokens.
"""

def calculate_average(numbers_list):
    """
    Calculates the mathematical mean average value of a collection of numbers.

    Parameters:
    numbers_list (list): A list containing integer or float numerical values.

    Returns:
    float: The calculated mathematical average of the numbers in the list.
           Returns 0.0 if the input list is empty.
    """
    if len(numbers_list) == 0:
        return 0.0

    total_sum = sum(numbers_list)
    total_elements = len(numbers_list)
    return total_sum / total_elements


def format_currency(amount):
    """
    Formats a numeric amount into a standardized South African Rand (ZAR) string.

    Parameters:
    amount (float or int): The numerical currency balance total to format.

    Returns:
    str: A string showing the value formatted as South African Rand (e.g., R150.50).
    """
    formatted_number = "%.2f" % amount
    return "R" + formatted_number

