"""
program: sum_ints_2_soln.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 2 2021
"""
import sys
import os

def main():
    try:
        file_name = sys.argv[1]
        with open(file_name, 'r') as f:
            content = f.read()
    except IndexError:
        sys.exit(f'Usage: {os.path.basename(sys.argv[0])}[input_file_name]')
    except FileNotFoundError:
        sys.exit(f'{file_name} does not exist.')
    
    num_list = content.split()
    
    notnum_list = []
    total = 0
    for num in num_list:
        try:
            total += float(num)
        except ValueError:
            notnum_list.append(num)
                
    print(f'Sum: {total}\nTokens: {notnum_list} are invalid.')


main()

     
