# Author : Nhlanhla
"""
Main Application Execution Script

Generates sample simulated transactions, updates tracking calculations via the 
local data_utils engine, and prints output summaries directly to the console terminal.
"""

import datetime
import random
import data_utils

def main():
    """
    Executes the main tracking flow application. Generates transaction parameters,
    calculates summary information metrics, and logs the results to the user view screen.
    """
    
    val1 = random.randint(50, 500)
    val2 = random.randint(50, 500)
    val3 = random.randint(50, 500)
    val4 = random.randint(50, 500)
    val5 = random.randint(50, 500)
    
    
    transaction_amounts = [val1, val2, val3, val4, val5]
    
    
    current_date = datetime.date.today()
    
    
    calculated_mean = data_utils.calculate_average(transaction_amounts)
    
    
    formatted_average = data_utils.format_currency(calculated_mean)
    
    
    print("Date: " + str(current_date))
    print("Generated Values: " + str(transaction_amounts))
    print("Calculated Currency String: " + str(formatted_average))


if __name__ == "__main__":
    main()


