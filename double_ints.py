"""
program: double_ints.py
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
    total_int = 0
    total_float = 0
    for num in num_list:
        try:
            intnum = int(num)
            total_int += intnum
        except ValueError:
            try:
                floatnum = float(num)
                total_float += floatnum
            except ValueError:
                notnum_list.append(num)
                
    print(f'Sum of ints: {total_int}\nSum of floats: {total_float:.2f}\nTokens: {notnum_list} are invalid.')


main()