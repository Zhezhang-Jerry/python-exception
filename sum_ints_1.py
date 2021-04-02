"""
program: sum_ints_1.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 2 2021
"""
import sys

def   get_number()  -> int  :
    """ Prompt for   and   return a single integer. """
    valid = False
    while not valid:
        user_input = input("Enter a number: ")
        try:
            num  = int(user_input)
            valid = True
        except ValueError:
            print(f"Invalid Number '{user_input}'. Input must be number.")
    
    return num 


def main():
    """ Get two numbers, add them together, display result. """
    number_1 = get_number() 
    number_2 = get_number()
    the_sum = number_1 + number_2
    print('Sum:', the_sum)

main()