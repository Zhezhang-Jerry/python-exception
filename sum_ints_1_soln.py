"""
program: sum_ints_1_soln.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 2 2021
"""
import sys

def main():
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


main()