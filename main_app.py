# Author : Nhlanhla 

import random
import datetime
import data_utils


def main():
    amount1 = random.randint(50, 500)
    amount2 = random.randint(50, 500)
    amount3 = random.randint(50, 500)
    amount4 = random.randint(50, 500)
    amount5 = random.randint(50, 500)

    
    
    average = data_utils.calculate_average( amount1, amount2, amount3, amount4, amount5)

    current_date = datetime.date.today()

    formatted_average = data_utils.format_currency(average)

    print('Transection summary')

    print("Date: ", current_date)
    print('Transection 1: ', amount1) 
    print('Transection 2: ', amount2)
    print('Transection 3: ', amount3)
    print('Transection 4: ', amount4)
    print('Transection 5: ', amount5)
    
    print("Average transection: ", formatted_average)



if __name__ == "__main__":
    main()
