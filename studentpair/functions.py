import random


# students = students in cohort
#pair_history = history of pairings

def pairup(students, pair_history):
    valid_pairs = []
    already_paired = []
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
        print("removing", student )
        never_paired.remove(student)
        print("never paired list ")
        print(never_paired)
        if len(never_paired) != 0:
            valid_pair = [student, never_paired[0]]
            valid_pairs.append(valid_pair)
            already_paired.append(student)
            already_paired.append(never_paired[0])
            print("student " + str(student))
            students.remove(student)
            print("never paired student " + str(never_paired[0]))
            students.remove(never_paired[0])
    not_paired_set = set(students) - set(already_paired)
    not_paired_list = list(not_paired_set)
    student_pairs = [] #pairs for this week
    single_student = []
    if len(not_paired_list) == 0:
        #all students have been paired
        print("DEPLETED")
        # pairup(not_paired_list)
    else:
        random.shuffle(not_paired_list)
        print('not paired', not_paired_list)
        # single_student = False
        if len(not_paired_list) % 2 == 0:
            group1 = not_paired_list[0:len(not_paired_list)//2]
            group2 = not_paired_list[len(not_paired_list)//2:]
            combined = zip(group1, group2)
            for pair in combined:
                pair_list = list(pair)
                student_pairs.append(pair_list)
        elif len(not_paired_list) > 2:
            unpaired = not_paired_list.pop(-1)        
            group1 = not_paired_list[0:len(not_paired_list)//2]
            group2 = not_paired_list[len(not_paired_list)//2:]
            combined = zip(group1, group2)
            print("COMBINED - ", combined)
            for pair in combined:
                pair_list = list(pair)
                student_pairs.append(pair_list)
            print("STUDENT PAIRS - ", student_pairs)
            student_pairs[0].append(unpaired)
        else:
            pair = not_paired_list[0]
            single_student.append(pair)
            # single_student=True

    print("STUDENT PAIRS - ", student_pairs)
    print("VALID PAIRS - ", valid_pairs)
    print("NOT PAIRED LIST - ", not_paired_list)
    final_valid_pairs = valid_pairs + student_pairs
    print('SINGLE STUDENT', single_student)
    if len(single_student) != 0:
        final_valid_pairs[0].append(single_student[0])
    print("HISTORY - ", pair_history)
    print("FINAL PAIRS - ", final_valid_pairs)
    return final_valid_pairs
# new_computed_pairs = pairup(students)
# for pair in new_computed_pairs:
#     if len(pair) == 2:
#         student1_id = pair[0]
#         student2_id = pair[1]
#     if len(pair) == 3:
#         student1_id = pair[0]
#         student2_id = pair[1]
#         student3_id = pair[2]