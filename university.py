max_num_of_stud = int(input())
all_students = []
accepted_students = []

with open('applicants.txt', 'r') as f:
    file_content = f.readlines()
    lines_count = len(f.readlines())
    for line in file_content:
        all_students.append(line.strip('\n').split(' '))
    all_students.sort(key=lambda x: x[0])

selected = {
    'Biotech': [],
    'Chemistry': [],
    'Engineering': [],
    'Mathematics': [],
    'Physics': [],
}

dep_to_score_index = {
    'Biotech': [2, 3],
    'Chemistry': [3],
    'Engineering': [4, 5],
    'Mathematics': [4],
    'Physics': [2, 4],
    'Special': [6]
}


def select_for_department(students, dep_name, priority_index, score_index):
    candidates = []
    for s in students:
        if s[priority_index] == dep_name:
            candidates.append(s)
    candidates.sort(
        key=lambda x: -max(sum([float(x[st]) for st in score_index]) / len(score_index), float(x[6]))
    )
    return candidates


for wave in range(3):
    for department_name in ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']:
        score_index = dep_to_score_index[department_name]
        dep_priority_index = 7 + wave
        for candidate in select_for_department(all_students, department_name, dep_priority_index, score_index):
            if len(selected[department_name]) < max_num_of_stud and candidate not in accepted_students:
                selected[department_name].append(candidate)
                accepted_students.append(candidate)

for department_name in ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']:
    score_index = dep_to_score_index[department_name]
    selected[department_name].sort(
        key=lambda x: (-max(sum([float(x[st]) for st in score_index]) / len(score_index), float(x[6])), x[0], x[1])
    )
    dep_file = open(department_name.lower() + '.txt', 'w')
    candidates = selected[department_name]
    for index, name_and_score in enumerate(candidates):
        score = max(sum([float(name_and_score[s]) for s in score_index]) / len(score_index), float(name_and_score[6]))
        if index < len(candidates) - 1:
            dep_file.write(f'{name_and_score[0]} {name_and_score[1]} {score}\n')
        else:
            dep_file.write(f'{name_and_score[0]} {name_and_score[1]} {score}')
    dep_file.close()
