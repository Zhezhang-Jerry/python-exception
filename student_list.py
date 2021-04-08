"""
program: student_list.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 7 2021
"""

import sys

def load_csv_data(file_name):
    """ Load file """
    with open(file_name, 'r') as f:
        content = f.readlines()
        for i, data in enumerate(content[:]):
            list_person = data.strip().split(',')
            content[i] = list_person

    return content


def get_student_list(list):
    """ sort the id """
    id_list = set([i[0] for i in list])
    
    return sorted(id_list)


def main():
    """ main function """
    try:
        file_name = sys.argv[1]
        student_list = load_csv_data(file_name)
        id_list = get_student_list(student_list)
        print(f'\nThere are {len(id_list)} registered students.\n')
        print('The first five students are')
        for i, id in enumerate(id_list):
            if i <= 4:
                print(f'{i+1}. {id}')
    except FileNotFoundError:
        sys.exit(f'{file_name} does not exist.')


main()