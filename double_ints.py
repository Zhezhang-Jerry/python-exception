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
            content = f.readlines()
            num_list = [num.split() for num in content]
            nlist = []
            for ilist in num_list:
                for n in ilist:
                    nlist.append(n)

        total = 0
        for num in nlist:
            num = float(num)
            total += num

        print(f'Sum: {total}')
    except IndexError:
        sys.exit(f'Usage: {os.path.basename(sys.argv[0])}[input_file_name]')
    except FileNotFoundError:
        sys.exit(f'{file_name} does not exist.')
    except ValueError:
        notnum_list = []
        total = 0
        for num in nlist:
            if num.isalpha() is True:
                notnum = num
                notnum_list.append(notnum)                
            else:
                num = float(num)
                total += num
                
        sys.exit(f'Sum: {total:.2f}\nTokens: {notnum_list} are invalid.')


main()