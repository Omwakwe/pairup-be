import random
from .models import StudentPair

from itertools import izip_longest



def create_pair(self, first_stundent, second_student):
    """
    Custom student model manager where first student and second student are picked
    randomly to make a pair.
    """
    #HISTORY
    pair_history = [
        [[‘Chai’, ‘Bob’, ‘Eric’, ‘Jill’, ‘Chris’, ‘Sam’, ‘Paul’, ‘Joe’]],
        [[‘Bob’, ‘Paul’, ‘Joe’, ‘Sam’, ‘Chai’, ‘Jill’, ‘Eric’, ‘Chris’]],
        [[‘Paul’, ‘Sam’, ‘Chai’, ‘Chris’, ‘Joe’, ‘Jill’, ‘Eric’, ‘Bob’]]
    ]
    original_students = [‘Joe’, ‘Sam’, ‘Bob’, ‘Jill’, ‘Paul’, ‘Eric’, ‘Chai’, ‘Chris’]
    students = [‘Joe’, ‘Sam’, ‘Bob’, ‘Jill’, ‘Paul’, ‘Eric’, ‘Chai’, ‘Chris’]
    valid_pairs = []
    already_paired = []
    def pairup(students):
        for student in students:
            student_history = []
            for week in pair_history:
                for pair in week:
                    if student in pair:
                        if len(pair) == 2:
                            if pair[0] == student:
                                student_history.append(pair[1])
                            if pair[1] == student:
                                student_history.append(pair[0])
                        if len(pair) == 3:
                            if pair[0] == student:
                                student_history.append(pair[1])
                                student_history.append(pair[2])
                            if pair[1] == student:
                                student_history.append(pair[0])
                                student_history.append(pair[2])
                            if pair[2] == student:
                                student_history.append(pair[0])
                                student_history.append(pair[1])
            never_paired_set= set(students) - set(student_history)
            never_paired= list(never_paired_set)
            never_paired.remove(student)
            print(“never paired list “)
            print(never_paired)
            valid_pair = [student, never_paired[0]]
            valid_pairs.append(valid_pair)
            already_paired.append(student)
            already_paired.append(never_paired[0])
            print(“student ” + student)
            students.remove(student)
            print(“never paired student ” + never_paired[0])
            students.remove(never_paired[0])
    not_paired_set = set(students) - set(already_paired)
    not_paired_list = list(not_paired_set)
    if len(not_paired_list) == len(original_students):
        print(“DEPLETED”)
        # pairup(not_paired_list)
    print(“not paired list”)
    print(not_paired_list)
    valid_pairs.append(not_paired_list)
    print(“VALID PAIRS”)
    print(valid_pairs)
    pairup(students)
    # pair_history.append(valid_pairs)
    print(” “)
    print(“HISTORY”)
    print(pair_history)
