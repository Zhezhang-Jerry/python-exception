"""
program: student_data.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 7 2021
"""

import sys

def load_csv_data():
    """ load file, return content list and student_id """
    try:
        file_name = sys.argv[1]
        student_id = sys.argv[2]
        with open(file_name, 'r') as f:
            content = f.readlines()
            for i, data in enumerate(content[:]):
                list_person = data.strip().split(',')
                content[i] = list_person
    except FileNotFoundError:
        sys.exit(f'File {file_name} does not exist.')
    except IndexError:
        sys.exit(f'Usage: {sys.argv[0]} [input_file_name] [student_id]')

    return content, student_id


def get_student_data(list, student_id):
    """ find the student user wants """
    spstudent = [i for i in list if student_id == i[0]]

    return spstudent


def get_student_list(list):
    """ sort the student id list """
    id_list = set([i[0] for i in list])
    
    return sorted(id_list)


def main():
    student_list, student_id = load_csv_data()
    print(len(student_list))
    student_data = get_student_data(student_list, student_id)
    id_list = get_student_list(student_list)
    if student_id in id_list:
        print(f'\nStudent data for: {student_id}\n')
        for i in student_data:
            print(i)
    else:
        print(f'No data found for student: {student_id}')


main()