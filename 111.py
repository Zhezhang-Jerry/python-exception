"""
program: validate_data.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 7 2021
"""

import sys
import string

def load_csv_data():
    """ load file, return content list and student_id """
    try:
        file_name = input('Enter the file name: ')
        student_id = input('Enter the ID: ')
        with open(file_name, 'r') as f:
            content = f.readlines()
            for i, data in enumerate(content[:]):
                list_person = data.strip().split(',')
                content[i] = list_person
            new_content = content
            valid_ch = ['P', 'F', 'W']
            print() 
            for i, data in enumerate(content[:]):
                try:
                    new_content[i][1] = content[i][1] + ' ' + content[i][2]
                    new_content[i].pop(2)
                    if new_content[i][2] in valid_ch:
                        new_content[i][2] = new_content[i][2]
                        new_content[i][3] = int(new_content[i][3])
                        new_content[i][4] = new_content[i][4]
                    else:
                        new_content[i][2] = int(new_content[i][2])
                        new_content[i][3] = int(new_content[i][3])
                        new_content[i][4] = new_content[i][4]
                except (ValueError, IndexError):
                    print(f'warning: invalid data in record\n         {data} discarded')
                    new_content.pop(i)
    except FileNotFoundError:
        sys.exit(f'File {file_name} does not exist.')
    # except IndexError:
        # sys.exit(f'Usage: {sys.argv[0]} [input_file_name] [student_id]')

    return new_content, student_id


def valid_data(list):
    """ validate the student data """



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
    student_data = get_student_data(student_list, student_id)
    id_list = get_student_list(student_list)
    if student_id in id_list:
        print(f'\nStudent data for: {student_id}\n')
        for i in student_data:
            print(i)
    else:
        print(f'No data found for student: {student_id}')


main()