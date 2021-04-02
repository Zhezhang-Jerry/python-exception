"""
program: sum_ints_1_soln.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 2 2021
"""

def main():
    with open('numbers.txt', 'r') as f:
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

    print(f'Total number is {total}')


main()